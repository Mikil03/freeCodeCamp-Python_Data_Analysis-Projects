import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date']).set_index('date')

# Clean data
df = df[(df['value']>df['value'].quantile(0.025)) & (df['value']<df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20, 5))
    ax.plot(df.index, df['value'], color='red')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()


    # Draw bar plot
    miss_data = pd.DataFrame({'date':['2016-01-01', '2016-02-01', '2016-03-01', '2016-04-01'], 'value':[0,0,0,0]})
    miss_data['date'] = pd.to_datetime(miss_data['date'])
    miss_data.set_index('date', inplace=True)
    df_bar = pd.concat([miss_data, df_bar])
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.barplot(data=df_bar, 
                x='year', 
                y='value', 
                hue='month', 
                hue_order=months, 
                palette='tab10',
                errorbar=None,
                ax=ax)

    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend().set_title('Month')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2, figsize=(25,8))

    sns.boxplot(data=df_box, 
                x='year', 
                y='value', 
                ax=ax[0],
                palette='tab10')

    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')

    sns.boxplot(data=df_box, 
                x='month', 
                y='value', 
                ax=ax[1],
                palette='tab10',
                order=months)
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
