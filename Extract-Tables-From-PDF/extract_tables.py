import tabula
import argparse
import logging
import csv


def extract_tables(pdf_path='foo.pdf', page_number='1', stream=False):
    try:
        # Read the PDF and extract tables from the specified page
        dfs = tabula.read_pdf(pdf_path, pages=page_number, stream=stream)

        # any tables extracted
        if dfs is not None and len(dfs) > 0:
            return dfs
        else:
            return None
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    # Provide the PDF file path and page number as arguments
    import sys

    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.INFO)
    logging.info("Extracting Tables!\n")

    parser = argparse.ArgumentParser(description="Table Extraction from PDF")
    parser.add_argument('--pdf_path', required=True, type=str, help="PDF Filename")
    parser.add_argument('--page_number', required=True, type=str, help='Page number(s) to extract tables from')
    parser.add_argument('--stream', type=bool, help="If the tables have no ruling lines, set stream=True")
    args = parser.parse_args()

    try:
        file_name = args.pdf_path.split('.')[0].split('/')[-1]
        # print(file_name)
        if 'pdf' not in args.pdf_path.split('.')[-1]:
            logging.critical(f"Invalid file format [{args.source}], Provide a file with a .pdf extension")
            sys.exit()

        extracted_tables = extract_tables(args.pdf_path, args.page_number, args.stream)

        if extracted_tables is not None:
            for i, df in enumerate(extracted_tables):
                df.to_csv(f"Extracted-Data/{file_name}_table_{i + 1}.csv", index=False)
                print(f"Table {i + 1} extracted and saved as {file_name}_table_{i + 1}.csv")
        else:
            print("No tables were found in the PDF.")

    except Exception as e:
        logging.error(f"This error occurred while processing pdf! : {str(e)}")