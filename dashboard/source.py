import numpy as np
import pandas as pd
import os
 
# get current directory
path = os.path.join(os.getcwd(), 'all_data.csv')
all_data = pd.read_csv(path)

# convert month name function
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
def number_to_month(month_number):
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return month_names[month_number - 1]

def month_to_number(month_name):
    month_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return month_numbers[month_names.index(month_name)]

# ambil label tahun
def get_year(df):
    years = df['year'].unique()
    return years

# ambil data bulan dari df
def get_month(df, year):
    years_df = df[df['year'] == year]
    months = sorted(years_df['month'].unique())
    months = [number_to_month(month) for month in months]
    return months

# ambil data stasiun
def get_station(df):
    station = df['station'].unique()
    return station

# ambil list polusi
def get_pollutan():
    return ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]

# dashboard needeed
# ambil rata-rata polusi kendaraan
def average_vehicle(df, year, station):
    new_df = df[(df['year'] == year) & (df['station'] == station)]
    average = new_df.agg({
        'vehicle_pollution': 'mean'
    })
    return round(average, 2)

# rata rata polusi industri
def average_industry(df, year, station):
    new_df = df[(df['year'] == year) & (df['station'] == station)]
    average = new_df.agg({
        'industrial_pollution': 'mean'
    })
    return round(average, 2)

# rata rata temperatur
def dashboard_bar(df, year, station):
    new_df = df[(df['year'] == year) & (df['station'] == station)]
    new_df = new_df.rename(columns={"TEMP": "temp", "WSPM": "wind"})
    average = new_df.agg({
        'temp': 'mean',
        'wind': 'mean'
    })
    return round(average, 2)

# ambil rata-rata polusi kendaraan pertahun
def get_average_vehicle_by_year(df, year, station):
    new_df = df[(df['year'] == year) & (df['station'] == station)]
    average_vehicle = new_df.groupby(by=['month']).agg({
        'vehicle_pollution': 'mean'
    })  
    average_vehicle.index = [number_to_month(month) for month in average_vehicle.index]
    average_vehicle.reset_index(drop=True)
    return round(average_vehicle, 2)

# ambil rata-rata polusi industri
def get_average_industry_by_year(df, year, station):
    new_df = df[(df['year'] == year) & (df['station'] == station)]
    average_pollution = new_df.groupby(by='month').agg({
        'industrial_pollution': 'mean'
    })
    average_pollution.index = [number_to_month(month) for month in average_pollution.index]
    return round(average_pollution, 2)

# rata-rata pollutan
def pollutan_by_year(df, station, year):
    new_df = df[(df['station'] == station) & (df['year'] == year)]
    pollutan = new_df.agg({
        "PM2.5": "mean",
        "PM10": "mean",
        "SO2": "mean",
        "NO2": "mean",
        "CO": "mean",
        "O3": "mean"
    }).sort_values(ascending=False)
    
    return round(pollutan, 2)

# by yearly
# yearly pollutan
def yearly_pollution(df, station, year):
    new_df = df[(df['station'] == station) & (df['year'] == year)]
    pollutan = new_df.groupby(by='month').agg({
        "PM2.5": "mean",
        "PM10": "mean",
        "SO2": "mean",
        "NO2": "mean",
        "CO": "mean",
        "O3": "mean"
    })
    pollutan.index = [number_to_month(month) for month in pollutan.index]
    return round(pollutan, 2)

# bar yearly
def yearly_bar(df, station, year):
    new_df = df[(df['station'] == station) & (df['year'] == year)]
    new_df = new_df.rename(columns={"TEMP": "temp", "RAIN": "rain", "WSPM": "wind"})
    info = new_df.agg({
        'temp': 'mean',
        'rain': 'mean',
        'wind': 'mean'
    })
    return round(info.temp, 1), round(info.rain, 3), round(info.wind, 1)


# by month
# monthly pollutan
def monthly_pollutan(df, station, year, month):
    # convert name to number
    month = month_to_number(month)
    new_df = df[(df['station'] == station) & (df['year'] == year) & (df['month'] == month)]
    pollutan = new_df.groupby(by='day').agg({
        "PM2.5": "mean",
        "PM10": "mean",
        "SO2": "mean",
        "NO2": "mean",
        "CO": "mean",
        "O3": "mean"
    })
    return round(pollutan, 2)

def monthly_bar(df, station, year, month):
    # convert name to number
    month = month_to_number(month)
    
    new_df = df[(df['station'] == station) & (df['year'] == year) & (df['month'] == month)]
    new_df = new_df.rename(columns={"TEMP": "temp", "RAIN": "rain", "WSPM": "wind"})
    info = new_df.agg({
        'temp': 'mean',
        'rain': 'mean',
        'wind': 'mean'
    })
    return round(info.temp, 1), round(info.rain, 3), round(info.wind, 1)

