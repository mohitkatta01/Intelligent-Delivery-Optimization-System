import streamlit as st
import json
import folium
from streamlit_folium import folium_static

# Initialize session state to keep track of vehicles and jobs
if 'vehicles' not in st.session_state:
    st.session_state['vehicles'] = []

if 'jobs' not in st.session_state:
    st.session_state['jobs'] = []

# Function to add a vehicle
def add_vehicle():
    new_vehicle = {
        "start": [float(st.session_state.start_lon), float(st.session_state.start_lat)],
        "capacity": [int(st.session_state.capacity)],
        "end": [float(st.session_state.end_lon), float(st.session_state.end_lat)],
        "id": len(st.session_state.vehicles) + 1,
        "time_window": [int(st.session_state.start_time), int(st.session_state.end_time)]
    }
    st.session_state.vehicles.append(new_vehicle)

# Function to add a job
def add_job():
    new_job = {
        "delivery": [int(st.session_state.delivery)],
        "id": len(st.session_state.jobs) + 1,
        "service": int(st.session_state.service),
        "location": [float(st.session_state.job_lon), float(st.session_state.job_lat)]
    }
    if st.session_state.time_window_start and st.session_state.time_window_end:
        new_job["time_windows"] = [[int(st.session_state.time_window_start), int(st.session_state.time_window_end)]]
    st.session_state.jobs.append(new_job)

# Streamlit interface
st.title("Generate JSON for Vehicles and Jobs")

# Columns for Vehicle and Job input
col1, col2 = st.columns(2)

with col1:
    st.header("Add Vehicle")
    st.text_input("Start Longitude", key="start_lon")
    st.text_input("Start Latitude", key="start_lat")
    st.text_input("Capacity", key="capacity")
    st.text_input("End Longitude", key="end_lon")
    st.text_input("End Latitude", key="end_lat")
    st.text_input("Start Time Window", key="start_time")
    st.text_input("End Time Window", key="end_time")
    if st.button("Add Vehicle"):
        add_vehicle()

with col2:
    st.header("Add Job")
    st.text_input("Delivery", key="delivery")
    st.text_input("Service", key="service")
    st.text_input("Job Longitude", key="job_lon")
    st.text_input("Job Latitude", key="job_lat")
    st.text_input("Time Window Start", key="time_window_start")
    st.text_input("Time Window End", key="time_window_end")
    if st.button("Add Job"):
        add_job()

# Display JSON
if st.button("Generate JSON"):
    data = {
        "vehicles": st.session_state.vehicles,
        "jobs": st.session_state.jobs
    }
    st.json(data)

st.header("Current Vehicles and Jobs")
st.write("Vehicles", st.session_state.vehicles)
st.write("Jobs", st.session_state.jobs)



# Function to generate map from JSON
# Function to generate map from JSON
def generate_map(json_data):
    # Check if 'routes' key is in the JSON data
    if 'routes' not in json_data:
        st.error("No routes found in JSON data")
        return None

    map_center = [json_data['routes'][0]['steps'][0]['location'][1], json_data['routes'][0]['steps'][0]['location'][0]]
    map_ = folium.Map(location=map_center, zoom_start=12)

    for route in json_data['routes']:
        for step in route['steps']:
            location = [step['location'][1], step['location'][0]]
            step_type = step['type']
            if step_type == 'start':
                color = 'green'
            elif step_type == 'job':
                color = 'blue'
            elif step_type == 'end':
                color = 'red'
            else:
                color = 'gray'
            folium.Marker(
                location=location,
                popup=f"Type: {step_type}, ID: {step.get('id', 'N/A')}",
                icon=folium.Icon(color=color)
            ).add_to(map_)

    # Add lines between points based on routes
    # for route in json_data['routes']:
    #     points = [[step['location'][1], step['location'][0]] for step in route['steps']]
    #     folium.PolyLine(points, color='blue', weight=5, opacity=0.7).add_to(map_)

    # add lines between points along roads
    for route in json_data['routes']:
        points = [[step['location'][1], step['location'][0]] for step in route['steps']]
        folium.PolyLine(points, color='blue', weight=5, opacity=0.7).add_to(map_)
    

    # Change colors as per vehicle
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']
    for i, route in enumerate(json_data['routes']):
        points = [[step['location'][1], step['location'][0]] for step in route['steps']]
        folium.PolyLine(points, color=colors[i % len(colors)], weight=5, opacity=0.7).add_to(map_)

    return map_


