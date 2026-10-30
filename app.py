import streamlit as st
import pandas as pd


st.title("Smart Temperature Alert System")

temperature = st.slider(
    "Temperature (°C)", 20, 50, 30
)

st.metric("Temperature", f"{temperature} °C")

# TASK 3: Change the threshold to 38
if temperature >= 38:
    st.error("WARNING: High Temperature!")
    st.write("Red LED: ON")
else:
    st.success("NORMAL TEMPERATURE")
    st.write("Red LED: OFF")

data = pd.DataFrame({
    "Temperature": [30, 37, 38, 42]
})

st.dataframe(data)
st.line_chart(data, y="Temperature")
