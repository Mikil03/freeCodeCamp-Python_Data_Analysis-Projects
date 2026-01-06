import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['bmi'] = df['weight']/ ((df['height']/100)**2)
df['overweight'] = df['bmi'].case_when([(df.bmi > 25, 1),(df.bmi <= 25, 0)])
df.drop('bmi', axis=1, inplace=True)

# 3
df['gluc'] = df['gluc'].case_when([(df['gluc']<=1, 0), (df['gluc']>1, 1)])
df['cholesterol'] = df['cholesterol'].case_when([(df['cholesterol']<=1, 0), (df['cholesterol']>1, 1)])

# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    p = sns.catplot(
        x='variable', 
        y='total', 
        hue='value', 
        col='cardio', 
        data=df_cat, 
        kind='bar',
        height=5,
        aspect=1
    )


    # 8
    fig = p.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo']<=df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(11, 9))

    # 15
    sns.heatmap(
        corr, 
        mask=mask, 
        vmax=.3, 
        center=0,
        square=True, 
        linewidths=.5, 
        cbar_kws={"shrink": .5}, 
        annot=True, 
        fmt='.1f'
    )


    # 16
    fig.savefig('heatmap.png')
    return fig
