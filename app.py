from flask import Flask, jsonify, render_template, request, redirect, url_for
from pydantic import MongoDsn
from pymongo import MongoClient


app = Flask(__name__)




client = MongoClient("mongodb+srv://71762132045:bob123@cluster0.w0k2rr9.mongodb.net/your_database_name?retryWrites=true&appName=Cluster0&ssl=true&tls=true")
db = client.get_database("BOB") 



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile_page():
    return render_template('profile.html')

@app.route('/login',methods=['GET','POST'])
def login_page():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']

        user_data = {
            'username': username,
            'password': password
        }
        db.users.insert_one(user_data) 
        return redirect(url_for('profile_page'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        date_of_birth = request.form['date_of_birth']
        country = request.form['country']
       
        user_data = {
            'username': username,
            'email': email,
            'password': password,
            'date_of_birth': date_of_birth,
            'country': country
            
        }
        db.users.insert_one(user_data)  

      
        return redirect(url_for('profile_page'))

    return render_template('user_registration.html')

from flask import render_template, request

@app.route('/search_users', methods=['GET', 'POST'])
def search_users_page():
        return render_template('user_search.html')


class Post:
    def __init__(self, content, image_path):
        self.content = content
        self.image_path = image_path

@app.route('/add_post', methods=['GET', 'POST'])
def add_post_page():
    if request.method == 'POST':
        post_content = request.form.get('content')

        return redirect(url_for('profile_page'))
    
    return render_template('add_post.html')

@app.route('/get_posts')
def get_posts():
   
    posts = Post.query.all()

    posts_data = []
    for post in posts:
        post_data = {
            'id': post.id,
            'content': post.content,
            'image': post.image_url if post.image_url else None
        }
        posts_data.append(post_data)

  
    return jsonify(posts_data)

if __name__ == '__main__':
    app.run(debug=True)