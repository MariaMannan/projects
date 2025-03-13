#bmi calculator using streamlit project

#importing module of streamlit to use
import streamlit as st

#Set title of our app
st.title("BMI Calculator")

#create a slider for user to select height & weight
height = st.slider("Select your height (in cm): ",100,250,175)
weight = st.slider("Select your weight (in kg): ", 40,150,75)

#formula to calculate bmi
bmi = weight/((height/100)**2)

#printing user's BMI and response according to user's BMI
st.write(f"Your BMI is {bmi:.2f}.")
if(bmi<18.5):
    st.write("You are underweight.")
elif(bmi<25):
    st.write("You have normal weight.")
elif(bmi<30):
    st.write("You are overweight.")
else:
    st.write("You have Obesity.")

#Printing information about all categories of BMI 
st.write("### BMI Categories ###")
st.write("- Underweight, if your BMI is less than 18.5.")
st.write("- Normal weight, if your BMI is between 18.5 to 25.")
st.write("- Overweight, if your BMI is between 25 to 30")
st.write("- Obesity, if your BMI is more than 30")