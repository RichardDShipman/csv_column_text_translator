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
python csv_column_translator.py -i input.csv -c column1 column2 -l ES -m llama3.2:latest
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

# Tests and Validation

column1,column2
Gene,A gene is a sequence of DNA that contains the instructions for making a specific protein or RNA molecule. Genes are the basic units of heredity and are responsible for determining the traits of an organism.
Cell,"The cell is the fundamental structural and functional unit of life. All living organisms are made up of cells, which can be unicellular (single-celled organisms) or multicellular (such as plants and animals)."
Protein,"Proteins are large, complex molecules made up of amino acids. They perform a vast array of functions within organisms, including catalyzing reactions (enzymes), providing structure to cells, and regulating biological processes."
DNA,"DNA (deoxyribonucleic acid) is a molecule that carries the genetic instructions used in the growth, development, and functioning of all living organisms. It consists of two strands that coil around each other to form a double helix."
RNA,"RNA (ribonucleic acid) is a molecule similar to DNA but typically single-stranded. RNA plays a key role in translating the genetic information from DNA into proteins, with types such as mRNA, tRNA, and rRNA."
Mitochondria,"Mitochondria are organelles found in eukaryotic cells that are responsible for producing energy in the form of ATP. Often called the 'powerhouses' of the cell, mitochondria also play a role in regulating the cell cycle and cell growth."
Enzyme,"Enzymes are biological catalysts that speed up chemical reactions in living organisms. They are typically proteins that lower the activation energy of a reaction, allowing it to proceed more quickly and efficiently."
Chromosome,"A chromosome is a long, thread-like structure made of DNA and proteins. It carries the genetic information of an organism, and humans have 23 pairs of chromosomes in their cells."
Lipid,"Lipids are a diverse group of hydrophobic or amphipathic molecules that include fats, oils, phospholipids, and sterols. They serve as energy storage, structural components of cell membranes, and signaling molecules, and are essential for maintaining cell integrity and function."
Glycan,"A glycan is a carbohydrate or saccharide, typically a polymer of sugar molecules, that can be attached to proteins or lipids in the form of glycosylation. Glycans are involved in a variety of biological processes, including cell-cell communication, immune response, and protein folding."
Mutation,"A mutation is a change in the DNA sequence that may lead to a change in the protein encoded by a gene. Mutations can be caused by environmental factors or occur spontaneously, and they can result in genetic diversity or disease."
Cloning,"Cloning is the process of creating genetically identical organisms or cells. In molecular biology, this often refers to creating copies of a specific gene, organism, or cell for research or therapeutic purposes."
Antibody,"Antibodies are proteins produced by the immune system that recognize and bind to specific antigens. They play a critical role in defending the body against pathogens like bacteria and viruses."
Bacterium,"A bacterium is a type of single-celled microorganism that lacks a nucleus. Bacteria are found in various environments and can have both beneficial and harmful effects on humans, plants, and animals."
Virus,"A virus is a microscopic infectious agent that requires a host cell to replicate. Viruses are composed of genetic material (either DNA or RNA) surrounded by a protein coat, and they can cause diseases in animals, plants, and bacteria."
Amino acid,"Amino acids are the building blocks of proteins. There are 20 standard amino acids that combine in different sequences to form proteins, and they are essential for the structure and function of biological organisms."
Metabolism,"Metabolism refers to the set of life-sustaining chemical reactions in organisms that enable them to convert food into energy, build cellular structures, and regulate vital processes. It consists of catabolic (breaking down molecules) and anabolic (building molecules) pathways."
Transcription,"Transcription is the process by which an RNA molecule is synthesized from a DNA template. It is the first step in gene expression, where messenger RNA (mRNA) is produced to carry genetic instructions from the DNA to the ribosomes."
Translation,Translation is the process by which a ribosome decodes the messenger RNA (mRNA) to synthesize proteins. It involves reading the mRNA codons and assembling the corresponding amino acids to form a polypeptide chain.
Eukaryote,"Eukaryotes are organisms whose cells contain a nucleus and other membrane-bound organelles. Eukaryotes include animals, plants, fungi, and protists, and they are distinguished from prokaryotes, which lack a nucleus."
Prokaryote,"Prokaryotes are single-celled organisms that lack a nucleus and membrane-bound organelles. Bacteria and archaea are examples of prokaryotes, and they are typically smaller and simpler than eukaryotic cells."
Phosphorylation,"Phosphorylation is the addition of a phosphate group to a protein or other molecule. This process plays a critical role in regulating cellular activities, including signaling pathways and enzyme activity."
Glycosylation,"Glycosylation is the process by which a carbohydrate (glycan) is covalently attached to a protein or lipid. This post-translational modification plays a critical role in protein folding, stability, and function, as well as in cellular signaling, immune response, and protein trafficking."
Apoptosis,"Apoptosis is a form of programmed cell death that is essential for maintaining the health of an organism. It allows the body to remove damaged or unnecessary cells in a controlled and regulated manner."
Biosynthesis,"Biosynthesis is the process by which living organisms produce complex molecules, such as proteins, nucleic acids, and lipids, from simpler precursor molecules. This process is crucial for cell growth, maintenance, and repair."
Endoplasmic Reticulum,"The endoplasmic reticulum (ER) is a membrane-bound organelle in eukaryotic cells involved in the synthesis of proteins and lipids. The rough ER is studded with ribosomes and synthesizes proteins, while the smooth ER is involved in lipid synthesis and detoxification."
