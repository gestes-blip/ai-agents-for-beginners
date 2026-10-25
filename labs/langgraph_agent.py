"""Lab: single LangGraph agent, two tools (web search + calculator),
conditional edge routes between tool use and a direct answer. Runs on a local Foundry Local model."""
import ast, operator, sys, warnings
warnings.filterwarnings("ignore")
from typing import Annotated
from typing_extensions import TypedDict
from foundry_local_sdk import Configuration, FoundryLocalManager
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

# ---- local model ----
FoundryLocalManager.initialize(Configuration(app_name="foundry_local_samples"))
mgr = FoundryLocalManager.instance
local_model = mgr.catalog.get_model("qwen2.5-7b")
local_model.download(); local_model.load(); mgr.start_web_service()
url = mgr.urls[0].rstrip("/")
llm = ChatOpenAI(base_url=url + "/v1", api_key="not-required", model=local_model.id, temperature=0)

# ---- tools ----
OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
       ast.Div: operator.truediv, ast.Pow: operator.pow, ast.USub: operator.neg, ast.Mod: operator.mod}
def _eval(n):
    if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)): return n.value
    if isinstance(n, ast.BinOp): return OPS[type(n.op)](_eval(n.left), _eval(n.right))
    if isinstance(n, ast.UnaryOp): return OPS[type(n.op)](_eval(n.operand))
    raise ValueError("unsupported expression")

@tool
def calculator(expression: str) -> str:
    """Evaluate a math expression such as '23 * (4 + 5) / 3'. Use for any arithmetic."""
    try: return str(_eval(ast.parse(expression, mode="eval").body))
    except Exception as e: return f"error: {e}"

@tool
def web_search(query: str) -> str:
    """Search the web and return the top results as short snippets. Use for current facts."""
    from ddgs import DDGS
    try:
        hits = DDGS().text(query, max_results=3)
        return "\n".join(f"- {h['title']}: {h['body']}" for h in hits) or "no results"
    except Exception as e: return f"search error: {e}"

tools = [calculator, web_search]
llm_with_tools = llm.bind_tools(tools)

# ---- graph ----
class State(TypedDict):
    messages: Annotated[list, add_messages]

SYSTEM = SystemMessage(
    "You are a helpful assistant with two tools.\n"
    "RULES:\n"
    "1. For ANY arithmetic, you MUST call the calculator tool. Never compute numbers yourself.\n"
    "2. For news, sports results, or anything that may have changed recently, you MUST call web_search, "
    "and base your answer ONLY on the search results (quote the dates and scores they give).\n"
    "3. For greetings, translations, or general knowledge, answer directly without tools.")

def agent(state: State):
    return {"messages": [llm_with_tools.invoke([SYSTEM] + state["messages"])]}

def route(state: State):          # the conditional edge
    return "tools" if state["messages"][-1].tool_calls else END

g = StateGraph(State)
g.add_node("agent", agent)
g.add_node("tools", ToolNode(tools))
g.add_edge(START, "agent")
g.add_conditional_edges("agent", route, {"tools": "tools", END: END})
g.add_edge("tools", "agent")
app = g.compile()

for q in ["What is 23 * (4 + 5) / 3?",
          "Who won the most recent Super Bowl, and what is the score?",
          "Say hello in French.",
          "What is 15% of 2480, plus 37?"]:
    print("\nQ:", q, flush=True)
    for step in app.stream({"messages": [HumanMessage(q)]}, stream_mode="updates"):
        for node, out in step.items():
            m = out["messages"][-1]
            if node == "agent" and m.tool_calls: print("  agent -> tool call:", [(c["name"], c["args"]) for c in m.tool_calls], flush=True)
            elif node == "tools": print("  tool result:", str(m.content)[:150].replace("\n"," "), flush=True)
            else: print("  final:", m.content[:300], flush=True)
mgr.stop_web_service(); local_model.unload()
