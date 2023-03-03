 

import streamlit as st
import pickle
import pandas as pd 
import numpy as np
import datetime
import time


def main():
    
    #Journey_day/ Departure/ Arrival

    st.title("Flight-Price-Prediction")
    st.write(" *--Built using StreamLit--* ")

    st.sidebar.subheader("Select Departure")
    m = pd.to_datetime("today").month
    d = pd.to_datetime("today").day
    y = pd.to_datetime("today").year
    
    dep = st.sidebar.date_input("Day" , datetime.date(y,m,d))
    if dep is not None:
        Journey_month = dep.month
        Journey_day = dep.day

        Dep_hour = st.sidebar.selectbox("Hour", list(range(1,25)))
        Dep_min = st.sidebar.selectbox("Minute", list(range(0,61)))

    st.subheader("Departure Time :")
    x = "2023" + "/"  +str(Journey_month) + "/" + str(Journey_day) + " " + str(Dep_hour) + ":" + str(Dep_min)
    
    if x is not None:
        op = pd.to_datetime([x])
        if op is not None:
            st.write(op.item())
    

    st.sidebar.subheader("Select Arrival")
    arr = st.sidebar.date_input("Day." , datetime.date(y,m,d+1))
    
    if arr is not None:
        mon_a = arr.month
        day_a = arr.day
        
        
        Arrival_hour = st.sidebar.selectbox("Hour.", list(range(1,25)) ,2)
        Arrival_min = st.sidebar.selectbox("Minute.", list(range(0,61)))

    st.subheader("Arrival Time :")
    x1 = "2023" + "/"  +str(mon_a) + "/" + str(day_a) + " " + str(Arrival_hour) + ":" + str(Arrival_min)
    
    if x1 is not None:
        op1 = pd.to_datetime([x1] )
        if op1 is not None:
            st.write(op1.item())
            
#-------------------------------------------------------------------------------------------------------------------------------

    #Source
    st.subheader("Select Source")
    source = st.selectbox(" " , ['Bangalore', 'Mumbai','Delhi','Kolkata',"Chennai"])
    
    S = {'Bangalore':0, 'Mumbai':0,'Delhi':0,'Kolkata':0,'Chennai':0}

    for i in S:
        if i == source:
            S[i] = 1

    
    st.write("Source -- " , source)
    
#-------------------------------------------------------------------------------------------------------------------------------
    #Destination
    st.subheader("Select Destination")
    dest = st.selectbox("" , ['Bangalore', 'Cochin', 'Hyderabad','New Delhi','Delhi','Kolkata'])

    D = {'Bangalore':0, 'Cochin':0, 'Hyderabad':0,"New Delhi":0,'Delhi':0,'Kolkata':0}
    
    for i in D:
        if i == dest:
            D[i] = 1

    st.write("Destination -- ",dest)
    
#-------------------------------------------------------------------------------------------------------------------------------
    #Airline
    st.subheader("Select Airline")
    airline = st.selectbox("  " , ["Air India","GoAir","IndiGo","Jet Airways","Multiple carriers","SpiceJet",
                                    "Vistara","Air Asia"])
    
    A = {"Air India":0,"GoAir":0,"IndiGo":0,"Jet Airways":0,"Multiple carriers":0,"SpiceJet":0,
                                    "Vistara":0,"Air Asia":0}
    

    for i in A:
        if i == airline:
            A[i] = 1

    st.write("Airline -- " , airline)

#-------------------------------------------------------------------------------------------------------------------------------

    #Stops
    st.subheader("Select Stops")
    Total_stops = st.selectbox("   " , [0,1,2,3,4])
    st.write("Stops -- ", Total_stops)

#-------------------------------------------------------------------------------------------------------------------------------   
    #Duration
    if st.checkbox("Duration"):
        if op1 is not None:
            
            st.write((op1.item() - op.item()))

    
    op2 = str(op1-op)
    if op2 is not None:
        dur_hour = int(op2.split(']')[0][-9:-7])
        dur_min = int(op2.split(']')[0][-6:-4])


#-------------------------------------------------------------------------------------------------------------------------------
    #model
    #model = open(r'C:\Users\Sarthak\Desktop\Flight-Price-Prediction\main_flight_rfr.pkl', "rb")
    #rfr_model = pickle.load(model)

    rfr_model = pickle.load(open("fare_rf1.pkl", "rb"))

    #prediction

  
    par1 = [Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            A['Air India'],
            A['GoAir'],
            A['IndiGo'],
            A['Jet Airways'],
            A['Multiple carriers'],
            A['SpiceJet'],
            A['Vistara'],
            S['Chennai'],
            S['Delhi'],
            S['Kolkata'],
            S['Mumbai'],
            D['Cochin'],
            D['Delhi'],
            D['Hyderabad'],
            D['Kolkata'],
            D['New Delhi']
           ]
    
                              
    if st.checkbox("Predict"):
        pred = rfr_model.predict([par1])
        for i in pred:
            st.write("Your Fare Price is : " , round(i ,3)  , "INR")
            st.write("*Happy and Safe Journey ...*")

    st.write("""    """)
    st.write("""    """)
   

if __name__ == "__main__":
    main()
