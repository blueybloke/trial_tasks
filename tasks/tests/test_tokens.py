"""Test the xml file is parsed correctly."""
import unittest

from ..task_one.parse_xml import parse_tokens


class TestTokens(unittest.TestCase):
    """Test that the tokens are parsed correctly."""

    def test_parse_tokens(self):
        """Test method for parse_tokens"""
        self.maxDiff = None
        """Test parsed XML file example.xml."""
        # Set the expected output to a list of metabolites.
        # Each dict represents a metabolite.
        expected_output: list = [
            {
                'name': 'D-GLUCOSE',
                'creation_date': '2005-11-16 15:48:42 UTC',
                'update_date': '2020-08-10 16:51:26 UTC',
                'accession': 'HMDB0000122',
                'normal_concentrations': [
                    {
                        'biospecimen': 'BLOOD',
                        'concentration_value': '3100-5600',
                        'concentration_units': 'UM',
                        'subject_age': 'NOT SPECIFIED',
                        'subject_sex': 'NOT SPECIFIED',
                        'subject_condition': 'NORMAL',
                        'references': ['10832746']
                    },
                    {
                        'biospecimen': 'BLOOD',
                        'concentration_value': '3890-5550',
                        'concentration_units': 'UM',
                        'subject_age': 'NOT SPECIFIED',
                        'subject_sex': 'NOT SPECIFIED',
                        'subject_condition': 'NORMAL',
                        'references': ['29030856']
                    }
                ]
            }
        ]
        actual_output = parse_tokens('tasks/tests/example.xml')
        self.assertListEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
