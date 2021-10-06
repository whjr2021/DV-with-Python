# Import the required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the csv file into dataframe 'df'
df = pd.read_csv(filepath_or_buffer = "https://github.com/whjr2021/DV-with-Python/blob/main/TA2_olympic_medals.csv?raw=true", encoding='latin-1')

# Extract the column values from df from top 10 rows
country_name = df['Country_Name'][:10]
gold_medals = df['Gold'][:10]
silver_medals = df['Silver'][:10]
bronze_medals = df['Bronze'][:10]

# Set values for x-axis. This will give an array of numbers 0 to 9.
bar_1 = np.arange(len(country_name))

# Set width of the bars
bar_width = 0.25

# Set the figsize
plt.figure(figsize = (20, 6))

# Plot the bar graphs for gold, silver and bronze medals for top 10 countries
plt.bar(x = bar_1, height = gold_medals, width = bar_width, label = 'Gold')
plt.bar(x = bar_1 + bar_width, height = silver_medals, width = bar_width, label = 'Silver')
plt.bar(x = bar_1 + (2*bar_width), height = bronze_medals, width = bar_width, label = 'Bronze')

# Change the x-axis values to country names
plt.xticks(ticks = bar_1 + bar_width, labels = country_name)

# Set the title of the graph
plt.title("Medals by Countries in Tokyo Olympics 2021")

# Set the labels for x and y-axes
plt.xlabel("Country")
plt.ylabel("Count of Medals Won")

# Show labels with legend
plt.legend()

# Display the graph
plt.show()
