#!/bin/sh
# Install the AI Starter skills into every agent found on this machine.
#
#   sh install.sh             copy the skills
#   sh install.sh --link      symlink instead of copy (updates follow git pull)
#   sh install.sh --dry-run   print what would happen, change nothing
#   sh install.sh --uninstall remove the skills this script installed
#   sh install.sh --force     also replace a different skill with the same name
#
# Where each tool reads personal skills (checked against each tool's docs):
#   Claude Code             ~/.claude/skills
#   Codex, Pi, and other    ~/.agents/skills   (Pi would warn on a second copy in
#   Agent Skills tools                          ~/.pi/agent/skills, so none goes there)
#   Hermes                  ~/.hermes/skills
# POSIX sh, no dependencies.

set -u

# AI_STARTER_HOME installs into another home folder (for tests).
H=${AI_STARTER_HOME:-$HOME}
SKILLS="ai-starter-onboarding ai-starter-process-scan ai-starter-first-skill ai-starter-skill-check"
MARK=".ai-starter-install"

DRY=0 UNINSTALL=0 FORCE=0 LINK=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY=1 ;;
    --uninstall) UNINSTALL=1 ;;
    --force) FORCE=1 ;;
    --link) LINK=1 ;;
    -h|--help) sed -n '2,9p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown option: $arg (try --help)" >&2; exit 2 ;;
  esac
done

SRC=$(cd "$(dirname "$0")/skills" 2>/dev/null && pwd -P) || { echo "skills/ folder not found next to install.sh" >&2; exit 1; }

run() {
  if [ "$DRY" = 1 ]; then echo "    would run: $*"; else "$@"; fi
}

has() { command -v "$1" >/dev/null 2>&1; }

# A skill folder is ours if it is a symlink into this repo or carries our marker file.
ours() {
  if [ -L "$1" ]; then
    case "$(readlink "$1")" in "$SRC"/*) return 0 ;; esac
    return 1
  fi
  [ -f "$1/$MARK" ]
}

handle() { # $1 label, $2 skills dir
  label=$1 dir=$2
  echo "$label -> $dir"
  for s in $SKILLS; do
    dest="$dir/$s"
    if [ "$UNINSTALL" = 1 ]; then
      if [ ! -e "$dest" ] && [ ! -L "$dest" ]; then
        echo "  $s: not installed"
      elif ours "$dest" || [ "$FORCE" = 1 ]; then
        echo "  $s: remove"; run rm -rf "$dest"
      else
        echo "  $s: SKIP, not installed by AI Starter (use --force to remove it anyway)"
      fi
      continue
    fi
    if [ -e "$dest" ] || [ -L "$dest" ]; then
      if ours "$dest"; then
        echo "  $s: update"
      elif [ "$FORCE" = 1 ]; then
        echo "  $s: replace a different skill (--force)"
      else
        echo "  $s: SKIP, a different skill already has this name (use --force to replace it)"
        continue
      fi
      run rm -rf "$dest"
    else
      echo "  $s: install"
    fi
    run mkdir -p "$dir"
    if [ "$LINK" = 1 ]; then
      run ln -s "$SRC/$s" "$dest"
    else
      run cp -R "$SRC/$s" "$dest"
      if [ "$DRY" = 1 ]; then echo "    would write: $dest/$MARK"
      else echo "copied from $SRC/$s by ai-starter install.sh" > "$dest/$MARK"; fi
    fi
  done
}

found=0
[ "$DRY" = 1 ] && echo "Dry run: nothing will change."

# Claude Code. The plugin already provides these skills, so a second copy is skipped.
if [ -d "$H/.claude" ] || has claude; then
  found=1
  if [ "$UNINSTALL" = 0 ] && grep -q '"ai-starter@' "$H/.claude/plugins/installed_plugins.json" 2>/dev/null; then
    echo "Claude Code -> already has the ai-starter plugin, skipped (no second copy)"
  else
    handle "Claude Code" "$H/.claude/skills"
  fi
fi

# Codex, Pi and any tool reading the open Agent Skills location.
if [ -d "$H/.agents" ] || [ -d "$H/.codex" ] || [ -d "$H/.pi" ] || has codex || has pi; then
  found=1
  handle "Codex, Pi, Agent Skills tools" "$H/.agents/skills"
fi

# Hermes.
if [ -d "$H/.hermes" ] || has hermes; then
  found=1
  handle "Hermes" "$H/.hermes/skills"
fi

if [ "$found" = 0 ]; then
  echo "No supported agent found (Claude Code, Codex, Pi, Hermes)."
  echo "Copy the folders in $SRC into your tool's skills folder by hand."
  exit 1
fi
[ "$DRY" = 1 ] || [ "$UNINSTALL" = 1 ] || echo "Done. Start a new session and say: start AI Starter"
