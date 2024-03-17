import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
city = st.text_input("Place:", placeholder="Tokyo")
days = st.slider("Forecast Days",
                 min_value=1,
                 max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox("Select data to view",
                      ("Temperature", "Sky")
                      )
st.subheader(f"{option} for the next {days} day(s) in {city}")

if city:
    filtered_data = get_data(city=city, days=days)

    match option:
        case "Temperature":
            temperatures = [item["main"]["temp"] for item in filtered_data]
            dates = [item["dt_txt"] for item in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        case "Sky":
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }
            sky_conditions = [item["weather"][0]["main"] for item in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=150)


