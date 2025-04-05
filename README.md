# csv_column_text_translator
A CSV text string column translator.

# CSV Translation Script

Richard Shipman - 15MAR2025

## Overview
This script translates specified columns in a CSV file into a target language using the Ollama API with a specified language model. It reads the CSV, translates the text in selected columns, and saves the translated output as a new CSV file.

## Features
- Supports translation of multiple columns in a CSV file.
- Uses Ollama API for translation.
- Supports multiple target languages.
- Outputs a new CSV file with translated columns appended with the language code.
- Logs translation time and token processing rate.

## Requirements
- Python 3.x
- Required Python libraries:
  - `argparse`
  - `pandas`
  - `ollama`
  - `time`
- Ollama API access configured and available.

## Installation
1. Install Python dependencies:

```bash
pip install pandas ollama
```
2. Ensure Ollama is properly configured and accessible.

## Usage
Run the script with the following command-line arguments:
```bash
python src/csv_column_translator.py -i data/input.csv -c column1 column2 -l ES -m llama3.2:latest
```

### Arguments
| Argument | Description |
|----------|-------------|
| `-i`, `--input` | Input CSV file (default: `test.csv`) |
| `-o`, `--output` | Output CSV file (default: `input_filename_LANGCODE.csv`) |
| `-l`, `--language` | Target language code (default: `ES` for Spanish) |
| `-m`, `--model` | Language model to use (default: `llama3.2:latest`) |
| `-c`, `--columns` | Column names to translate (space-separated, required) |

### Example
Translating the `description` and `comments` columns from `data.csv` to French:
```bash
python csv_column_translator.py -i data.csv -c description comments -l FR
```

## Output
- The script generates a new CSV file where each translated column is appended with the target language code.
- Example: If `data.csv` contains `description`, the translated file will have `description_FR`.

## Supported Languages
The script supports a wide range of languages using their respective language codes (e.g., `EN` for English, `ES` for Spanish, `ZH` for Chinese, etc.). See the script for the full list of supported language codes.

## Supported Languages

The following table lists the supported language codes and their corresponding language names.

| Language Code | Language Name          | Language Code | Language Name        |
|--------------|----------------------|--------------|--------------------|
| ZH           | Chinese              | EL           | Greek             |
| ES           | Spanish              | HE           | Hebrew            |
| CA           | Catalan/Valencian    | ID           | Indonesian        |
| EN           | English              | MS           | Malay             |
| HI           | Hindi                | KO           | Korean            |
| AR           | Arabic               | SW           | Swahili           |
| PT           | Portuguese           | FI           | Finnish           |
| BN           | Bengali              | CS           | Czech             |
| RU           | Russian              | DA           | Danish            |
| JA           | Japanese             | SV           | Swedish           |
| PA           | Punjabi              | SK           | Slovak            |
| DE           | German               | BG           | Bulgarian         |
| FR           | French               | HR           | Croatian          |
| VI           | Vietnamese           | SR           | Serbian           |
| MR           | Marathi              | SL           | Slovenian         |
| TA           | Tamil                | LT           | Lithuanian        |
| UR           | Urdu                 | LV           | Latvian           |
| TR           | Turkish              | ET           | Estonian          |
| IT           | Italian              | EU           | Basque            |
| FA           | Persian (Farsi)      | GL           | Galician          |
| PL           | Polish               | GA           | Irish             |
| UK           | Ukrainian            | CY           | Welsh             |
| RO           | Romanian             | MT           | Maltese           |
| NL           | Dutch                | IS           | Icelandic         |
| TH           | Thai                 | MK           | Macedonian        |
| HU           | Hungarian            | HY           | Armenian          |
| BE           | Belarusian           | SQ           | Albanian          |
| BS           | Bosnian              | LB           | Luxembourgish     |

## Notes
- Empty cells or missing values remain unchanged.
- The script logs translation time and token processing statistics for efficiency tracking.

## License

MIT License, open source. :) 

