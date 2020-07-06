"""This is the main module in the billparser application.

This module initializes the CLI to read the input arguments and parses the default XML files.
"""
import re
import xml.etree.ElementTree as ET
from zipfile import ZipFile

import config
from utils.cli import init_argparse
from utils.formatting import format_bill_id, format_bill_summary
from utils.xml import SRXMLElements


def sort_bills(found_bills) -> list:
    """Sort found Bills by their Bill Ids."""
    return sorted(found_bills.items(), key=lambda x: int(x[0].split(" ")[1]))


def parse_xml(found_bills, search_pattern) -> None:
    """Use provided regex pattern to match on zipped XML files.

    Keyword arguments:
    found_bills -- Dictionary to add matched Bills
    search_pattern -- Regex object that match on
    """
    with ZipFile(config.DEFAULT_ZIP, "r") as my_zip:
        for file_name in my_zip.namelist():
            with my_zip.open(file_name) as my_file:
                root = ET.fromstring(my_file.read().decode())
                for billSummary in root.iter(SRXMLElements.BillSummaries.value):
                    for text in billSummary.iter(SRXMLElements.Text.value):
                        summary_text = text.text
                        for match in search_pattern.finditer(summary_text):
                            found_bills[format_bill_id(root)] = format_bill_summary(
                                summary_text, match
                            )


def main() -> None:
    """Main function that initializes the CLI and read inputs to print any matched Bill Ids"""
    parser = init_argparse()
    args = parser.parse_args()
    search_pattern = re.compile(args.Search)
    found_bills = {}
    parse_xml(found_bills, search_pattern)
    if not found_bills:
        print("Did not find any bills")
    else:
        print("Found the following bill(s):")
        if args.text:
            for bill_id, bill_summary in sort_bills(found_bills):
                print(f"{bill_id}: {bill_summary}")
        else:
            for bill_id, bill_summary in sort_bills(found_bills):
                print(bill_id)


if __name__ == "__main__":
    main()
