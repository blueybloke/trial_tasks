"""Parses a given XML file to return a dictionary of tokens."""
import xml.etree.ElementTree as ET


def parse_xml(xml_path: str):
    """Parse a given XML file to get the metabolite data."""
    xml = ET.parse(xml_path)
    root = xml.getroot()


