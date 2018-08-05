import os
import json

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/api/<int: zipcode>")
def return_user_zipcode_info(zipcode):
    zipcode_info = db.execute("""SELECT * from "Locations" where zipcode = """ . zipcpde)

    for info in zipcode_info:
        json_data = {"place_name": info.city,
                     "state": info.state,
                     "latitude": info.lat,
                     "longitude": info.long,
                     "population": info.population,
                     "zip": info.zipcode}
    encoded_json = json.JSONEncoder(json_data)
    json.dump(json_data, indent=2)



