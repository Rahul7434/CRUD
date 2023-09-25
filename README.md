# CRUD

This  CRUD (Create, Read, Update, Delete) application I developed using Django, Based on (MVT) architecture Patern. This project allows users to perform various operations on user data, including adding, viewing, updating, and deleting user records. The application is designed with a user-friendly interface and incorporates essential features for managing user data efficiently.

## Features

* Models: In the project's models.py file, I defined a User model with attributes such as name, email, and password. This model represents the structure of the data stored in the database.

* Forms: I created a UserForm using Django's forms module to handle user input and data validation. The form includes fields for name, email, and password, and I added custom widgets to enhance the user interface.

* Views: The views.py file contains several functions to handle different aspects of the CRUD operations. Here are the main functions:

* add_show: This function handles the creation of new user records and displays the existing user data in a template. It utilizes the UserForm for data input and validation.

* delete_data: Allows users to delete a user record by clicking a delete button. It responds to POST requests and deletes the specified record.

* update_data: Enables users to edit and update existing user records. It fetches the user data, populates the UserForm for editing, and saves the changes.

* Admin Interface: I registered the User model in the admin.py file, which provides an admin interface for managing user data easily.

* Templates: The project includes HTML templates for rendering the user interface. These templates use the Django template engine to display data and forms.

* Static Files: I incorporated static files (CSS, JavaScript, etc.) to enhance the project's appearance and functionality.

* Database: The project uses a MySQL database to store user data. Database settings, including name, user, password, host, and port, are configured in the settings.py file.

* Technologies Used: Django, Python, MySQL, HTML, CSS

##  Project Stracture

- CRUD
    - crud
        - __init__.py
        - asgi.py
        - urls.py
        - wsgi.py
        - setting.py
    - app1
        - __init__.py
        - admin.py
        - apps.py
        - form.py
        - models.py
        - tests.py
        - views.py
    - static
        - app1
            - css
            - images
            - js
    - templates
        - app1
            - all templates files
    - manage.py
 
## Installation
1. Python Installation
   - Visit the official Website https://www.python.org/.
   - Click on the "Download" option.
   - Choose The Python Version
   - Select Operating System
   - Download the Installer
   - Run the Installer
   - Optional Modify The Path
   - Verify the installation
2. Django Installation
   - Open Command Promot or Terminal
   - Run the Commant ```pip install django```  For Specfic Version ```pip install django==4.2```
   - Verify the Installation ```python -m django --version```

   
      
