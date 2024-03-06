import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the data
all_data_df = pd.read_csv("all_data.csv")

# Function to plot Total Rides by Season
def total_rides_by_season():
    st.header("Total Rides by Season")
    seasonly_df = all_data_df.groupby("season").agg({
        "casual": "sum",
        "registered": "sum",
        "count": "sum"
    })
    seasonly_df = seasonly_df.reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    season_order = ['Spring', 'Summer', 'Fall', 'Winter']
    sns.barplot(x="season", y="count", data=seasonly_df, order=season_order, ax=ax)
    plt.xlabel("Season")
    plt.ylabel("Total Rides")
    plt.title("Count of bikeshare rides by Season")
    st.pyplot(fig)

# Function to plot Total Rides by Weather
def total_rides_by_weather():
    st.header("Total Rides by Weather")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=all_data_df, x="weather", y="count", ax=ax)
    plt.ylabel("Jumlah")
    plt.title("Jumlah peminjaman sepeda yang digunakan berdasarkan cuaca")
    plt.tight_layout()
    st.pyplot(fig)

# Function to plot Monthly Bike Usage Trend in 2011
def monthly_bike_usage_trend_2011():
    st.header("Monthly Bike Usage Trend in 2011")
    all_data_df['dateday'] = pd.to_datetime(all_data_df['dateday'])
    day_df_2011 = all_data_df[all_data_df['dateday'].dt.year == 2011]
    monthly_total = day_df_2011.groupby(day_df_2011['dateday'].dt.to_period('M'))['count'].sum()
    monthly_total.index = monthly_total.index.strftime('%B')  # Convert PeriodIndex to string
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=monthly_total.index, y=monthly_total.values, color='blue', marker='o', ax=ax)
    plt.title('Tren Penggunaan Sepeda di Tahun 2011 per Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Pengguna Sepeda')
    plt.tight_layout()
    st.pyplot(fig)

# Function to plot Total Rides by Workingday
def total_rides_by_workingday():
    st.header("Total Rides by Workingday")
    fig, ax = plt.subplots(figsize=(15, 10))
    sns.barplot(x='workingday', y='count', data=all_data_df, ax=ax)
    plt.title('Jumlah Pengguna Sepeda berdasarkan Hari Kerja')
    plt.xlabel('Hari Kerja')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(fig)

# Function to plot Total Rides by Holiday
def total_rides_by_holiday():
    st.header("Total Rides by Holiday")
    fig, ax = plt.subplots(figsize=(15, 10))
    sns.barplot(x='holiday', y='count', data=all_data_df, ax=ax)
    plt.title('Jumlah Pengguna Sepeda berdasarkan Hari Libur')
    plt.xlabel('Hari Libur')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(fig)

# Function to plot Total Rides by Weekday
def total_rides_by_weekday():
    st.header("Total Rides by Weekday")
    fig, ax = plt.subplots(figsize=(15, 10))
    sns.barplot(x='weekday', y='count', data=all_data_df, ax=ax)
    plt.title('Jumlah Pengguna Sepeda berdasarkan Hari dalam Seminggu')
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(fig)

# Streamlit app header
st.title("Bikeshare Data Dashboard")

# Sidebar for selecting visualization
selected_chart = st.sidebar.selectbox(
    "Select Visualization",
    ("Total Rides by Season", "Total Rides by Weather", "Monthly Bike Usage Trend in 2011",
     "Total Rides by Workingday", "Total Rides by Holiday", "Total Rides by Weekday")
)

# Display selected visualization
if selected_chart == "Total Rides by Season":
    total_rides_by_season()
elif selected_chart == "Total Rides by Weather":
    total_rides_by_weather()
elif selected_chart == "Monthly Bike Usage Trend in 2011":
    monthly_bike_usage_trend_2011()
elif selected_chart == "Total Rides by Workingday":
    total_rides_by_workingday()
elif selected_chart == "Total Rides by Holiday":
    total_rides_by_holiday()
elif selected_chart == "Total Rides by Weekday":
    total_rides_by_weekday()

st.caption('Copyright (c) Buana Dewi 2024')
