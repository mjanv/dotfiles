#!/bin/bash

# Read JSON input from stdin
input=$(cat)

# Extract model display name
MODEL=$(echo "$input" | jq -r '.model.display_name')

# Extract current directory and get basename
CURRENT_DIR=$(echo "$input" | jq -r '.workspace.current_dir')
DIR_NAME=$(basename "$CURRENT_DIR")

# Get git branch if in a git repo
GIT_BRANCH=""
cd "$CURRENT_DIR" 2>/dev/null
if git rev-parse --git-dir > /dev/null 2>&1; then
    BRANCH=$(git branch --show-current 2>/dev/null)
    if [ -n "$BRANCH" ]; then
        GIT_BRANCH="/$BRANCH"
    fi
fi

# Extract hook event (will show what triggered this)
HOOK=$(echo "$input" | jq -r '.hook_event_name // "Status"')

# Extract cost information
COST=$(echo "$input" | jq -r '.cost.total_cost_usd // 0')
COST_FORMATTED=$(printf "\$%.2f" "$COST")

# Calculate context window usage percentage
CONTEXT_SIZE=$(echo "$input" | jq -r '.context_window.context_window_size // 200000')
USAGE=$(echo "$input" | jq '.context_window.current_usage')

if [ "$USAGE" != "null" ]; then
    INPUT_TOKENS=$(echo "$USAGE" | jq -r '.input_tokens // 0')
    CACHE_CREATE=$(echo "$USAGE" | jq -r '.cache_creation_input_tokens // 0')
    CACHE_READ=$(echo "$USAGE" | jq -r '.cache_read_input_tokens // 0')
    CURRENT_TOKENS=$((INPUT_TOKENS + CACHE_CREATE + CACHE_READ))
    PERCENT_USED=$((CURRENT_TOKENS * 100 / CONTEXT_SIZE))
    CONTEXT_INFO="${PERCENT_USED}%"
else
    CONTEXT_INFO="0%"
fi

# Format: Model - Dir/Branch - Hook - Cost - Context
echo "${MODEL} - ${DIR_NAME}${GIT_BRANCH} - ${HOOK} - ${COST_FORMATTED} - ${CONTEXT_INFO}"