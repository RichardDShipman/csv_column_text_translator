#!/bin/bash

# Define language two leter codes
LANG_CODES=(
    # Spoken languages
     "ES" "PT" "DE" "FR" "NL" "AR" "RU" "ZH" "JA" #"KO" "TH" "VI" "HI" "BN" "MR" "PA" "TA" "UR" "TR" "IT" "FA" "PL" "UK" "RO" "NL"  "HU" "EL" "HE" "ID" "MS" "KO" "SW" "FI" "CS" "DA" "SV" "SK" "BG" "HR" "SR" "SL" "LT" "LV" "ET" "EU" "GL" "GA" "CY" "MT" "IS" "MK" "HY" "BE" "SQ" "BS" "LB"
    
    # Fantasy and Sci-Fi languages
    #"ELV" "DWV" "PRT" "HVL" "DTH" "KLN" "OTL" "NAV" "BJR" "HTS" "VLC" "ESP" "SML" "ATL" "MNS" "VKR" "PIR" "TSL" "LOTR" "GND" "YDI" "SNO"

    # Emoji and Brain Rot languages
    #"EMJ" "BRR"

)

# Define Ollama hosted models
MODELS=(
    "mistral:latest"
    "llama3.2:latest"
    "llama3.2:1b"
    "qwen2.5:0.5b"
    "qwen2.5:1.5b"
    "deepseek-r1"
    "deepseek-r1:1.5b"
    "gemma3:4b"
)

# Define columns to translate
COLUMNS=("term" "definition")  # Change to the columns you want to translate

# Parent directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Define input file (fantasy language plus+++)
INPUT_FILE="$PROJECT_ROOT/data/test_input.csv"

# Loop through all models and language codes and run the Python script
for MODEL in "${MODELS[@]}"; do
    for LANG in "${LANG_CODES[@]}"; do
        echo "Translating into $LANG using model $MODEL..."
        python "$PROJECT_ROOT/src/csv_column_translator.py" -i "$INPUT_FILE" -l "$LANG" -m "$MODEL" -c "${COLUMNS[@]}"
    done
done

echo "Translation for all languages complete!"
