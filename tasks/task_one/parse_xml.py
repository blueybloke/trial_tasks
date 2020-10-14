"""Parses a given XML file to return a list of metabolite tokens."""
import xml.etree.ElementTree as ET


def parse_xml(xml_path: str):
    """Parse a given XML file to get the metabolite data."""
    result: list = []

    # Load the XML file.
    xml = ET.parse(xml_path)
    root = xml.getroot()

    for metabolite in root:
        result.append({
            'name': metabolite.findtext('name')
        })
    return result

