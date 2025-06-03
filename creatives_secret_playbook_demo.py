# Rebuilding the script after code execution environment reset
from datetime import time

# Create the content of the Streamlit script
script_content = '''
import streamlit as st
from datetime import datetime, time

# Simulate session state defaults
if 'location' not in st.session_state:
    st.session_state.location = "From Home"
if 'projects' not in st.session_state:
    st.session_state.projects = 1
if 'work_style' not in st.session_state:
    st.session_state.work_style = "Focused Pomodoros of 20 mins"

# LEFT PANEL INPUTS
st.title("The Creative’s Secret Playbook")

st.header("Environment & Setup")

st.write("### 🌦 Is it raining?")
location = st.radio("Where are you working from?", ["Office", "From Home", "Third Space"])
st.session_state.location = location

st.write("### 🎯 What are you working on today?")
projects = st.slider("How many projects are you working on today?", 1, 7, 1)
st.session_state.projects = projects

st.write("### 🕰️ How would you like to work today?")
work_style = st.radio("Choose your work style:", [
    "Top Three Tasks",
    "Focused Pomodoros of 20 mins",
    "By quarters",
    "Custom",
    "Flexibly"
])
st.session_state.work_style = work_style

# RIGHT PANEL - GENERATED WORKDAY PLAN
st.markdown("---")
st.header("📋 Today's Custom Work Plan")

st.write(f"**Location**: {st.session_state.location}")
st.write(f"**Number of Projects**: {st.session_state.projects}")
st.write(f"**Work Style**: {st.session_state.work_style}")

# Dynamic Widget Based on Work Style
if st.session_state.work_style == "Top Three Tasks":
    st.write("🔹 Focus on completing your top 3 priorities today.")
elif st.session_state.work_style == "Focused Pomodoros of 20 mins":
    st.write("⏱ You’ll work in 4 Pomodoro blocks:")
    st.write("- 20 mins work / 5 mins break × 4")
elif st.session_state.work_style == "By quarters":
    st.write("🕒 Your day is split into quarters:")
    st.write("- 9–11am\\n- 12–1pm (Lunch)\\n- 1–3pm\\n- 3–5pm")
elif st.session_state.work_style == "Custom":
    st.write("✏️ Design your own custom block schedule below.")
    custom_start = st.time_input("Start Time", time(9, 0))
    custom_end = st.time_input("End Time", time(17, 0))
    st.write(f"Custom Schedule: {custom_start.strftime('%I:%M %p')} – {custom_end.strftime('%I:%M %p')}")
else:
    st.write("🌈 You’re working flexibly today—follow your creative flow.")
'''

# Save the script to a file
script_path = "/mnt/data/creatives_secret_playbook_demo.py"
with open(script_path, "w") as f:
    f.write(script_content)

script_path
