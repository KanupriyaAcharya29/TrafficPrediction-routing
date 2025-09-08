# 🚦 Smart Traffic Prediction & Routing System  

## 📌 Overview  
This project is a *real-time traffic prediction and smart routing system*.  
It uses *Kafka* for data ingestion, *Spark* for ETL, a *hybrid GNN + LSTM model* for traffic forecasting, and exposes results via a *Flask API* and an interactive *Streamlit dashboard*.  

---

## 🏗 Repository Structure

smart-traffic-prediction/
│── README.md
│── requirements.txt
│── docker-compose.yml
│
├── data/ # Sample traffic data
├── kafka/ # Real-time GPS producer
├── spark/ # ETL and feature engineering
├── feature_store/ # Store & retrieve features
├── models/ # GNN + LSTM training
├── serving/ # Flask API
└── frontend/ # Streamlit dashboard


## ⚙️ Tech Stack  
- *Python 3.9+*  
- *Apache Kafka* – Real-time ingestion  
- *Apache Spark* – Big data processing  
- *PyTorch / TensorFlow* – ML model training  
- *Flask* – REST API  
- *Streamlit + Folium* – Dashboard visualization  
- *Docker Compose* – Multi-service deployment  

---

## 📊 Features  
- Real-time GPS data ingestion (Kafka)  
- Big data ETL pipeline (Spark)  
- Hybrid ML model (GNN + LSTM) for traffic forecasting  
- Optimal route calculation using NetworkX  
- REST API for predictions & routes  
- Interactive dashboard with live traffic maps

- 👩‍💻 Author

Kanupriya Acharya
B.Tech CSE | Data Science & AI Enthusiast 🚀
