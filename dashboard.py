import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("🚦 Smart Traffic Prediction Dashboard")

m = folium.Map(location=[12.95, 77.6], zoom_start=12)
folium.Marker([12.95, 77.6], popup="Traffic Source").add_to(m)
folium.Marker([13.0, 77.65], popup="Traffic Target").add_to(m)

st_folium(m, width=700, height=500)

st.write("Predicted Congestion: Moderate 🚗🚕🚙")