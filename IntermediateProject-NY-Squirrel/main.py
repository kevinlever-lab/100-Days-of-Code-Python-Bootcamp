import pandas
"""
Central Park Squirrel Census - Fur Colour Counter

A data analysis script that processes the 2018 Central Park Squirrel
Census dataset to count the number of squirrels observed for each
primary fur colour and saves the results to a new CSV file.

Process:
    1. Reads the 2018 Central Park Squirrel Census CSV data file into
       a pandas DataFrame.
    2. Initialises a dictionary to store the fur colour counts for
       three categories: grey, red (cinnamon), and black.
    3. Counts the number of unique squirrel IDs for each fur colour:
          - Black:    Squirrels with 'Black' primary fur colour.
          - Cinnamon: Squirrels with 'Cinnamon' primary fur colour,
                      mapped to 'red' in the output.
          - Gray:     Squirrels with 'Gray' primary fur colour,
                      mapped to 'grey' in the output.
    4. Stores the counts in the data dictionary and prints each
       colour count to the console.
    5. Converts the results dictionary to a pandas DataFrame and
       saves it to a new CSV file named 'squirrel_colour_count.csv'.

Input:
    2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv:
        The raw squirrel census dataset containing squirrel observations
        with columns for 'Primary Fur Color' and 'Unique Squirrel ID'.

Output:
    squirrel_colour_count.csv:
        A CSV file containing two columns:
            - Fur Color: The fur colour category (grey, red, black).
            - Count:     The number of squirrels observed for each
                         fur colour.

Dependencies:
    pandas: Used to read the CSV data file, filter and count squirrel
            records by fur colour, convert the results dictionary to
            a DataFrame, and save the output to a new CSV file.
"""
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# group by the squirrel colour and count the number of unique squirrel IDs of each colour
# count_colour = data.groupby("Primary Fur Color")['Unique Squirrel ID'].count()
# print(count_colour)

#Create a dictionary to store the resulting output in the format required
data_count ={
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [0, 0, 0]
}

#Count each colour
squirrel_count = data[data["Primary Fur Color"] == "Black"]['Unique Squirrel ID'].count()
data_count['Count'][2] = squirrel_count.item()
print(f"Black squirrels: {squirrel_count}")
squirrel_count = data[data["Primary Fur Color"] == "Cinnamon"]['Unique Squirrel ID'].count()
data_count['Count'][1] = squirrel_count.item()
print(f"Red squirrels: {squirrel_count}")
squirrel_count = data[data["Primary Fur Color"] == "Gray"]['Unique Squirrel ID'].count()
data_count['Count'][0] = squirrel_count.item()
print(f"Grey squirrels: {squirrel_count}")
print(data_count)

#Convert the dictionary to a pandas DataFrame
dataf = pandas.DataFrame(data_count)
print(dataf)

#Save DataFrame to csv file
dataf.to_csv("squirrel_colour_count.csv")


