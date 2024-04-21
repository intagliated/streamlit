import streamlit as st

title = st.title('Maximum of 3 numbers:')

number1 = st.number_input("Input a Number:") 
number2 = st.number_input("Input a Number:") 
number3 = st.number_input("Input a Number:")

st.write(max([number1,number2,number3]))
