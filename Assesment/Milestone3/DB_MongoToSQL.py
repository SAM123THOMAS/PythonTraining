from pymongo import MongoClient
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

connection_string=r"mongodb+srv://samabraham555:yZOdvMvTlgQO4xMM@cluster0.y0piy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client=MongoClient(connection_string,tlsAllowInvalidCertificates=True)
    print("connected to mongo db success")
    #connect to mongo cluster
    db=client['sample_mflix']
    #access a collection
    collection=db["movies"]
    #query collection
    movie_details=collection.find()

    #Define the database
    DATABASE_URL = "sqlite:///movies.db"
    engine = create_engine(DATABASE_URL, echo = True)   
    Base = declarative_base()
    SessionLocal = sessionmaker(bind = engine)

    #define a  ORM Model movies
    class MovieClass(Base):
        __tablename__ = "movies"
        id = Column(String, primary_key = True)
        movie_name = Column(String, nullable = True)
        movie_plot = Column(String, nullable = True)
        movie_directors = Column(String, nullable = True)
        movie_languages=Column(String, nullable = True)
        released_date=Column(String, nullable = True)
        movie_genres= Column(String, nullable = True)

    #Create the database and tables
    Base.metadata.create_all(engine)
    #Create a new session
    session = SessionLocal()



     # Insert data into SQLite
    for movie in movie_details:
            # Extract data from MongoDB document
            movie_id = str(movie.get("_id", ""))
            plot=movie.get("plot","dummyplot")
            title = movie.get("title", "dummytitle")
            directors = ','.join(movie.get("directors", ["dummydirector"]))
            languages=','.join(movie.get("languages", ["Malayalam"]))
            released = movie.get("released", 2020)
            genres =','.join( movie.get("genres", ["Scifi"]))  

            #Create
            movie_data = MovieClass(id = movie_id, movie_name = title, movie_plot=plot, movie_directors=directors, movie_languages=languages, released_date=released, movie_genres=genres)
            session.add(movie_data)
    session.commit()

    #Read
    movies_read = session.query(MovieClass).all()
    for mov in movies_read:
        print(mov.id, mov.movie_name)

except Exception as e:
    print(e)

finally:
    client.close()
    session.close()
