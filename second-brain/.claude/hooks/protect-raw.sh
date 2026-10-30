#!/usr/bin/env bash
# Blocks any tool call that would change files in raw/.
# Claude Code passes the tool call as JSON on stdin; exit code 2 blocks it and
# sends stderr back to Claude. No jq or python needed.

input=$(cat)

# Edit, Write, MultiEdit, NotebookEdit: block when the target path is inside raw/.
if printf '%s' "$input" | grep -Eq '"(file_path|notebook_path)"[[:space:]]*:[[:space:]]*"([^"]*[/\\])?raw[/\\]'; then
  echo "Blocked: raw/ is read-only. Write summaries and pages to wiki/ instead." >&2
  exit 2
fi

# Bash: block commands that mention raw/ together with something that modifies files.
if printf '%s' "$input" | grep -q '"tool_name"[[:space:]]*:[[:space:]]*"Bash"'; then
  cmd=$(printf '%s' "$input" | grep -o '"command"[[:space:]]*:[[:space:]]*"[^"]*' | head -1)
  if { printf '%s' "$cmd" | grep -Eq '(^|[^A-Za-z0-9_])raw/' &&
       printf '%s' "$cmd" | grep -Eq '(^|[^A-Za-z0-9_-])(rm|mv|sed[[:space:]]+-i|truncate|chmod|unlink|perl[[:space:]]+-pi)([^A-Za-z0-9_-]|$)'; } ||
     printf '%s' "$cmd" | grep -Eq '(>|tee[[:space:]]+(-a[[:space:]]+)?|touch[[:space:]]+)[[:space:]]*("|\\")?(\./)?raw/'; then
    echo "Blocked: this command would modify raw/, which is read-only." >&2
    exit 2
  fi
fi

exit 0
