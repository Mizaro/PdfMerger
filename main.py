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
    parser = argparse.ArgumentParser(description='Process some integers.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', "--folder", dest="pdfs_folder", type=str,
                    help='folder of pdf files, sorted')
    group.add_argument('-s', "--pdfs", type=str, nargs="+",
                    help='folder of pdf files, sorted')
    parser.add_argument('result_file', type=str,
                    help='path to result of merge')
    args = parser.parse_args()

    def dir_dir(name):
        return [os.path.join(name, x) for x in os.listdir(name)]

    pdfs = []
    if args.pdfs_folder is not None:
        pdfs_folder = os.path.abspath(args.pdfs_folder)
        if not os.path.isdir(pdfs_folder):
            raise Exception("folder must be a folder")
        else:
            pdfs = dir_dir(pdfs_folder)
    else:
        pdfs = [os.path.abspath(x) for x in args.pdfs]
    if not any(pdfs):
        raise Exception("None pdf files have been found.")
    return pdfs, args.result_file

if __name__ == '__main__':
    main(*parse_arguments())