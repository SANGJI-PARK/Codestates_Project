from twit_app import db

class Weather(db.Model):
    __tablename__ = 'weather'

    id = db.Column(db.Integer(), primary_key=True)
    weather = db.Column(db.String(64), nullable=False)
    wind = db.Column(db.Float())
    temp = db.Column(db.Float())

    def __repr__(self):
        return f"User {self.id}"


'''import csv

from flask import Blueprint, render_template
from mini_flask_app import CSV_FILEPATH

main_bp = Blueprint('main', __name__)


@main_bp.route('/',methods=['GET'])
def index():
    users = []

    with open(CSV_FILEPATH, 'r') as f:
      csv_reader = csv.DictReader(f)

      for row in csv_reader :
        users.append(row)

    return render_template('index.html',user_list=users) 
    # 렌더링을 하면 'template'폴더에 있는 html 문서에 데이터를 전달해준다.
'''