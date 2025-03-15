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
        'CA': 'Catalan/Valencian',  
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

        # Fantasy Languages
        'ELV': 'Elvish (Sindarin and Quenya) - Tolkien’s Elvish languages, highly developed with complex grammar.',
        'DWV': 'Dwarvish (Khuzdul) - A Semitic-inspired language from Tolkien’s works, spoken by the Dwarves.',
        'PRT': 'Parseltongue - The language of serpents from J.K. Rowling’s *Harry Potter* series.',
        'HVL': 'High Valyrian - A fully developed language from *Game of Thrones*, created by David J. Peterson.',
        'DTH': 'Dothraki - A language created by David J. Peterson for the *Game of Thrones* series.',
        'KLN': 'Klingon - A popular constructed language from *Star Trek*, with a distinct syntax and vocabulary.',
        'OTL': 'The Old Tongue - An ancient and obscure language from *The Wheel of Time* series.',
        
        # Science Fiction Languages
        'NAV': 'Na\'vi - The language of the indigenous people from *Avatar*, designed to fit the fictional world.',
        'BJR': 'Bajoran - A language from *Star Trek: Deep Space Nine*, spoken by the Bajoran people.',
        'HTS': 'Huttese - A language from *Star Wars*, spoken by the Hutt species and other characters.',
        'VLC': 'Vulcan - A logical, structured language from *Star Trek*, spoken by the Vulcan species.',
        'ESP': 'Esperanto - A constructed international auxiliary language, featured in *Star Trek* and used for intergalactic communication.',
        'SML': 'Simlish - The nonsensical, playful language from *The Sims* series, widely recognized in pop culture.',
        
        # Other Fictional Languages
        'ATL': 'Atlantean - The language from Disney’s *Atlantis: The Lost Empire*, designed to fit the mythic world of Atlantis.',
    
        # Additional Fun and Popular Fictional Languages
        'MOR': 'Morse Code - A simple system of encoding textual information using sequences of dots and dashes, used for communication.',
        'R2D': 'Droid Speak (R2-D2) - A series of beeps, whistles, and tones used by the droids in the *Star Wars* universe.',
        'LOTR': 'Rohan - A language from *Lord of the Rings*, based on Old English and spoken by the people of Rohan.',
        'GND': 'Gungan - The language spoken by Jar Jar Binks and other Gungans in *Star Wars*.',
        'MNS': 'Minionese - A playful, nonsensical language used by the Minions from the *Despicable Me* series.',
        'YDI': 'Yoda Speak - A distinctive form of speech used by the character Yoda in *Star Wars*, often involving reversed word order.',
        'BFE': 'Belfast English - The unique dialect and slang from the city of Belfast in Northern Ireland.',
        'DTH': 'Dothraki - The language of the Dothraki people from *Game of Thrones*, created by linguist David J. Peterson.',
        'SNA': 'Simlish - The nonsensical language from *The Sims*, often used to create humorous or emotional tone without structured grammar.',
        'VKR': 'Vulcan - A language from *Star Trek*, focusing on logic and structure, spoken by the Vulcan species.',
        'PIR': 'Pirate Speak - A playful and exaggerated English-based dialect used to imitate pirate speech.',
        'TSL': 'Twi’lek - The language of the Twi’lek people in the *Star Wars* universe, though it is not fully fleshed out, it appears in the background of the series.',
        'ELD': 'Elder Speech - The language of the Elves in *The Witcher* series, which has elements of Old English and Latin.',
        'SNO': 'Shyriiwook - The language of the Wookiees, including Chewbacca, from *Star Wars*, characterized by growls and roars.',
    
        # Emoji-based Language
        'EMJ': 'Emoji Language - A symbolic language using emojis to represent feelings, actions, or concepts. For example, ❤️ (love), 🐱 (cat), 🌧️ (rain), etc.',
    
        # Brain Rot Language
        'BRR': 'Brain Rot - A nonsensical, meme-inspired language that often combines absurd phrases, exaggerated emotions, and internet slang. Example: "💀 I can’t even, like, bruh 😭✨😫".',

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
        "basic": f"Translate the following text to {language_name}. Output only the translation.\n\nText: {text}",
        "semantic_tone_format": f"Translate the following text to {language_name}, maintaining the original meaning and structure. Ensure the translation is accurate, with natural and contextually appropriate expressions. Output only the translation.\n\nText: {text}",
        "formal_style": f"Translate the following text to {language_name}, maintaining a formal tone and structure. Ensure clarity and precision, especially with technical or formal terms. Output only the translation.\n\nText: {text}",
        "informal_style": f"Translate the following text to {language_name}, maintaining a conversational tone while preserving the structure. Output only the translation, and ensure it sounds natural and friendly.\n\nText: {text}",
        "accurate_meaning": f"Translate the following text to {language_name}, ensuring the translation is precise and that no information or nuance is lost. Output only the translation.\n\nText: {text}",
        "basic_enter": f"Translate the following text to {language_name}. Output only the translation without any line breaks or extra characters. Make sure the translation fits in one continuous line.\n\nText: {text}",
        "semantic_tone_format_enter": f"Translate the following text to {language_name}, maintaining the original meaning and structure, and ensuring no line breaks are included. The translation should be one continuous text without extra newlines or breaks.\n\nText: {text}",
        "formal_style_enter": f"Translate the following text to {language_name}, maintaining a formal tone, without inserting any newlines or breaks. The output should be continuous.\n\nText: {text}",
        "informal_style_enter": f"Translate the following text to {language_name}, keeping a casual tone and ensuring the translation is one continuous block of text with no newlines.\n\nText: {text}",
        "accurate_meaning_enter": f"Translate the following text to {language_name}, ensuring accuracy and no line breaks. The translation should be in one continuous paragraph without any newlines or breaks.\n\nText: {text}",
        "semantic_tone_format_accurate_meaning_enter": f"Translate the following text to {language_name}, maintaining the original meaning and structure, ensuring accuracy and no line breaks. The translation should be in one continuous paragraph without any newlines or breaks.\n\nText: {text}"
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

def translate_csv(input_csv, columns, target_lang, model, back_translate=True):
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
        new_col_name = f"{col}_{target_lang.upper()}"
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
    parser = argparse.ArgumentParser(description="Translate CSV column(s) using Llama 3.1 model from Ollama.")
    parser.add_argument("-i", "--input", type=str, default="input.csv", help="Input CSV file (default: input.csv)")
    parser.add_argument("-o", "--output", type=str, help="Output CSV file (default: input_filename_LANGCODE.csv)")
    parser.add_argument("-l", "--language", type=str, default="ES", help="Target language (default: ES for Spanish)")
    parser.add_argument("-m", "--model", type=str, default="llama3.2:latest", help="LLM model to use (default: llama3)")
    parser.add_argument("-c", "--columns", nargs="+", required=True, help="Column names to translate (space-separated)")

    args = parser.parse_args()
    translate_csv(args.input, args.columns, args.language, args.model)
