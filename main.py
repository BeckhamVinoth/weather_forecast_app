import streamlit as st
import plotly.express as px


st.title('Weather Forecast App 🌦🌩☀')

place = st.text_input("Place :")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="You can select number of days here for weather forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
if days == 1:
    sub_header_text = f"{option} for tomorrow in {place}"
else:
    sub_header_text = f"{option} for the next {days} days in {place}"

st.subheader(sub_header_text)


def get_data(days):
    dates_val = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperature_val = [10, 11, 15]
    return dates_val, temperature_val


dates, temperature = get_data(days)

figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)
