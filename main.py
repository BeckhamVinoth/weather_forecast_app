import streamlit as st


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
