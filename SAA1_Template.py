# Import the required modules
import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file into dataframe 'df'
df = pd.read_csv(filepath_or_buffer = "                       ")

# Extract the column 'Year' from dataframe 'df'
year = df['          ']

# Extract the column 'Facebook' from dataframe 'df'
fb = df['           ']

# Extract the column 'Twitter' from dataframe 'df'
twitter = df['          ']

# Set the figsize
plt.figure(figsize = (16, 5))

# Plot the bar graphs for growth in facebook users 
plt.       (year, fb, label = 'Facebook', marker = 'o')

# Plot the bar graphs for growth in twitter users
plt.       (year, twitter, label = 'Twitter', marker = 'o')

# Set the title of the graph
plt.title("Number of people using social media platforms, 2010 to 2019")

# Set the labels for x and y-axes
plt.xlabel("Population in bilion")
plt.ylabel("Year")

# Show labels with legend
plt.legend()

# Set the values for x-axis 
plt.xticks(ticks = year , labels= year)

# Display the graph
plt.show()

