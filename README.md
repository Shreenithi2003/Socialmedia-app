
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
![Screenshot (222)](https://github.com/Shreenithi2003/Socialmedia-app/assets/143317948/dd9881b2-2f6c-4b85-b1dd-ba56192de509)
![Screenshot (223)](https://github.com/Shreenithi2003/Socialmedia-app/assets/143317948/76154686-ec70-40a6-bf50-297f1be8d742)
![Screenshot (224)](https://github.com/Shreenithi2003/Socialmedia-app/assets/143317948/b98549eb-79ab-4cdd-9815-d667507e7403)
![Screenshot (225)](https://github.com/Shreenithi2003/Socialmedia-app/assets/143317948/e83970fd-f984-414b-9b0b-708ea5a6853c)
![Screenshot (226)](https://github.com/Shreenithi2003/Socialmedia-app/assets/143317948/0a462da5-1165-473e-bade-9645c4958bdb)
![Screenshot (227)](https://github.com/Shreenithi2003/Socialmedia-app/assets/143317948/843679cc-0830-465e-8a9d-6aaee7e244b2)
![Screenshot (228)](https://github.com/Shreenithi2003/Socialmedia-app/assets/143317948/f2bf3b46-607c-49c4-979d-4f962545f7f1)


