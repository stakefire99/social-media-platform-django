# 📘 SocialApp — Django Social Media Platform

A fully-featured social media platform built with Django as part of a Python web development course.

## 🚀 Features
- User Registration & Login & Logout
- User Profiles with bio, profile picture, location
- Create, view and delete Posts with image uploads
- Like and Comment on posts
- Friend Request system (send & accept)
- Auto Notifications for likes, comments, friend requests
- Notification badge on navbar
- Search for users by username
- Responsive UI with Bootstrap 5
- Django Admin Panel for managing all data

## 🛠️ Tech Stack
- Python 3.12
- Django 6.0
- SQLite
- Bootstrap 5
- Pillow
- Django REST Framework
- Django Crispy Forms

## ⚙️ Setup Instructions

1. Clone the repository
git clone https://github.com/YOUR_USERNAME/social-media-platform-django.git
cd social-media-platform-django

2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py migrate

5. Create admin account
python manage.py createsuperuser

6. Start the server
python manage.py runserver

7. Open in browser
http://127.0.0.1:8000/

## 📁 Project Structure
social_platform/
├── manage.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── users/
│   │   ├── register.html
│   │   ├── login.html
│   │   ├── profile.html
│   │   ├── edit_profile.html
│   │   └── search.html
│   ├── posts/
│   │   └── home.html
│   ├── friends/
│   │   └── friend_list.html
│   └── notifications/
│       └── notifications.html
├── users/
├── posts/
├── friends/
├── notifications/
└── social_platform/

## 🗄️ Database Models
- UserProfile — extends Django User with bio, picture, location
- Post — content, image, likes, timestamps
- Comment — linked to posts and users
- FriendRequest — tracks pending and accepted friendships
- Notification — likes, comments, friend request alerts

## 🔑 Admin Panel
http://127.0.0.1:8000/admin/

Manage users, posts, comments, friend requests and notifications.

## 🧪 How to Test
1. Register two accounts
2. Login as user1 and create a post
3. Login as user2 and like/comment on the post
4. Check notifications as user1
5. Send and accept a friend request
6. Use the search bar to find users

## 👩‍💻 Author
Lakshita
Built as part of Month 2 — Web Development with Django
