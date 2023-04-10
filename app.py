import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model

Lrdetect_File = open('Language Detection/model.pckl', 'rb')
Lrdetect_Model = pickle.load(Lrdetect_File)
Lrdetect_File.close()
st.title("Language Detection Tool")
input_test = st.text_input("Provide your text input here," ' Eg: Hello my name is Supratim Paul')

button_clicked = st.button("Get Language Name")
if button_clicked:
    st.text(Lrdetect_Model.predict([input_test]))

# streamlit run "C:\series\NLP tut\Language Detection\app.py"