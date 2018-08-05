from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import csv
import os

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")


# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

with open('zips.csv') as csvFile:
    readCSV = csv.reader(csvFile)
    for zipcode, city, state, lat, long, population in readCSV:
        print(zipcode, city, state, lat, long, population)
        db.execute("""insert into "Locations" 
                    (zipcode, 
                    city, 
                    state, 
                    lat, 
                    long, 
                    population) 
                    values 
                   (:zipcode, 
                   :city, 
                   :state, 
                   :lat, 
                   :long, 
                   :population)""",
                   {"zipcode": zipcode,
                    "city": city,
                    "state": state,
                    "lat": lat,
                    "long": long,
                    "population": population})
    db.commit()

