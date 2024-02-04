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


def get_type(data):
    if data== 3:
        return "level 3"

    
    elif data== 1:
        return "level 1"


    elif data==2:
        return "level 2"


    elif data== 4:
        return "level 4"


    if data== 5:
        return "level 5"
    else:
        return "Not bullied"



def encourage(label):

    print("label is:", label[-1])

    if label=="level 3":
        return "You are valued and loved for who you are, and your religious beliefs are a fundamental part of your identity."

        
    elif label=="level 1":
        return "Age is just a number. You have a lot to offer, and your uniqueness is something to be celebrated."


    elif label=="level 2":
        return "You have the right to express your true gender identity without fear or discrimination. It's important to stand up for who you are."


    elif label=="level 4":
        return "This difficult time will pass, and you will emerge even stronger."


    if label=="level 5":
        return "Embrace your cultural heritage with pride. Your ethnicity is a source of strength and richness, you are not alone in this!"
    else:
        return "Don't be a bully!" 

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(val):
 
#    val=input("Enter the comment: ")

    val=mod.rem_punc(val)
    val=mod.remove_stopwords(val)
    val=mod.lemmatize_text(val)
    val=tfidf_vectorizer.transform([val])

    type=get_type(classifier.predict(val)[0])
    return get_type(classifier.predict(val)[0]), encourage(type)

# print(" Verdict: \n",get_type(clf.predict(val)[0]))
    # prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    # print(prediction)
    # return prediction



def main():
    st.title("Cyber Bullying Detection")
    html_temp = """
    <div style="background-color:tomato;padding:10px; border-radius:10px">
    <h2 style="color:white;text-align:center"> Cyber Bullying Detection ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    val = st.text_input("text","Type Here")
    
    result=""
    tup=("hi","hello")
    if st.button("Predict"):
        result=predict_note_authentication(val)
    if type(result)==type(tup):
        if result[0]=="level 3" or result[0]=="level 5":

            subject= "The user discrimination on social media on the basis of Race, Religion or Ethenicity with a severity level of "+ str(result[0])
            st.success('You are rated at {}'.format(result[0]))
            st.success(result[-1])
            st.text("This is a critical comment on your Race, Religion or Ethenicity. ")
            st.header("The :red[Cybercrime Branch] has been texted and mailed with your situtation")
            # send_text()

            send_email("Discrimination based on Race, Religion or Ethenicity", subject)
        # print(result)

        else:
            st.success('You are rated at {}'.format(result[0]))
            st.success(result[-1])

    else:
        st.success('You are rated at {}'.format(result))

        
    if st.button("About"):
        st.markdown("Made with :heartbeat: ")
        st.markdown("**Ruchika Bihari** | **Aditya** ")

        

if __name__=='__main__':
    main()





