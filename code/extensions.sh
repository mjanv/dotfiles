#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXTENSIONS_FILE="${SCRIPT_DIR}/extensions.txt"

usage() {
    cat <<EOF
Usage: $(basename "$0") <command>

Commands:
    save      Save currently installed extensions (with versions) to extensions.txt
    install   Install extensions from extensions.txt
    prune     Remove extensions not present in extensions.txt
    sync      Install missing + prune unused (install + prune)
    diff      Show differences between installed and saved extensions
EOF
    exit 1
}

get_installed() {
    code --list-extensions --show-versions 2>/dev/null | sort
}

get_saved() {
    if [[ ! -f "$EXTENSIONS_FILE" ]]; then
        echo "Error: $EXTENSIONS_FILE not found. Run 'save' first." >&2
        exit 1
    fi
    sort "$EXTENSIONS_FILE"
}

cmd_save() {
    echo "Saving extensions to $EXTENSIONS_FILE..."
    get_installed > "$EXTENSIONS_FILE"
    local count
    count=$(wc -l < "$EXTENSIONS_FILE")
    echo "Saved $count extensions."
}

cmd_install() {
    get_saved | while IFS= read -r ext; do
        [[ -z "$ext" ]] && continue
        echo "Installing $ext..."
        code --install-extension "$ext" --force || echo "  Failed to install $ext"
    done
    echo "Done."
}

cmd_prune() {
    local saved installed to_remove
    saved=$(get_saved | cut -d@ -f1 | tr '[:upper:]' '[:lower:]')
    installed=$(get_installed | cut -d@ -f1)

    to_remove=()
    while IFS= read -r ext; do
        [[ -z "$ext" ]] && continue
        ext_lower=$(echo "$ext" | tr '[:upper:]' '[:lower:]')
        if ! echo "$saved" | grep -qxF "$ext_lower"; then
            to_remove+=("$ext")
        fi
    done <<< "$installed"

    if [[ ${#to_remove[@]} -eq 0 ]]; then
        echo "No extensions to remove."
        return
    fi

    echo "Extensions to remove:"
    printf '  %s\n' "${to_remove[@]}"
    echo
    read -rp "Proceed? [y/N] " confirm
    if [[ "$confirm" =~ ^[Yy]$ ]]; then
        for ext in "${to_remove[@]}"; do
            echo "Removing $ext..."
            code --uninstall-extension "$ext" || echo "  Failed to remove $ext"
        done
        echo "Done."
    else
        echo "Aborted."
    fi
}

cmd_diff() {
    local saved_exts installed_exts
    saved_exts=$(get_saved | cut -d@ -f1 | tr '[:upper:]' '[:lower:]' | sort)
    installed_exts=$(get_installed | cut -d@ -f1 | tr '[:upper:]' '[:lower:]' | sort)

    echo "=== Missing (in saved but not installed) ==="
    comm -23 <(echo "$saved_exts") <(echo "$installed_exts") | sed 's/^/  /'

    echo
    echo "=== Extra (installed but not in saved) ==="
    comm -13 <(echo "$saved_exts") <(echo "$installed_exts") | sed 's/^/  /'
}

cmd_sync() {
    cmd_install
    cmd_prune
}

[[ $# -lt 1 ]] && usage

case "$1" in
    save)    cmd_save ;;
    install) cmd_install ;;
    prune)   cmd_prune ;;
    sync)    cmd_sync ;;
    diff)    cmd_diff ;;
    *)       usage ;;
esac