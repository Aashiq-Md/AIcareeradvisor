from google import genai
import streamlit as st
advisor=genai.Client(api_key="AIzaSyDr_EH3XI44ltHmHAF5KaLJK5Igl7veRS0")
age=st.text_input("what is your age:")
qualification=st.text_input("what is your qualification:")
designation=st.text_input("what is your current designation:")
salary=st.text_input("what is your  current salary:")
skills=st.text_input("what is your skills:")
experience=st.text_input("Mention your experience:")
interest=st.text_input("which fields are you interested in?:")
goals=st.text_input("what is your career goals:")
location=st.text_input("what is your preferred location:")
languages=st.text_input("what are the  languages you know:")
nationality=st.text_input("what is your nationality:")

prompt=f"""you are a expert career advisor. Based on the following inputs from the user,give a career advise
age: {age}
qualification: {qualification}
designation: {designation}
salary: {salary}
skills: {skills}
experience: {experience}
interest: {interest}
goals: {goals}
location: {location}
languages: {languages}
nationality: {nationality}
keep it simple and jot it in bullet points,also suggest some resourse material and course links
"""

if st.button("Submit:"):
    response=advisor.model.generate_content(model="gemini-1.5-flash",contents=prompt)
    st.write(response.text)
