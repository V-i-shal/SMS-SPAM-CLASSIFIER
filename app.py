import streamlit as st
import pickle

# Load the model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Streamlit app interface
st.title("📩 SMS Spam Classifier")
st.write("Enter a message below to check if it's spam or not.")

# User input
user_input = st.text_area("Type your message here:")

# Predict button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Transform input text and predict
        transformed_input = vectorizer.transform([user_input])
        prediction = model.predict(transformed_input)[0]

        # Display result
        if prediction == "spam":
            st.error("This message is classified as **SPAM**.")
        else:
            st.success("This message is classified as **NOT SPAM**.")
