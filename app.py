import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np

# Optimal values
OPTIMAL_TEMPERATURE = (37, 38)  # Range for optimal temperature in °C
OPTIMAL_HUMIDITY = (45, 50)     # Range for optimal humidity in %

# Simulated historical data
def generate_historical_data(num_points=10):
    temperature_history = [random.uniform(35, 40) for _ in range(num_points)]
    humidity_history = [random.uniform(40, 60) for _ in range(num_points)]
    return temperature_history, humidity_history

# Function to predict if hatching will occur based on conditions
def predict_hatching(temperature, humidity):
    if OPTIMAL_TEMPERATURE[0] <= temperature <= OPTIMAL_TEMPERATURE[1] and \
       OPTIMAL_HUMIDITY[0] <= humidity <= OPTIMAL_HUMIDITY[1]:
        return "Likely to Hatch", "green"
    else:
        return "Unlikely to Hatch", "red"

# Streamlit interface
st.title("Egg Incubator Prediction App")

# Display the optimal values for reference
st.subheader("Optimal Conditions for Incubation:")
st.write(f"**Temperature:** {OPTIMAL_TEMPERATURE[0]}°C - {OPTIMAL_TEMPERATURE[1]}°C")
st.write(f"**Humidity:** {OPTIMAL_HUMIDITY[0]}% - {OPTIMAL_HUMIDITY[1]}%")

# Manual input option
st.subheader("Manual Input for Sensor Values:")
manual_input = st.checkbox("Manually Input Sensor Values")

if manual_input:
    temperature = st.slider("Set Temperature (°C)", 35.0, 40.0, 37.5)
    humidity = st.slider("Set Humidity (%)", 40.0, 60.0, 47.5)
else:
    temperature = random.uniform(35, 40)
    humidity = random.uniform(40, 60)

st.write(f"**Current Temperature:** {temperature:.2f}°C")
st.write(f"**Current Humidity:** {humidity:.2f}%")

# Prediction
prediction, color = predict_hatching(temperature, humidity)
st.markdown(f"### Prediction: <span style='color:{color}'>{prediction}</span>", unsafe_allow_html=True)

# Historical data
st.subheader("Historical Sensor Data:")
temperature_history, humidity_history = generate_historical_data()

# Plotting the graph
fig, ax = plt.subplots()
time_points = np.arange(len(temperature_history))

ax.plot(time_points, temperature_history, label='Temperature (°C)', color='blue')
ax.plot(time_points, humidity_history, label='Humidity (%)', color='orange')

ax.set_xlabel("Time (arbitrary units)")
ax.set_ylabel("Value")
ax.set_title("Temperature & Humidity Over Time")
ax.legend()

# Display the graph in Streamlit
st.pyplot(fig)
