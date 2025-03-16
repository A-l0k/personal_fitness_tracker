import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Personal Fitness Tracker")

# Sidebar for user input
st.sidebar.header("Enter Your Fitness Data")

# Input fields
date = st.sidebar.date_input("Date")
steps = st.sidebar.number_input("Steps", min_value=0)
calories_burned = st.sidebar.number_input("Calories Burned", min_value=0)
workout_duration = st.sidebar.number_input("Workout Duration (minutes)", min_value=0)

# Store data in a DataFrame
if "fitness_data" not in st.session_state:
    st.session_state.fitness_data = pd.DataFrame(columns=["Date", "Steps", "Calories Burned", "Workout Duration (min)"])

# Add data to the DataFrame
if st.sidebar.button("Add Entry"):
    new_entry = pd.DataFrame({
        "Date": [date],
        "Steps": [steps],
        "Calories Burned": [calories_burned],
        "Workout Duration (min)": [workout_duration]
    })
    st.session_state.fitness_data = pd.concat([st.session_state.fitness_data, new_entry], ignore_index=True)
    st.sidebar.success("Entry added!")

# Display the data
st.header("Fitness Data")
st.write(st.session_state.fitness_data)

# Visualize the data
st.header("Visualizations")

if not st.session_state.fitness_data.empty:
    # Plot Steps Over Time
    st.subheader("Steps Over Time")
    fig, ax = plt.subplots()
    ax.plot(st.session_state.fitness_data["Date"], st.session_state.fitness_data["Steps"], marker="o")
    ax.set_xlabel("Date")
    ax.set_ylabel("Steps")
    st.pyplot(fig)

    # Plot Calories Burned Over Time
    st.subheader("Calories Burned Over Time")
    fig, ax = plt.subplots()
    ax.plot(st.session_state.fitness_data["Date"], st.session_state.fitness_data["Calories Burned"], marker="o", color="red")
    ax.set_xlabel("Date")
    ax.set_ylabel("Calories Burned")
    st.pyplot(fig)

    # Plot Workout Duration Over Time
    st.subheader("Workout Duration Over Time")
    fig, ax = plt.subplots()
    ax.plot(st.session_state.fitness_data["Date"], st.session_state.fitness_data["Workout Duration (min)"], marker="o", color="green")
    ax.set_xlabel("Date")
    ax.set_ylabel("Workout Duration (min)")
    st.pyplot(fig)
else:
    st.warning("No data available yet. Please add entries using the sidebar.")