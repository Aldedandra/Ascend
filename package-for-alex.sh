#!/bin/zsh

set -e

PROJECT_DIR="$HOME/Projects/Ascend"
OUTPUT_DIR="$HOME/Projects"
DATE_TAG=$(date +"%Y%m%d-%H%M")
OUTPUT_FILE="$OUTPUT_DIR/Ascend-source-$DATE_TAG.zip"

cd "$PROJECT_DIR"

echo "Creating Ascend source package..."
echo "Output: $OUTPUT_FILE"

zip -r "$OUTPUT_FILE" . \
  -x ".git/*" \
     "frontend/node_modules/*" \
     "frontend/dist/*" \
     "frontend/public/audio/*" \
     "frontend/ios/App/App/public/*" \
     "*/.DS_Store" \
     ".DS_Store" \
     "*/Thumbs.db" \
     "Thumbs.db" \
     ".env"

echo
echo "Package complete:"
ls -lh "$OUTPUT_FILE"
