from flask import Flask
from flask import request
from flask import jsonify
import requests

app = Flask(__name__)

@app.route('/')
def welcome():
    return jsonify('Welcome. This statement confirms you can reach the flask server.')

@app.route('/error')
def error():
    return jsonify('Error 404. No route found.')

@app.route('/api/submit', methods=['POST'])
def submitData():
    data = request.json

    if 'firstName' not in data or 'lastName' not in data or 'supervisor' not in data:
        return jsonify({'error': 'firstName, lastName, and supervisor are required parameters'}), 400

    print('Alert: New Information Submitted!')
    print('First Name:', data.get('firstName'))
    print('Last Name:', data.get('lastName'))
    print('Email:', data.get('email', 'Not provided'))
    print('Phone Number:', data.get('phoneNumber', 'Not provided'))
    print('Supervisor:', data.get('supervisor'))
    return '', 200

@app.route('/api/supervisors', methods=['GET'])
def getSupervisors():
    try:
        managers = requests.get('https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers').json()
        supervisors = [
            f"{manager['jurisdiction']} - {manager['lastName']}, {manager['firstName']}"
            for manager in managers
            if not str(manager['jurisdiction']).isdigit()
        ]
        supervisors.sort()
        return jsonify({'supervisors': supervisors})
    
    except Exception as e:
        print('There has been an error while fetching supervisors:', e)
        return jsonify({'error': 'Internal Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)