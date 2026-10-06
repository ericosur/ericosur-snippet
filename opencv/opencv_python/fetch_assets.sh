#!/usr/bin/env bash
set -e

# ==================== Configuration (Modify here for new releases) ====================
REPO="ericosur/private"
DEFAULT_TAG="v0.0.1-alpha"
DEFAULT_ASSET="image-assets-v0.0.2.zip"
# ======================================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="${SCRIPT_DIR}/data"
mkdir -p "$DATA_DIR"

# Parse CLI arguments
INPUT_ZIP=""
TAG="$DEFAULT_TAG"
ASSET_NAME="$DEFAULT_ASSET"
FORCE=false
POSITIONAL_TAG_SET=""
POSITIONAL_ASSET_SET=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        -i|--input)
            if [ -z "$2" ] || [[ "$2" == -* ]]; then
                echo "[ERROR] Missing argument for $1"
                exit 1
            fi
            INPUT_ZIP="$2"
            shift 2
            ;;
        -f|--force)
            FORCE=true
            shift
            ;;
        -t|--tag)
            if [ -z "$2" ] || [[ "$2" == -* ]]; then
                echo "[ERROR] Missing argument for $1"
                exit 1
            fi
            TAG="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: $0 [options] [TAG] [ASSET_NAME]"
            echo ""
            echo "Options:"
            echo "  -f, --force          Run automatically without confirmation prompts"
            echo "  -i, --input <file>   Use a locally provided zip file instead of downloading via GitHub CLI"
            echo "  -t, --tag <tag>      Specify release tag (default: $DEFAULT_TAG)"
            echo "  -h, --help           Show this help message"
            echo ""
            echo "Examples:"
            echo "  $0                                        # Prompt user before downloading"
            echo "  $0 -f                                     # Automatically download default release asset"
            echo "  $0 -f -i /path/to/image-assets.zip        # Manually provided zip without prompt"
            echo "  $0 -f v0.0.2-alpha image-assets-v0.0.2.zip # Automatically download specific release version"
            exit 0
            ;;
        *)
            if [ -z "$POSITIONAL_TAG_SET" ]; then
                TAG="$1"
                POSITIONAL_TAG_SET=1
            elif [ -z "$POSITIONAL_ASSET_SET" ]; then
                ASSET_NAME="$1"
                POSITIONAL_ASSET_SET=1
            fi
            shift
            ;;
    esac
done

# Pre-flight check: unzip is required in all modes
if ! command -v unzip &> /dev/null; then
    echo "[ERROR] 'unzip' is not installed."
    echo "Install it via: sudo apt install unzip"
    exit 1
fi

# Confirmation prompt when --force is not specified
if [ "$FORCE" = false ]; then
    echo "======================================================================"
    echo " Target directory: ${DATA_DIR}"
    echo " Files in this directory will be extracted and may overwrite existing"
    echo " files. Note that '${DATA_DIR}' is NOT tracked by Git (.gitignored)."
    echo "======================================================================"
    read -r -p "Do you want to proceed? [y/N]: " CONFIRM || CONFIRM="n"
    case "$CONFIRM" in
        [yY][eE][sS]|[yY])
            echo "==> Proceeding..."
            ;;
        *)
            echo "==> Operation cancelled by user. No files were modified."
            exit 0
            ;;
    esac
fi

CLEANUP_ZIP=false
ZIP_SOURCE=""

if [ -n "$INPUT_ZIP" ]; then
    # Mode 1: Manual local zip file
    if command -v cygpath &> /dev/null; then
        INPUT_ZIP="$(cygpath -u "$INPUT_ZIP")"
    fi
    if [ ! -f "$INPUT_ZIP" ]; then
        echo "[ERROR] Specified input file does not exist: $INPUT_ZIP"
        exit 1
    fi
    ZIP_SOURCE="$(cd "$(dirname "$INPUT_ZIP")" && pwd)/$(basename "$INPUT_ZIP")"
    echo "==> Using manually provided zip archive: $ZIP_SOURCE"
else
    # Mode 2: Download via GitHub CLI
    if ! command -v gh &> /dev/null; then
        echo "[ERROR] GitHub CLI ('gh') is not installed."
        echo "Install it via: sudo apt install gh"
        exit 1
    fi

    echo "==> Checking GitHub CLI authentication status..."
    if ! gh auth status &> /dev/null; then
        echo "[WARNING] You are not logged in to GitHub CLI."
        echo "Please run 'gh auth login' to authenticate."
        exit 1
    fi

    echo "==> Target Repo  : $REPO"
    echo "==> Target Tag   : $TAG"
    echo "==> Target Asset : $ASSET_NAME"
    echo "==> Downloading test assets from private repo..."

    (
        cd "$DATA_DIR"
        gh release download "$TAG" \
          --repo "$REPO" \
          --pattern "$ASSET_NAME" \
          --dir . \
          --clobber
    )

    ZIP_SOURCE="${DATA_DIR}/${ASSET_NAME}"
    if [ ! -f "$ZIP_SOURCE" ]; then
        echo "[ERROR] Downloaded archive not found: ${ZIP_SOURCE}"
        exit 1
    fi
    CLEANUP_ZIP=true
fi

# Extract and normalize folder structure
echo "==> Extracting assets to ${DATA_DIR}..."
TEMP_EXTRACT_DIR=$(mktemp -d)

unzip -o -q "$ZIP_SOURCE" -d "$TEMP_EXTRACT_DIR"

# Prevent 'data/data/': if zip already has a root 'data/' directory, extract its contents directly into DATA_DIR
if [ -d "${TEMP_EXTRACT_DIR}/data" ]; then
    cp -r "${TEMP_EXTRACT_DIR}/data/." "$DATA_DIR/"
else
    cp -r "${TEMP_EXTRACT_DIR}/." "$DATA_DIR/"
fi

rm -rf "$TEMP_EXTRACT_DIR"

if [ "$CLEANUP_ZIP" = true ]; then
    rm -f "$ZIP_SOURCE"
fi

echo "==> Success! All test images are ready in ${DATA_DIR}."
