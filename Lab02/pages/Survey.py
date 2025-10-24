# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)

# PAGE TITLE AND USER DIRECTIONS
st.title("Technology expense data📝")
st.write("Please fill out the highest amount of money you spent on a device")

fname = 'data.csv'

# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
with st.form("survey_form"):
    # Create text input widgets for the user to enter data.
    # The first argument is the label that appears above the input box.
    phone = st.number_input("Phone")
    tablet_iPad = st.number_input("Tablet/iPad")
    computer_laptop = st.number_input("Computer/Laptop")
    headphones = st.number_input("Headphones/Audio Device")
    video_game_console = st.number_input(f"Video Game console")
    

    # The submit button for the form.
    submitted = st.form_submit_button("Submit Data")

    # This block of code runs ONLY when the submit button is clicked.
    if submitted:
       devices = ["Phone","Tablet/iPad", "Computer/Laptop", "Headphone/Audio Device", "Video Game Console"]
       amounts = [phone,tablet_iPad,computer_laptop,headphones,video_game_console]
       data = pd.DataFrame({
            "Device": ["Phone","Tablet/iPad", "Computer/Laptop", "Headphone/Audio Device", "Video Game Console"],
            "Amount" :[phone,tablet_iPad,computer_laptop,headphones,video_game_console]
        })


       data = pd.DataFrame({"Device": devices, "Amount": amounts})

       #exists = os.pathexists(fname) and os.path.getsize(fname) > 0

       outfile = open(fname, "w")
       header = outfile.write("Device,Amount\n")
       _ = """
       if not exits:
           outfile.write("Device,Amount\n")
           pd.to_csv(data, index=False)
       """
       i = 0
       while i < len(devices):
           line = str(devices[i]) + "," + str(amounts[i]) + "\n"
           outfile.write(line)
           i += 1
       outfile.close()
        
            
            
        
        # TO DO:
        # 1. Create a new row of data from 'category_input' and 'value_input'.
        # 2. Append this new row to the 'data.csv' file.
        #    - You can use pandas or Python's built-in 'csv' module.
        #    - Make sure to open the file in 'append' mode ('a').
        #    - Don't forget to add a newline character '\n' at the end.

       
        
       st.success("Your data has been submitted!")
       #st.write(f"You entered: **Device:** {categoty_input}, **Amount:** {value_input}")


# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Current Data in CSV")

# Check if the CSV file exists and is not empty before trying to read it.
if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    # Read the CSV file into a pandas DataFrame.
    current_data_df = pd.read_csv('data.csv')
    # Display the DataFrame as a table.
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")
