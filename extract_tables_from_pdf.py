import sys
import os
import tabula
import pandas as pd

def extract_tables_from_pdf(pdf_file):
    # Read tables from the PDF file
    tables = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True)

    # Save each table as a CSV file
    for i, table in enumerate(tables):
        csv_file = f"{os.path.splitext(pdf_file)[0]}_table_{i+1}.csv"
        table.to_csv(csv_file, index=False)
        print(f"Saved table {i+1} to {csv_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_tables_from_pdf.py [PDF_FILE]")
        sys.exit(1)

    pdf_file = sys.argv[1]
    if not os.path.exists(pdf_file):
        print(f"File '{pdf_file}' not found.")
        sys.exit(1)

    extract_tables_from_pdf(pdf_file)
