import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the data
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Streamlit app header
st.title("Bikeshare Data Dashboard")

# Sidebar for selecting visualization
selected_chart = st.sidebar.selectbox(
    "Select Visualization",
    ("Total Rides by Season", "Total Rides by Weather", "Monthly Bike Usage Trend in 2011",
     "Total Rides by Workingday", "Total Rides by Holiday", "Total Rides by Weekday")
)

day_df.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weather',
    'cnt': 'count'
}, inplace=True)

day_df['dateday'] = pd.to_datetime(day_df.dateday)
day_df['season'] = day_df.season.astype('category')
day_df['year'] = day_df.year.astype('category')
day_df['month'] = day_df.month.astype('category')
day_df['holiday'] = day_df.holiday.astype('category')
day_df['weekday'] = day_df.weekday.astype('category')
day_df['workingday'] = day_df.workingday.astype('category')
day_df['weather'] = day_df.weather.astype('category')

day_df.head()

day_df['weather'] = day_df['weather'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})

def find_season(season):
    season_string = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
    return season_string.get(season)

season_list = []

for season in day_df['season']:
    season = find_season(season)
    season_list.append(season)

day_df['season'] = season_list

day_df['month'] = day_df['dateday'].dt.month_name()
day_df['year'] = day_df['dateday'].dt.year

# Visualizations with Streamlit
if selected_chart == "Total Rides by Season":
    st.header("Total Rides by Season")
    seasonly_df = day_df.groupby("season").agg({
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

    # Display the figure using st.pyplot()
    st.pyplot(fig)

elif selected_chart == "Total Rides by Weather":
    st.header("Total Rides by Weather")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=day_df, x="weather", y="count", ax=ax)
    plt.ylabel("Jumlah")
    plt.title("Jumlah peminjaman sepeda yang digunakan berdasarkan cuaca")
    plt.tight_layout()

    # Display the figure using st.pyplot()
    st.pyplot(fig)

elif selected_chart == "Monthly Bike Usage Trend in 2011":
    st.header("Monthly Bike Usage Trend in 2011")
    day_df['month'] = pd.Categorical(day_df['month'], categories=
    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    ordered=True)

    # Filter data hanya untuk tahun 2011
    day_df_2011 = day_df[day_df['dateday'].dt.year == 2011]

    # Menghitung total penggunaan sepeda per bulan
    monthly_total = day_df_2011.groupby(day_df_2011['dateday'].dt.to_period('M'))['count'].sum()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=monthly_total.index.strftime('%B'), y=monthly_total.values, color='blue', marker='o', ax=ax)
    plt.title('Tren Penggunaan Sepeda di Tahun 2011 per Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Pengguna Sepeda')
    plt.tight_layout()

    # Display the figure using st.pyplot()
    st.pyplot(fig)

elif selected_chart == "Total Rides by Workingday":
    st.header("Total Rides by Workingday")
    fig, ax = plt.subplots(figsize=(15, 10))
    sns.barplot(x='workingday', y='count', data=day_df, ax=ax)
    plt.title('Jumlah Pengguna Sepeda berdasarkan Hari Kerja')
    plt.xlabel('Hari Kerja')
    plt.ylabel('Jumlah Pengguna Sepeda')

    # Display the figure using st.pyplot()
    st.pyplot(fig)

elif selected_chart == "Total Rides by Holiday":
    st.header("Total Rides by Holiday")
    fig, ax = plt.subplots(figsize=(15, 10))
    sns.barplot(x='holiday', y='count', data=day_df, ax=ax)
    plt.title('Jumlah Pengguna Sepeda berdasarkan Hari Libur')
    plt.xlabel('Hari Libur')
    plt.ylabel('Jumlah Pengguna Sepeda')

    # Display the figure using st.pyplot()
    st.pyplot(fig)

elif selected_chart == "Total Rides by Weekday":
    st.header("Total Rides by Weekday")
    fig, ax = plt.subplots(figsize=(15, 10))
    sns.barplot(x='weekday', y='count', data=day_df, ax=ax)
    plt.title('Jumlah Pengguna Sepeda berdasarkan Hari dalam Seminggu')
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Jumlah Pengguna Sepeda')

    # Display the figure using st.pyplot()
    st.pyplot(fig)

st.caption('Copyright (c) Buana Dewi 2024')
