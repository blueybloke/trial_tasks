"""Task One: Parses a given XML file to return a list of metabolite tokens."""
import xml.etree.ElementTree as ET


def parse_tokens(xml_path: str):
    """Parse a given XML file to get the metabolite data."""
    result: list = []

    # Load the XML file.
    xml = ET.parse(xml_path)

    for metabolite in xml.getroot():
        # Generate normal_concentrations.
        normal_concentrations = []
        for con in metabolite.find('normal_concentrations'):
            normal_concentrations.append({
                'biospecimen':
                    con.findtext('biospecimen').upper(),
                'concentration_value':
                    con.findtext('concentration_value').upper(),
                'concentration_units':
                    con.findtext('concentration_units').upper(),
                'subject_age':
                    con.findtext('subject_age').upper(),
                'subject_sex':
                    con.findtext('subject_sex').upper(),
                'subject_condition':
                    con.findtext('subject_condition').upper(),
                'references': [
                    ref.findtext('pubmed_id') for ref in con.find('references')
                    ]
            })

        result.append({
            'name':
                metabolite.findtext('name').upper(),
            'creation_date':
                metabolite.findtext('creation_date').upper(),
            'update_date':
                metabolite.findtext('update_date').upper(),
            'accession':
                metabolite.findtext('accession').upper(),
            'normal_concentrations':
                normal_concentrations


        })
    return result
