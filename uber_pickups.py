import streamlit as st  # Streamlit for building the web app
import pandas as pd  # Pandas for data manipulation
import numpy as np  # NumPy for numerical operations (not used in this script but imported for potential future use)

# Set the title of the Streamlit app
st.title('Uber pickups in NYC')

# Define constants
DATE_COLUMN = 'date/time'  # Column name for date/time in the dataset
DATA_URL = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'  # URL of the dataset

@st.cache_data  # Cache the function to avoid reloading data on every run
# This decorator helps to speed up the app by caching the results of the function
# The cached data will be used if the function is called with the same parameters again
def load_data(nrows):
    """
    Load data from the specified URL and preprocess it.

    Args:
        nrows (int): Number of rows to read from the dataset.

    Returns:
        pd.DataFrame: Preprocessed data with lowercase column names and parsed date/time column.
    """
    # Read the dataset from the URL, limiting to `nrows` rows
    data = pd.read_csv(DATA_URL, nrows=nrows)
    
    # Convert column names to lowercase for consistency
    def lowercase(x):
        return str(x).lower()
    
    # Apply the lowercase function to all column names
    # This is done to ensure that all column names are in lowercase
    # This is important for consistency and to avoid case sensitivity issues
    # when accessing the columns later in the code
    # The `axis='columns'` argument specifies that we are applying the function to the column names
    # The `inplace=True` argument modifies the DataFrame in place without creating a copy
    data.rename(lowercase, axis='columns', inplace=True)
    
    # Convert the date/time column to datetime format for easier manipulation
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    
    return data

# Display a loading message in the Streamlit app
load_data_state = st.text('Loading data...')

# Load the first 10,000 rows of data
data = load_data(10000)

# Update the loading message to indicate completion
load_data_state.text('Data loaded! (Using st.cache_data)')

if st.checkbox('Show raw data'):
    # If the checkbox is checked, display the raw data
    st.subheader('Raw data')
    st.write(data)  # Display the raw data in the app


st.subheader('Number of pickups by hour')
# Create a histogram of the number of pickups by hour
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
# Create a bar chart to visualize the histogram values
st.bar_chart(hist_values)  # Display the histogram as a bar chart

st.subheader('Map of all pickups')
st.map(data)  # Display a map with all the pickup locations


st.subheader('Pickups by hour')
hour_to_filter = st.slider('hour', 0, 23, 17) # Create a filter to select data for the specified hour
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
# Display the filtered data in the app
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)  # Display a map with the filtered pickup locations


