import os

from utils.xml import SRXMLElements


class Format:
    """A simple class for formatting python strings."""

    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def format_bill_id(root) -> str:
    """Return the formatted bill_id for a given bill xml root."""
    return (
        f"""{root.findall(os.path.join(".",SRXMLElements.Bill.value, SRXMLElements.BillType.value))[0].text} """
        f"""{root.findall(os.path.join(".",SRXMLElements.Bill.value, SRXMLElements.BillNumber.value))[0].text}"""
    )


def format_bill_summary(summary_text, match) -> str:
    """Return the formatted bill summary text for a given bill summary text and match object."""
    return (
        summary_text.replace("<p>", "")
        .replace("</p>", "")
        .replace(match[0], f"{Format.BOLD}{match[0]}{Format.END}")
    )
