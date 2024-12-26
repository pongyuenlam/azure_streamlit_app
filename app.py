import streamlit as st
st.text_input("Please enter the password to use this App", key="in_password", type="password")
app_password = st.session_state.in_password
if app_password:
    if (app_password != PASSWORD_APP):
        st.write("Password incorrect, please try again")
    else:
        st.write("password correct")
