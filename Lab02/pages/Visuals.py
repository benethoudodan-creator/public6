# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

# PAGE TITLE AND INFORMATION
st.title(" Technology Expense Visuals📈")
st.write("This page displays graphs based on the collected data.")

data = pd.read_csv("data.csv")
# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")

if os.path.exists("data.csv"):
    df = pd.read_csv("data.csv")
    st.dataframe(df) #NEW
else:
    st.warning("data.csv not found")
    df = pd.DataFrame(columns=["Device", "Amount"])

if os.path.exists("data.json") and os.path.getsize > 0:
    with open(json_path, "r") as f:
        json_data = json.load(f)
else:
    json_data = {"device_title": "", "amount" : []}
    st.warning("JSON not found")
ƒ    
# TO DO:
# 1. Load the data from 'data.csv' into a pandas DataFrame.
#    - Use a 'try-except' block or 'os.path.exists' to handle cases where the file doesn't exist.
# 2. Load the data from 'data.json' into a Python dictionary.
#    - Use a 'try-except' block here as well.

st.info("TODO: Add your data loading logic here.")


# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.divider()
st.header("Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("Bar Visuals of Technology expenses") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create a static graph (e.g., bar chart, line chart) using st.bar_chart() or st.line_chart().
# - Use data from either the CSV or JSON file.
# - Write a description explaining what the graph shows.


if not data.empty:
    st.bar_chart(data.set_index("Device")["Amount"], color = "#00FF00")
    st.caption("This Bar graph shows how much money the user spends when buying a device")
else:
    st.warning("Placeholder for your first graph.")


# GRAPH 2: DYNAMIC GRAPH
st.subheader("Line Trends of money spent on Technology") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
device_categories = data["Device"]

if device_categories not in st.session_state:
    st.session_state.selected_category = device_categories[0] #NEW
if len(device_categories) > 0:
    st.session_state.selected_category = st.multiselect(
        "Choose a Device",
        options=["Phone", "Tablet/iPad", "Computer/Laptop", "Headphone/Audio Device", "Video Game Console"],
        default=["Phone"]
    )

    if st.session_state.selected_category:
        showdw = data[data["Device"].isin(st.session_state.selected_category)]
    else:
        showdw = data.iloc[0:0]

    if showdw.empty:
        st.warning("Oops your graph isn't showing :(")
    else:
        st.line_chart(showdw.set_index("Device")["Amount"])
    st.caption("This graph shows the line trends of spent on a device. You can decide which device will show using the device buttons.")
        
    
else:
    st.warning("Oops your graph isn't showing :(")



# TODO:
# - Create a dynamic graph that changes based on user input.
# - Use at least one interactive widget (e.g., st.slider, st.selectbox, st.multiselect).
# - Use Streamlit's Session State (st.session_state) to manage the interaction.
# - Add a '#NEW' comment next to at least 3 new Streamlit functions you use in this lab.
# - Write a description explaining the graph and how to interact with it.




# GRAPH 3: DYNAMIC GRAPH
st.subheader("Area chart of Money spent on technology") # CHANGE THIS TO THE TITLE OF YOUR GRAPH

if not d_dict or "data_points" not in d_dict:
    st.warning("Oops, where is the json??")
else:
    jdata = pd.DataFrame(d_dict["data_points"])
    jdata["Device"] = jdata["Device"].astype(str).str.strip()
    jdata["Amount"] = pd.to_numeric(jdata["Amount"], errors="coerce").fillna(0) #NEW

    devices = sorted(jdata["Device"].unique().tolist())

    if "selected_device" not in st.session_state:
        st.session_state.selected_device = "ALL DEVICES"

    tech_choice = st.radio("Choose a Device", options=["ALL DEVICES"] + devices, index=0, key="selected_device"
                           )
    if tech_choice == "ALL DEVICES":
        st.area_chart(jdata.set_index("Device")[["Amount"]])
    else:
        fdata = jdata[jdata["Device"] == tech_choice][["Device", "Amount"]]
        if fdata.empty:
            st.warning("Where is the data??")
        else:
            st.bar_chart(fdata.set_index("Device")[["Amount"]]) #NEW

    st.caption("Select which amount you want view")

    

                                                    
                                                       


                    
# TO DO:
# - Create another dynamic graph.
# - If you used CSV data for Graph 1 & 2, you MUST use JSON data here (or vice-versa).
# - This graph must also be interactive and use Session State.
# - Remember to add a description and use '#NEW' comments.

