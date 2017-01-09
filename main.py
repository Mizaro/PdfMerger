import argparse
import os
from PyPDF2 import PdfFileMerger


def merger(pdfs, result_path):
    """
    get pdf paths and writes to another path the result
    @param pdfs: paths to pdf files.
    @type pdfs: C{list} of C{str}
    @param result_path: the path where to save the merged-pdf.
    @type result_path: C{str}
    """
    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(result_path)


def main(pdf_paths, result_path):
    merger(pdf_paths, result_path)


def parse_arguments():
    return [os.path.join("test", x) for x in os.listdir("test")], "result.pdf"

if __name__ == '__main__':
    main(*parse_arguments())