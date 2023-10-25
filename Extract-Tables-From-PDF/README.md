# Extracting Table Data From PDF

While it's mostly possible to get data in `spreadsheet`, `text`, and `JSON` format, Sometimes you may find the data you need is part of a paper or a pdf document

One is usually left with few options of getting the data from those `PDF` tables either copying and pasting which doesn't work well always, or manually typing them

With `tabula`, you can customize to extract data from any region of a page in a pdf

It returns a list of `DataFrame`, that you can perform further cleaning, to get the data that you expected

In this repo, is a customized program, that you can extract the data from the tables

You can execute the program by running the following from the CLI

## Table that have ruling line

```bash

python extract_tables.py --pdf_path  'PDF-Files/foo.pdf' --page_number '1'

```
## Table with no ruling line

```bash
python extract_tables.py --pdf_path  'PDF-Files/campaign_donors.pdf' --page_number 'all' --stream True
```

where, `--pdf_path` is the path for the pdf file, `--page_number` is a string that contains the page number you are extracting the data from; you can pass `all` for all pages, or even a sequence like `'1-3, 5'` for pages 1 to 3, and page 5
`--stream` by default is False, pass True if the table doesn't have the ruling lines



