from flask import Flask
import os
from threading import Thread
from dotenv import load_dotenv

load_dotenv('./.env')

app = Flask('')

@app.route('/')
def index():
    return("Don't kill me please D:")

def run():
    app.run(host=os.getenv("HOST"),port=os.getenv("PORT"))

def staying_alive():
    t = Thread(target=run)
    t.start()
    