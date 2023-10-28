import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\sanja\Desktop\project\startups_data.csv'
data = pd.read_csv(file_path)

# Set up the Streamlit app
st.title("Startup Analysis Dashboard")

# Top 10 startups by revenue over the last 5 years
data['Amount'] = data['Amount'].str.replace('[\$,]', '', regex=True)
data['Amount'] = pd.to_numeric(data['Amount'], errors='coerce')
top_10_startups = data.sort_values(by='Amount', ascending=False).head(10)

st.subheader("Top 10 Startups by Revenue")
st.write(top_10_startups)

# Create a bar plot to visualize the top 10 startups
plt.figure(figsize=(10, 6))
plt.barh(top_10_startups['Company Name'], top_10_startups['Amount'], color='skyblue')
plt.xlabel('Revenue')
plt.title('Top 10 Startups by Revenue over the Last 5 Years')
plt.gca().invert_yaxis()
st.pyplot(plt)

# The rest of your analysis and visualization code for other sections...
