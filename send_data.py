import requests

if __name__ == '__main__':
    
    url = 'http://localhost:5000/api/submit'

    print("\nWelcome to your simple Data Sender (send_data.py)\n")

    firstName = input("Enter Your First Name: ")
    lastName = input("Enter Your Last Name: ")
    email = input("Enter Your Email: ")
    phoneNumber = input("Enter Your Phone Number: ")
    supervisor = input("Enter Your Supervisor: ")

    info = {
        'firstName': firstName,
        'lastName': lastName,
        'email': email,
        'phoneNumber': phoneNumber,
        'supervisor': supervisor
    }

    resp = requests.post(url, json=info)

    if resp.status_code == 200:
        print('Congradulations! Your Request has been sent.')
    else:
        print('Error... Failed to submit data:', resp.text)