import argparse
import pandas as pd
import ollama
import time

def get_language_name(language_code):
    """
    Maps language codes to full language names.
    """
    language_map = {
        # Most spoken languages
        'ZH': 'Chinese',
        'ES': 'Spanish',
        'CA': 'Catalan',  
        'EN': 'English',
        'HI': 'Hindi',
        'AR': 'Arabic',
        'PT': 'Portuguese',
        'BN': 'Bengali',
        'RU': 'Russian',
        'JA': 'Japanese',
        'PA': 'Punjabi',
        'DE': 'German',
        'FR': 'French',
        'VI': 'Vietnamese',
        'MR': 'Marathi',
        'TA': 'Tamil',
        'UR': 'Urdu',
        'TR': 'Turkish',
        'IT': 'Italian',
        'FA': 'Persian (Farsi)',
        'PL': 'Polish',
        'UK': 'Ukrainian',
        'RO': 'Romanian',
        'NL': 'Dutch',
        'TH': 'Thai',
        'HU': 'Hungarian',
        'EL': 'Greek',
        'HE': 'Hebrew',
        'ID': 'Indonesian',
        'MS': 'Malay',
        'KO': 'Korean',
        'SW': 'Swahili',
        'FI': 'Finnish',
        'CS': 'Czech',
        'DA': 'Danish',
        'SV': 'Swedish',
        'SK': 'Slovak',
        'BG': 'Bulgarian',
        'HR': 'Croatian',
        'SR': 'Serbian',
        'SL': 'Slovenian',
        'LT': 'Lithuanian',
        'LV': 'Latvian',
        'ET': 'Estonian',
        'EU': 'Basque',
        'GL': 'Galician',
        'GA': 'Irish',
        'CY': 'Welsh',
        'MT': 'Maltese',
        'IS': 'Icelandic',
        'MK': 'Macedonian',
        'HY': 'Armenian',
        'BE': 'Belarusian',
        'SQ': 'Albanian',
        'BS': 'Bosnian',
        'LB': 'Luxembourgish',
        
    }

    return language_map.get(language_code.upper(), language_code)

def translate_text(text, target_lang, model):
    """Translates text using Ollama and logs timing and token usage."""
    if pd.isna(text) or text.strip() == "":
        return text

    # Language mapping
    language_name = get_language_name(target_lang)

    # Define multiple prompt options to test
    prompts = {
        "basic_enter": f"Translate the following text to {language_name}. Output only the translation without any line breaks or extra characters. Make sure the translation fits in one continuous line.\n\nText: {text}",
    }

    # Select the prompt variant to test (you can change this to switch between prompts)
    prompt = prompts["basic_enter"]  # Change this line to select a different prompt

    # Log start time
    start_time = time.time()  # Start timing translation for this row

    # LLM reponse
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])

    # Log end time
    end_time = time.time()  # End timing
    translation_time = end_time - start_time  # Elapsed time in seconds

    # Extract token statistics
    eval_count = response.get("eval_count", 0)  # Number of tokens processed
    total_duration = response.get("total_duration", 1) / 1e6  # Convert microseconds to seconds
    token_rate = eval_count / total_duration if total_duration > 0 else 0  # Tokens per second

    # Log timing and token info
    print(f"Row translation time: {translation_time:.2f} sec | Tokens: {eval_count} | Rate: {token_rate:.2f} tokens/sec")

    return response['message']['content'].strip()

import pandas as pd

def translate_csv(input_csv, columns, target_lang, model, back_translate=False):
    """
    Reads a CSV, translates specified columns using the dynamic prompt,
    and saves a new CSV with the translated columns.
    Each new column is named as original column name appended with an underscore
    and the target language code.
    After translation, the columns are also translated back to English.
    """

    df = pd.read_csv(input_csv, encoding="utf-8")

    # Check if each specified column exists
    for col in columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in CSV file.")
    
    print(f"Translating columns {columns} to {target_lang.upper()} using {model}...")

    # Translate each column to the target language and create new columns with the appended language code
    for col in columns:
        new_col_name = f"{col}_{target_lang.upper()}_{model}"
        df[new_col_name] = df[col].apply(lambda text: translate_text(text, target_lang, model) if pd.notnull(text) else text)

    # Optionally translate back the target language columns to English
    if back_translate:
        print(f"Translating back the columns to English...")
        for col in columns:
            target_col_name = f"{col}_{target_lang.upper()}"
            new_col_name_en = f"{col}_EN"
            df[new_col_name_en] = df[target_col_name].apply(lambda text: translate_text(text, "EN", model) if pd.notnull(text) else text)

    # Save the translated CSV file
    output_csv = input_csv.replace(".csv", f"_{target_lang.upper()}_{model}.csv")
    df.to_csv(output_csv, index=False)
    print(f"Translation complete. File saved as: {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate CSV column(s) using LLMs hosted locally from Ollama.")
    parser.add_argument("-i", "--input", type=str, default="input.csv", help="Input CSV file (default: input.csv)")
    parser.add_argument("-o", "--output", type=str, help="Output CSV file (default: input_filename_LANGCODE.csv)")
    parser.add_argument("-l", "--language", type=str, default="ES", help="Target language (default: ES for Spanish)")
    parser.add_argument("-m", "--model", type=str, default="llama3.2:latest", help="LLM model to use (default: llama3)")
    parser.add_argument("-c", "--columns", nargs="+", required=True, help="Column names to translate (space-separated)")

    args = parser.parse_args()
    translate_csv(args.input, args.columns, args.language, args.model)
