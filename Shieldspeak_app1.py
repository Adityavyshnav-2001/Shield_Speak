import numpy as np
import pickle
import pandas as pd
import re
#from flasgger import Swagger
import streamlit as st 
import modules as mod
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer
# from twilio.rest import Client

import smtplib
import ssl
from email.message import EmailMessage
import configparser

tfidf_vectorizer = TfidfVectorizer()

app=Flask(__name__)
Swagger(app)


pickle_in = open("F:/SOP/codeathon1.pkl","rb")
classifier=pickle.load(pickle_in)


tfidf_vectorizer=pickle.load(open("F:/SOP/tfidf_vectorizer.pickle", 'rb'))

@app.route('/')
def welcome():
    return "Welcome All"



def send_email(subject, body):

    print("sending email")

    email_sender = "semthreecs@gmail.com"
    email_password = "bfqt hoec iapq bbnk"
    email_receiver = "codeadityavyshnav@gmail.com"

    em = EmailMessage()
    em.set_content(body)
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)
        print("sent mail")





