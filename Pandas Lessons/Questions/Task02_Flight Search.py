import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/flights.csv")

print(df.columns)

while True:
    date = input("Enter the date from 01/04/22 - 29/06/22 (DD-MM-YYYY): ")
    from_location = input("Enter departure location: ").strip()
    to_location = input("Enter destination: ").strip().upper()
    time_period = input("Enter time period (AM/PM): ").strip().upper()
    
    if date not in df['Date'].values:
        print("No flights available for the date entered, please enter the right dates.")
        continue
    
    # Filter the DataFrame based on user inputs
    filtered_df = df[(df['Date'] == date) & 
                     (df['From'] == from_location) & 
                     (df['To'] == to_location) & 
                     (df['TimePeriod'] == time_period)]
    
    if filtered_df.empty:
        print("No flights match your search criteria.")
    else:
        print("Available flights:")
        print(filtered_df)
    
    # Option to exit the loop
    exit_choice = input("Do you want to search for another flight? (yes/no): ").strip().lower()
    if exit_choice != 'yes':
        break