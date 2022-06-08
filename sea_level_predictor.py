import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    fig=plt.scatter(x='Year',y= 'CSIRO Adjusted Sea Level',data=df)
    slope, intercept, r, p, se = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x= np.arange(1880,2051)
    plt.plot(x,slope*x+intercept)
    df2=df[df['Year']>=2000]
    slope2, intercept2, r2, p2, se2 = linregress(df2['Year'],df2['CSIRO Adjusted Sea Level'])
    x2= np.arange(2000,2051)
    plt.plot(x2,slope2*x2+intercept2)
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    fig=fig.figure
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()