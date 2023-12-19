from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["SECRET_KEY"] = "4c5dde258a8141d485b40dfb47cbe992adeee89f"
app.config["MONGO_URI"] = "mongodb+srv://wael22ka:1DNHoHrqeuzZ71Na@cluster0.gaad0pv.mongodb.net/LogIn_Reg?retryWrites=true&w=majority"

try:
    mongodb_client = PyMongo(app)
    db = mongodb_client.db

    if db is None:
        print("Error: Could not connect to the database.")
    else:
        print("Connected to the database successfully.")
except Exception as e:
    print(f"Error: {e}")


from application import routes
