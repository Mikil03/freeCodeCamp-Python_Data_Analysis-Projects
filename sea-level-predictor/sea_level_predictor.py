import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    best_fit_1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    df_pred = pd.DataFrame({'Year':list(range(1880, 2051, 1))})
    df_pred['pred_sea_level'] = best_fit_1.slope * df_pred['Year'] + best_fit_1.intercept
    plt.plot(df_pred['Year'], df_pred['pred_sea_level'], color = 'red', linewidth = 3)


    # Create second line of best fit
    best_fit_2 = linregress(df[df['Year'] > 1999]['Year'], df[df['Year'] > 1999]['CSIRO Adjusted Sea Level'])
    df_pred2 = pd.DataFrame({'Year':list(range(2000, 2051, 1))})
    df_pred2['pred_sea_level'] = best_fit_2.slope * df_pred2['Year'] + best_fit_2.intercept
    plt.plot(df_pred2['Year'], df_pred2['pred_sea_level'], color = 'yellow', linewidth = 3)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()