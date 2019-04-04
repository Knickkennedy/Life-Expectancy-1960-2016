import matplotlib.pyplot as plot
import csv

"""
    Author: Knicholas Kennedy
    Purpose of Code:
        To graphically represent life expectancy around the world from the years 1960 to 2016
        This portion of the code generates the graphs that I used to create the gif of information
"""


# A simple wrapper class to store life expectancies during specific years
class Country:
    lifespan = {}
    name = ""

    def __init__(self, name):
        self.name = name
        self.lifespan = {}


countries = []

# Open the information and parse a specific column range
with open('life-expectancy.csv', 'r', encoding='utf-8-sig') as file:
    data = csv.reader(file, delimiter=',')
    for row in data:
        country = Country(row[0].strip())
        year = 1960
        # starting at 1960, collect our information, there are many ways to do this
        for column in range(4, 61):
            try:
                country.lifespan[year] = float(row[column])
            except NameError:
                country.lifespan[year] = 0.0
            year = year + 1
        countries.append(country)

# Python range is exclusive on upper bound so we run to 2017
for i in range(1960, 2017):
    country_names = []
    life = []
    x = 0
    # Get our initial plot for each range
    fig, ax = plot.subplots(figsize=(50, 25))
    ax.set_title(i)
    for country in countries:
        life.append(country.lifespan[i])
        country_names.append(country.name)
        plot.bar(x, country.lifespan[i], width=0.6, tick_label=country.name)
        x = x + 1

    x_values = [i for i in range(len(country_names))]

    # Save the files without opening them to save time
    # I use a common naming convention of the years, but you can use whatever is necessary for your project
    plot.xticks(x_values, country_names, fontsize=8, rotation=90)
    plot.tight_layout()
    plot.ylim(0, 100)
    filename = str(i) + '.png'
    plot.savefig(filename, dpi='figure', quality=95)
    plot.show(block=False)
