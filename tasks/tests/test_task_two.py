"""Task Two Test: Test the route for task two's backend."""
import unittest

from werkzeug.datastructures import ImmutableMultiDict, MultiDict

from ..app import app


class TestTaskTwo(unittest.TestCase):
    """Test that the backend handles the form data from the frontend."""

    def setUp(self) -> None:
        """Set up the test."""
        self.tester = app.test_client(self)
        self.mock_data = MultiDict([
            ('metaboliteName', 'iron'),
            ('metaboliteValue', '34'),
            ('metaboliteName', 'potassium'),
            ('metaboliteValue', '99'),
            ('metaboliteName', 'glubin'),
            ('metaboliteValue', '44'),
        ])

    def test_submit_patient_data(self):
        """Test route for patient data form submit."""
        response = self.tester.post(
            '/submitPatientData',
            content_type='application/x-www-form-urlencoded',
            data=ImmutableMultiDict(self.mock_data)
        )
        self.assertEqual(response.status_code, 200)
