
# CHATTER SPACE

## Overview
This is a simple social media web application built using Flask, a Python web framework. It allows users to register, log in, share posts,  and manage their profiles.

## Features
- User Registration: New users can create an account by providing a username and password.
- User Authentication: Registered users can log in using their username and password.
- Post Management: Users can create, edit, and delete their posts.
- Profile Editing: Users can edit their profile information, such as their bio and profile picture.
- Deployment: The application can be deployed to a web server for public access.

## Installation
1. Clone the repository: `git clone https://github.com/your-username/my-social-media-app.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up the database: 
    - Create a MySQL database and update the database configuration in `config.py`.
    - Run the following commands in the Python interpreter to create the database tables:
      ```python
      from app import db
      db.create_all()
      ```
4. Run the application: `python app.py`
5. Access the application in your web browser at `http://localhost:5000`

## Technologies Used
- Flask: Web framework for building the application.
- MySQL: Database management system for storing user and post data.
- HTML/CSS/Bootstrap: Frontend technologies for designing the user interface.
- JavaScript: Used for client-side interactions and form validation.

## Screenshots 
![Screenshot (222)](https://github.com/Shreenithi2003/Socialmedia-app/assets/143317948/7bd3805e-7a8b-480a-9b83-6633f628f0ec)
![Screenshot (223)](https://github.com/Shreenithi2003/Socialmedia-app/assets/143317948/0cc127a0-af33-4bad-a545-9244a6077b9c)
![Screenshot (224)](https://github.com/Shreenithi2003/Socialmedia-app/assets/143317948/64d810f4-a2c8-47de-beea-18a2dc82fcbf)
![Screenshot (225)](https://github.com/Shreenithi2003/Socialmedia-app/assets/143317948/4817cf1d-9261-44a8-a397-83876d7842f7)
![Screenshot (226)](https://github.com/Shreenithi2003/Socialmedia-app/assets/143317948/a7f47e27-f4fe-4226-b878-60f0b1b64954)
![Screenshot (227)](https://github.com/Shreenithi2003/Socialmedia-app/assets/143317948/497ba551-1af5-44c1-b551-d8597f1cfdfe)
![Screenshot (228)](https://github.com/Shreenithi2003/Socialmedia-app/assets/143317948/5f9b3bef-f4e5-4e91-bca3-eca15e29c6cc)


