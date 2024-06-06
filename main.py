import streamlit as st
import backend as be

st.title("Weather Query Bot")
st.write("Ask about the weather or any other query.")
user_input = st.text_input("Enter your query:")

if st.button("Submit"):
    if user_input:

        if "weather" in user_input.lower():

            response = be.check_weather(user_input)
            
        else:

            response = be.search_query(user_input)
        
        st.write(response)
    else:
        st.write("Please enter a query.")