json_data = {
    "code": 0,
    "summary": {
        "cost": 13207,
        "routes": 2,
        "unassigned": 0,
        "delivery": [
            9
        ],
        "amount": [
            9
        ],
        "pickup": [
            0
        ],
        "setup": 0,
        "service": 1500,
        "duration": 13207,
        "waiting_time": 0,
        "priority": 0,
        "violations": [],
        "computing_times": {
            "loading": 41,
            "solving": 3,
            "routing": 0
        }
    },
    "unassigned": [],
    "routes": [
        {
            "vehicle": 1,
            "cost": 7306,
            "delivery": [
                5
            ],
            "amount": [
                5
            ],
            "pickup": [
                0
            ],
            "setup": 0,
            "service": 900,
            "duration": 7306,
            "waiting_time": 0,
            "priority": 0,
            "steps": [
                {
                    "type": "start",
                    "location": [
                        77.70228200000001,
                        12.7831358
                    ],
                    "setup": 0,
                    "service": 0,
                    "waiting_time": 0,
                    "load": [
                        5
                    ],
                    "arrival": 1600416000,
                    "duration": 0,
                    "violations": []
                },
                {
                    "type": "job",
                    "location": [
                        77.47897809999999,
                        12.9097719
                    ],
                    "id": 5,
                    "setup": 0,
                    "service": 300,
                    "waiting_time": 0,
                    "job": 5,
                    "load": [
                        2
                    ],
                    "arrival": 1600418223,
                    "duration": 2223,
                    "violations": []
                },
                {
                    "type": "job",
                    "location": [
                        77.4971795,
                        12.9234009
                    ],
                    "id": 4,
                    "setup": 0,
                    "service": 300,
                    "waiting_time": 0,
                    "job": 4,
                    "load": [
                        1
                    ],
                    "arrival": 1600418785,
                    "duration": 2485,
                    "violations": []
                },
                {
                    "type": "job",
                    "location": [
                        77.4538699,
                        13.068898
                    ],
                    "id": 3,
                    "setup": 0,
                    "service": 300,
                    "waiting_time": 0,
                    "job": 3,
                    "load": [
                        0
                    ],
                    "arrival": 1600420716,
                    "duration": 4116,
                    "violations": []
                },
                {
                    "type": "end",
                    "location": [
                        77.70228200000001,
                        12.7831358
                    ],
                    "setup": 0,
                    "service": 0,
                    "waiting_time": 0,
                    "load": [
                        0
                    ],
                    "arrival": 1600424206,
                    "duration": 7306,
                    "violations": []
                }
            ],
            "violations": []
        },
        {
            "vehicle": 2,
            "cost": 5901,
            "delivery": [
                4
            ],
            "amount": [
                4
            ],
            "pickup": [
                0
            ],
            "setup": 0,
            "service": 600,
            "duration": 5901,
            "waiting_time": 0,
            "priority": 0,
            "steps": [
                {
                    "type": "start",
                    "location": [
                        77.70228200000001,
                        12.7831358
                    ],
                    "setup": 0,
                    "service": 0,
                    "waiting_time": 0,
                    "load": [
                        4
                    ],
                    "arrival": 1600416000,
                    "duration": 0,
                    "violations": []
                },
                {
                    "type": "job",
                    "location": [
                        77.656476,
                        13.0521424
                    ],
                    "id": 2,
                    "setup": 0,
                    "service": 300,
                    "waiting_time": 0,
                    "job": 2,
                    "load": [
                        2
                    ],
                    "arrival": 1600418604,
                    "duration": 2604,
                    "violations": []
                },
                {
                    "type": "job",
                    "location": [
                        77.7537243,
                        13.0452482
                    ],
                    "id": 1,
                    "setup": 0,
                    "service": 300,
                    "waiting_time": 0,
                    "job": 1,
                    "load": [
                        0
                    ],
                    "arrival": 1600419964,
                    "duration": 3664,
                    "violations": []
                },
                {
                    "type": "end",
                    "location": [
                        77.70228200000001,
                        12.7831358
                    ],
                    "setup": 0,
                    "service": 0,
                    "waiting_time": 0,
                    "load": [
                        0
                    ],
                    "arrival": 1600422501,
                    "duration": 5901,
                    "violations": []
                }
            ],
            "violations": []
        }
    ]
}

# Button to generate map
if st.button("Generate Map"):
    map_ = generate_map(json_data)
    folium_static(map_)

# st.header("Current Vehicles and Jobs")
# st.write("Vehicles", st.session_state.vehicles)
# st.write("Jobs", st.session_state.jobs)
    