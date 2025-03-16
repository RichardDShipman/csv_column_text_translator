#!/bin/bash

# Define the list of language codes (real languages)
#LANG_CODES=("ZH" "ES" "EN" "HI" "AR" "PT" "BN" "RU" "JA" "PA" "DE" "FR" "VI" "MR" "TA" "UR" "TR" "IT" "FA" "PL" "UK" "RO" "NL" "TH" "HU" "EL" "HE" "ID" "MS" "KO" "SW" "FI" "CS" "DA" "SV" "SK" "BG" "HR" "SR" "SL" "LT" "LV" "ET" "CA" "EU" "GL" "GA" "CY" "MT" "IS" "MK" "HY" "BE" "SQ" "BS" "LB")

LANG_CODES=(
    # Spoken languages
     "ES" #"PT" "DE" "FR" "NL" "AR" "RU" "ZH" "JA" "TH" # "KO" "VI" "HI" "BN" "MR" "PA" "TA" "UR" "TR" "IT" "FA" "PL" "UK" "RO" "NL"  "HU" "EL" "HE" "ID" "MS" "KO" "SW" "FI" "CS" "DA" "SV" "SK" "BG" "HR" "SR" "SL" "LT" "LV" "ET" "EU" "GL" "GA" "CY" "MT" "IS" "MK" "HY" "BE" "SQ" "BS" "LB"
    
    # Fantasy and Sci-Fi languages
    #"ELV" "DWV" "PRT" "HVL" "DTH" "KLN" "OTL" "NAV" "BJR" "HTS" "VLC" "ESP" "SML" "ATL" "MNS" "VKR" "PIR" "TSL" "LOTR" "GND" "YDI" "SNO"

    # Emoji and Brain Rot languages
    #"EMJ" "BRR"

)

# Define input file (fantasy language plus+++)
INPUT_FILE="export.csv"

# Define Ollama hosted model
#MODEL="llama3.2:latest"  # Adjust if needed
MODEL="llama3.2:1b"
#MODEL="qwen2.5:0.5b"
#MODEL="qwen2.5:1.5b"
#MODEL="deepseek-r1"
#MODEL="deepseek-r1:1.5b"

# Define columns to translate
COLUMNS=("name")  # Change to the columns you want to translate

# Loop through all language codes and run the Python script
for LANG in "${LANG_CODES[@]}"; do
    echo "Translating into $LANG..."
    python csv_column_translator.py -i "$INPUT_FILE" -l "$LANG" -m "$MODEL" -c "${COLUMNS[@]}"
done

echo "Translation for all languages complete!"
