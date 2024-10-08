from datetime import datetime, timedelta
from collections import Counter

# Given flight data
flights = [
    "flight_id,airline,origin_destination,datetime,terminal,gate,passengers",
    "BA123,British Airways,incoming,2024-06-28 14:30,5,A22,180",
    "BA124,British Airways,outgoing,2024-06-28 16:30,5,A23,185",
    "BA125,British Airways,incoming,2024-06-28 18:45,5,A24,175",
    "BA126,British Airways,outgoing,2024-06-29 08:15,5,A22,190",
    "LH456,Lufthansa,outgoing,2024-06-28 15:45,2,B10,220",
    "LH457,Lufthansa,incoming,2024-06-28 17:30,2,B11,215",
    "LH458,Lufthansa,outgoing,2024-06-29 09:00,2,B10,225",
    "LH459,Lufthansa,incoming,2024-06-29 11:30,2,B12,210",
    "AF789,Air France,incoming,2024-06-28 16:15,3,C5,195",
    "AF790,Air France,outgoing,2024-06-28 18:00,3,C6,200"
]

# Extracting headers and rows
headers = flights[0].split(",")
rows = [flight.split(",") for flight in flights[1:]]

# Function to parse the flight datetime
def parse_flight_time(flight_time):
    return datetime.strptime(flight_time, "%Y-%m-%d %H:%M")

# 1. More crowded flight in 2 hours (we'll take the current time as "2024-06-28 14:30" for this example)
def more_crowded_in_2_hours(current_time_str):
    current_time = parse_flight_time(current_time_str)
    two_hours_later = current_time + timedelta(hours=2)
    
    crowded_flight = None
    max_passengers = 0
    
    for row in rows:
        flight_time = parse_flight_time(row[3])
        passengers = int(row[6])
        
        if current_time <= flight_time <= two_hours_later:
            if passengers > max_passengers:
                max_passengers = passengers
                crowded_flight = row
    
    return crowded_flight

# Example current time (as per question context)
current_time = "2024-06-28 14:30"
crowded_flight = more_crowded_in_2_hours(current_time)

if crowded_flight:
    print(f"Most crowded flight within 2 hours: {crowded_flight[0]} with {crowded_flight[6]} passengers.")
else:
    print("No flight found within 2 hours.")

# 2. Common terminal and gate
def common_terminal_gate():
    terminal_gate_pairs = [(row[4], row[5]) for row in rows]
    counter = Counter(terminal_gate_pairs)
    
    most_common = counter.most_common(1)[0]  # Get the most common terminal and gate
    return most_common

common_pair = common_terminal_gate()
print(f"Most common terminal and gate: Terminal {common_pair[0][0]}, Gate {common_pair[0][1]} (appears {common_pair[1]} times)")

# 3. Balanced flight (defined as having a passenger count close to the average)
def balanced_flight():
    passenger_counts = [int(row[6]) for row in rows]
    avg_passengers = sum(passenger_counts) / len(passenger_counts)
    
    # Finding the flight with passengers closest to the average
    balanced_flight = min(rows, key=lambda x: abs(int(x[6]) - avg_passengers))
    
    return balanced_flight, avg_passengers

balanced, avg_passengers = balanced_flight()
print(f"Balanced flight: {balanced[0]} with {balanced[6]} passengers (average: {avg_passengers:.2f})")

