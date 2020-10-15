"""Task Two: Backend for given frontend."""
from ..app import app


@app.route('/submitPatientData', methods=['POST'])
def submit_patient_data():
    """Handle the patient data passed from the form."""
    # TODO: Parse the patient data.
    # TODO: Santize the patient data.
    # TODO: Store the patient data to PostgreSQL with SQLAlchemy.
    pass
