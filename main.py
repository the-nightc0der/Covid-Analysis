import pandas as pd
import matplotlib.pyplot as plt

# Load the COVID-19 time series data from a CSV file
df = pd.read_csv('WHO-COVID-19-global-data.csv', parse_dates=['Date_reported'])

# Group the data by date and calculate the total number of cases and deaths
daily_cases = df.groupby(['Date_reported']).sum()['New_cases']
daily_deaths = df.groupby(['Date_reported']).sum()['New_deaths']
# Calculate the 7-day rolling average of cases and deaths
rolling_cases = daily_cases.rolling(window=15).mean()
rolling_deaths = daily_deaths.rolling(window=15).mean()

# Plot the daily cases and deaths, along with the rolling averages
plt.plot(daily_cases.index, daily_cases, label='New_cases')
plt.plot(daily_deaths.index, daily_deaths, label='New_deaths')
plt.plot(rolling_cases.index, rolling_cases, label='7-Day Rolling Average Cases')
plt.plot(rolling_deaths.index, rolling_deaths, label='7-Day Rolling Average Deaths')

# Add labels and a legend to the plot
plt.xlabel('Date')
plt.ylabel('Number of Cases/Deaths')
plt.title('Pandemic Outbreak Time series analysis for Covid-19  ')
plt.legend()

# Show the plot
plt.show()
