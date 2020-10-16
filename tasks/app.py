"""Entry point for the web app."""
import os

from flask import Flask, render_template, request, escape, abort

app = Flask(__name__, template_folder='public')


@app.route('/')
def index():
    """Serve the frontend."""
    return render_template('index.html')


@app.route('/submitPatientData', methods=['POST'])
def submit_patient_data():
    """Handle the patient data passed from the form."""
    response = {
        'metabolites': []
    }
    for i, metabolite in enumerate(request.form.getlist('metaboliteName')):
        try:
            response['metabolites'].append(
                {
                    'name': str(escape(metabolite)),
                    'value': int(escape(
                        # Get the value of the corresponding metabolite.
                        request.form.getlist('metaboliteValue')[i]
                    ))
                }
            )
        except KeyError:
            return abort(400, f'Missing a required value for {metabolite}')
    return f'Success!\nData serialized to: {response}'


if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port=8000,
            debug=os.getenv('DEBUG', False))
