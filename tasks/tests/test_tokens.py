"""Test the xml file is parsed correctly."""
import unittest

from ..task_one.parse_xml import parse_xml


class TestTokens(unittest.TestCase):
    """Test that the tokens are parsed correctly."""

    def test_xml_parser(self):
        """Test parsed XML file example.xml."""
        # Set the expected output to a list of metabolites.
        # Each dict represents a metabolite.
        expected_output: list = [
            {
                'name': 'D-Glucose',
                'creation_date': '2005-11-16 15:48:42 UTC',
                'update_date': '2020-08-10 16:51:26 UTC',
                'accession': 'HMDB0000122',
                'normal_concentrations': [
                    {
                        'biospecimen': 'blood',
                        'concentration_value': '3100-5600',
                        'concentration_units': 'um',
                        'subject_age': None,
                        'subject_sex': None,
                        'subject_condition': 'normal',
                        'references': [10832746]
                    },
                    {
                        'biospecimen': 'blood',
                        'concentration_value': '3890-5550',
                        'concentration_units': 'um',
                        'subject_age': None,
                        'subject_sex': None,
                        'subject_condition': 'normal',
                        'references': [29030856]
                    }
                ]
            }
        ]
        actual_output = parse_xml('tasks/tests/example.xml')
        print(actual_output)
        self.assertListEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
