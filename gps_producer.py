from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_gps_data(vehicle_id):
    return {
        "vehicle_id": vehicle_id,
        "lat": round(random.uniform(12.9, 13.1), 6),
        "lon": round(random.uniform(77.5, 77.7), 6),
        "speed": round(random.uniform(20, 80), 2),
        "timestamp": time.time()
    }

while True:
    for vid in range(1, 6):
        data = generate_gps_data(vid)
        producer.send('traffic_data', data)
        print("Sent:", data)
    time.sleep(2)