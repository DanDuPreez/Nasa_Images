import requests
import streamlit as st

# Prepare API key and API url
api_key = "D1EZPwNJKSVY4PYo5pkqZ81lk8fkQis1yxcPhgwa"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# Get the request data as a dictionary
response1 = requests.get(url)
data = response1.json()