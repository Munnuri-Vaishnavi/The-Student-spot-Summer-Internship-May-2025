# The-Student-spot-Summer-Internship-May-2025
# Basic Chatbot using Streamlit and Conditional Statements in Python

This is a simple chatbot application built using Python Conditional Statements and the Streamlit library to create a basic UI. The chatbot responds to a set of predefined questions using conditional statements.

## Features
- Built with *Streamlit* for a quick and easy web-based interface.
- Mainly focused on The Student Spot realted ques.
- Uses if-elif-else conditional ladder to respond to specific questions.
- Includes a basic function (def) to handle the chatbot logic.
- Returns a default response if the input doesn't match any predefined questions.

## How It Works
- The user enters a question in the chatbot input box.
- The chatbot checks the input against predefined questions.
- If a match is found, it returns the corresponding answer.
- If there's no match, it replies with: "I don't understand that question."

## Example Questions
- "Do you know about The Student Spot?"
- "What is StudentSpot SummerInternship?"
- "How can i join into the Student Spot?"

## Requirements
- Python 3.x
- Streamlit
  
  import streamlit as st

# Function to handle chatbot responses
```def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hii" in user_input or "hello" in user_input:
        return "hello how can I help you"
    elif "know" in user_input and "about" in user_input:
        return "yes offcourse"
    elif "what" in user_input and "studentspot" in user_input:
        return "The Student Spot is a vibrant online community designed to empower students. which gives updates about internships,webinars,workshops,events,jobs,hackothans etc."
    elif "want" in user_input and "join" in user_input:
        return "That's Nice, All the best for your journey...."
    elif "join" in user_input:
        return "Any interested students can join.There is no restrictions for it."
    elif "gain" in user_input or "updates" in user_input:
        return "you will get the updates regarding internships,govt,private jobs,webinars,workshops,events and networking."
    elif "founder" in user_input or "ceo" in user_input:
        return "Rajkamal Panthagani is the Founder and CEO of THE STUDENT SPOT"
    elif "teams" in user_input:
        return "Campus Ambassador,Web Development,Creative Team,Content and Research Team,Social Media Team."
    elif "trusted" in user_input:
        return "Yes, many companies recognize StudentSpots certifications."
    elif "fee" in user_input or "paid" in user_input:
        return "Its, absolutely free of cost."
    elif "summerinternship" in user_input:
        return "Student Spot Offers SummerInternship for students to gain practical experience of their Skills in different domains."
    elif "gain" in user_input and "SummerInternship" in user_input:
        return "You will get Certificate to showcase and you will also get recommendations based on your work."
    elif "stipend" in user_input:
        return "you will get goodies and Swags based on your group"
    elif "domains" in user_input:
        return "The domians are AI,Web development,CyberSecurity,Data science,Python,Java,Android Development,UI/UX,c++"
    elif "duration" in user_input:
        return "Its a 1 month Internship."
    else:
        return "Sorry, I don't understand that question."

# Streamlit UI
st.set_page_config(page_title="StudentSpot Chatbot", layout="centered")
st.title("StudentSpot Chatbot")
st.markdown("Welcome to StudentSpot Chatbot!")

user_input = st.text_input("Type your question here:")

if user_input:
    response = chatbot_response(user_input)
    st.write("*Bot:*",response)```

