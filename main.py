import streamlit as st
import plotly.express as px
from weather_api import get_data


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

if place:
    try:
        filtered_data = get_data(place, days)
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            temperatures = [round(temp - 273.15, 2) for temp in temperatures]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths, width=115)
    except KeyError:
        st.warning("This place does not exists !!!")
