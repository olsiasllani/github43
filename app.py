import streamlit as st

if st.button("Click me"):
    st.write("Button Clicked")

if st.checkbox("Check me to show some text"):
    st.write("You re seeing this text because you checked the checkbox")

    user_input = st.text_input("Enter text", "sample text")
    st.write("You entered:", user_input)

age = st.number_input("Enter your age", min_value=0, max_value=100)

st.write(f"You age is:{age}")


 message = st.text_area("Enter a message")
 
st.write(f"Your message: {message}")
