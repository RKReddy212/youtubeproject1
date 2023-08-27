import streamlit as st
import pymongo

# Create a Streamlit app
st.title("Explore YouTube channel Data in Streamlit")

# Import the necessary libraries
import pymongo

# Load the data from MongoDB
client = pymongo.MongoClient("mongodb+srv://rkreddy4895:Rkr2298@rkreddy.nn8dtc8.mongodb.net/?retryWrites=true&w=majority")
db = client["youtube"]
collection = db["channels"]
data = collection.find()

# Create a sidebar with controls for filtering and exploring the data
st.sidebar.title("Filters")

channel_id = st.sidebar.selectbox("Channel ID", list(data))

# Create a main area for displaying the data
if channel_id:
    channel_data = data.get(channel_id)
    st.write(channel_data)
