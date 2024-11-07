import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    y1 = pd.Series(range(1880, 2051))
    y2 = pd.Series(range(2000, 2051))
    slope1, intercept1, *_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(y1, y1 * slope1 + intercept1)
    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, *_ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    plt.plot(y2, y2 * slope2 + intercept2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)');
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()