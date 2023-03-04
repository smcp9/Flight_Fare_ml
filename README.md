# Flight Fare Prediction

# Overview 

This is a Streamlit web app which predicts fare of flight tickets.

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps.

Web app Link:
https://smcp9-flight-fare-ml-app1-t78248.streamlit.app/#departure-time

# Installation
The Code is written in Python 3.9. To install the required packages and libraries, run this command in the project directory after cloning the repository:
pip install -r requirements.txt

# Objective

The number of persons using aircraft has dramatically increased in recent years. Since prices fluctuate owing to several factors, it is challenging for airlines to maintain their prices. We shall therefore attempt to employ machine learning to address this issue. By foreseeing what costs airlines can keep, this can be helpful. Customers may use it to forecast future flight costs and make travel plans accordingly.

The objective of this model is to predict flight prices given the various parameters. Data used in this article is publicly available at Kaggle. 

Data Source: https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh

#### About the data

Airline: Name of the airline used for traveling

Date_of_Journey: Date at which a person traveled

Source: Starting location of flight

Destination: Ending location of flight

Route: This contains information on starting and ending location of the journey in the standard format used by airlines.

Dep_Time: Departure time of flight from starting location

Arrival_Time: Arrival time of flight at destination

Duration: Duration of flight in hours/minutes

Total_Stops: Number of total stops flight took before landing at the destination.

Additional_Info: Shown any additional information about a flight

Price: Price of the flight

#### Model Building

The model gives an accuracy of 80% and is bulit upon RandomForestRegressor from the python sklearn library.
It is a simple model built for exploring the deployment realm of machine learning.

# Future Scope
- The dataset contains prices of 2019. Building a model using relevant data containing route distance and fuel prices would give much better results.
- Feature engineering could be employed to consider weekends, festivals and holiday seasons.


