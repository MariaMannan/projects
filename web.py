#Project9 : Python website
# SAMPLE DATA FILE IS ALSO PROVIDED IN FOLDER

#Importing required libraries
import streamlit as st
import pandas as pd

st.title("Data Analysis")
#uploading a csv file
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

#if file is uploaded successfully then this block will work
if uploaded_file is not None:
    #reading file and converting it into dataframe
    df = pd.read_csv(uploaded_file)

#displaying first five datasets
    st.subheader("Data Preview")
    st.write(df.head())

#Displaying summary of data with min, max, avrg etc operations
    st.subheader("Data Summary")
    st.write(df.describe())

#Filtering some records from data
    st.subheader("Filter data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Choose a column to select",columns)
    unique_value = df[selected_column].unique()
    selected_value = st.selectbox("Choose a value to select",unique_value)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

#selecting x and y axis from columns for ploting a graph 
    x_column = st.selectbox("Choose any column for x axis", columns)
    y_column = st.selectbox("Choose any column for y axis", columns)

#when button is pressed to generate a graph, a line graph will be seen
    st.subheader("Plot graph")

    if st.button("Generate Graph"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

#if file is not uploaded, show this message
else:
    st.write("Waiting for file upload")