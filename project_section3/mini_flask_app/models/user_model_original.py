'''import os
import csv
import json

from flask import Blueprint, request
from mini_flask_app import CSV_FILEPATH, TMP_FILEPATH

user_bp = Blueprint('user', __name__)

# CSV 파일 경로와 임시 파일 경로입니다.
CSV_FILEPATH = os.path.join(os.getcwd(), 'mini_flask_app', 'users.csv')

def add_user(raw_user) :
    
    new_user = User(
        id = raw_user._json['id'],
        username = raw_user._json['screen_name'],
        full_name = raw_user._json['name'],
        followers = raw_user._json['followers_count']
     )

    # id는 primary key이기 떄문에 동일한 id가 있는 경우에는 진행하지 않도록 설정
    if User.query.filter(User.id == new_user.id).first() == None :
        db.session.add(new_user)
        db.session.commit()

def get_users():
    return User.query.all()

def delete_user(user_Id) :

    user = User.query.filter(User.id == user_Id).first()
    db.session.delete(user)
    db.sessiont.commit()

'''