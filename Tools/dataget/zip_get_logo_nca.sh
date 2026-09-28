#!/usr/bin/env bash

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

if [[ ! -f "./-.-/prod.keys" ]]; then
    echo
    echo "------------------------"
    echo "No existe prod.keys"
    echo "------------------------"
    echo
    read -rp "Pulsa ENTER para salir..."
    exit 1
fi

if [[ -z "$1" ]]; then
    echo "Uso: $0 archivo"
    read -rp "Pulsa ENTER para salir..."
    exit 1
fi

INPUT="$1"
INPUT_NAME="$(basename -- "$INPUT")"
INPUT_BASE="${INPUT_NAME%.*}"

rm -rf "nca"
mkdir -p "nca"

echo "Extrayendo $INPUT..."
unzip -j "$INPUT" -d "nca"

echo "Extraer nca para Logo..."

for NCA in nca/*.nca; do
    [[ -e "$NCA" ]] || continue

    INFO="$(./-.-/hactool -i -k ./-.-/prod.keys "$NCA" 2>/dev/null)"

    TITLE_ID="$(printf '%s\n' "$INFO" | sed -n 's/^Title ID:[[:space:]]*//p' | tail -n 1)"
    CONTENT_TYPE="$(printf '%s\n' "$INFO" | sed -n 's/^Content Type:[[:space:]]*//p' | tail -n 1)"

    echo "Title ID: $TITLE_ID"
    echo "Content Type: $CONTENT_TYPE"

    if [[ "$TITLE_ID" == "010000000000002d" && "$CONTENT_TYPE" != "Meta" ]]; then
        echo "$NCA"

        mkdir -p "Data/$INPUT_BASE"

        ./-.-/hactool -x -k ./-.-/prod.keys --exefsdir="Data/$INPUT_BASE" "$NCA"
        echo ./-.-/hactool -x -k ./-.-/prod.keys --exefsdir="Data/$INPUT_BASE" "$NCA"
        #cp $NCA "Data/$INPUT_BASE"

        python dataget.py "Data/$INPUT_BASE"

        break
    fi
done

rm -rf "nca"

echo "extraido"
echo "Completado"

read -rp "Pulsa ENTER para salir..."

