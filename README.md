# Vendor_mangement_system
Vendor Management System with Performance Metrics
INITIAL SETUP

Clone the repository:
git clone https://github.com/codejahirx/Vendor-management-system.git

Navigate to the project directory:
cd Vendor_Management_system

Activate virtualenv
venv\scripts\activate


Install dependencies:
pip install -r requirements.txt


Apply database migrations:
python manage.py migrate


Run the development server using following command:
python manage.py runserver

----------------------------------------------
Setup instructions and details on using the API endpoints:

I have used Postman for API testing and demonstrated the functionality and reliability of the endpoints.

Follow the url below and click on 'Run in Postman' which is in the top right side corner to open Postman


API test suite - https://documenter.getpostman.com/view/31500665/2s9YeLZpj5




Retrieve Vendor Performance:

URL: /vendors/<int:pk>/performance/
Method: GET (Retrieve Vendor Performance)
Authentication: Token Authentication required
