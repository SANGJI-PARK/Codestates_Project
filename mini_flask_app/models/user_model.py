from mini_flask_app import db
import requests
import json

API_KEY = '999579ae24c9a2798ddc5f0cef792ce5'
Base = declarative_base()

    
class City(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer(), primary_key=True)
    cityname = db.Column(db.String(64), nullable=False)
    country = db.Column(db.String(64), nullable=False)
    weathers = db.relationship('Weather', backref='city',cascade = "all,delete")

    def __repr__(self):
        return f"User {self.id}"

def add_city(raw_city) :
    API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={raw_city}&appid={API_KEY}'
    
    resp = requests.get(API_URL)
    json_resp = json.loads(resp.text)

    new_city = City(
        id = json_resp['id'],
        cityname = json_resp['name'],
        country = json_resp['sys']['country']
     )

    # id는 primary key이기 떄문에 동일한 id가 있는 경우에는 진행하지 않도록 설정
    if City.query.filter(City.id == new_city.id).first() == None :
        db.session.add(new_city)
        db.session.commit()

def get_city():
    return City.query.all()

def delete_city(city_name) :

    city = City.query.filter(City.cityname == city_name).first()
    db.session.delete(city)
    db.sessiont.commit()