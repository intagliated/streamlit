import streamlit as st

title = st.title('Maximum of 3 numbers:')

numbers =[st.number_input("Input a Number:") for i in range(3)]
st.write(max(numbers))
