# Vendor_mangement_system
Vendor Management System with Performance Metrics
INITIAL SETUP

Open VSCode

Open terminal
if django not installed

type pip install django in terminal

Clone the repository:
git clonehttps://github.com/Abhicodes4/Vendor_mangement_system.git

Navigate to the project directory:
cd Vendor_Management_system

Make a virtual environment
python -m venv venv

Activate virtualenv
venv\scripts\activate


Install dependencies:
pip install -r requirements.txt

Apply database migrations:
python manage.py migrate

python manage.py make migrations


Run the development server using following command:
python manage.py runserver





Retrieve Vendor Performance:

URL: /vendors/<int:pk>/performance/
Method: GET (Retrieve Vendor Performance)
Authentication: Token Authentication required
