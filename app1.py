import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open(
    'diabetes_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:

    selected = option_menu('Here you can predict your diabetes',

                           ['Diabetes Prediction'],
                           icons=['activity'],
                           default_index=0)


# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input(
            'Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

    
    
page_bg_img = """

<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
background-size: cover;
}

[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0)
}

[data-testid="stSidebar"]{
    background-image: url("https://images.pexels.com/photos/837258/pexels-photo-837258.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
    background-size: cover;
}
<style/>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.sidebar.header(" ")

