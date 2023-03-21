# PDF Table Extractor

This Python script extracts tables from a PDF file and saves them as separate CSV files using the `tabula-py` and `pandas` libraries.

## Requirements

- Python 3.6 or higher
- Java Runtime Environment (JRE) or Java Development Kit (JDK) 8 or higher

## Installation

1. Install the required Python libraries:

<pre>
pip install tabula-py pandas
</pre>


2. Install Java, if not already installed, by following the instructions at https://www.java.com/en/download/

## Usage

Run the script with the desired PDF file as an argument:

<pre>
python3 extract_tables_from_pdf.py your_pdf_file.pdf
</pre>


The script will extract all tables from the input PDF file and save them as separate CSV files, named with the format `<pdf_file_name>_table_<table_number>.csv`.

## Troubleshooting

If you encounter issues related to Java, please ensure that the `JAVA_HOME` environment variable is set correctly. 

## License

This project is licensed under the MIT License.

