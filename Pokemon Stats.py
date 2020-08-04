import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.offline as ply
import plotly.express as px


pokemon = pd.read_csv('Pokemon.csv')
pokemon = pokemon.drop('#', axis=1)

pokemon['Type 2'] = pokemon['Type 2'].fillna(pokemon['Type 1'], inplace=True)
pokemon['Name'] = pokemon['Name'].str.replace(".*(?=Mega)","")

def Pie():
    labels = pokemon['Type 1'].value_counts()
    labels.plot(kind='pie', autopct='%1.1f%%', pctdistance=1.0)
    plt.show()
#print(Pie())

def Distributions():
    health = sns.distplot(pokemon['HP'])
    plt.show()
    attack = sns.distplot(pokemon['Attack'])
    plt.show()
    defense = sns.distplot(pokemon['Defense'])
    plt.show()
#print(Distributions())

def Legendary():
    sns.countplot(pokemon['Legendary'])
    plt.show()
    sns.boxplot(x=pokemon['Legendary'], y=pokemon['Attack'])
    plt.show()
    sns.lmplot(x='Attack',y='Defense', hue='Legendary', fit_reg=False, data=pokemon, markers=['x','o'])
    plt.show()
#print(Legendary())

def LegendByGen():
    Legnedary_index = pokemon.groupby('Generation').sum().Legendary.index
    Legnedary_values = pokemon.groupby('Generation').sum().Legendary.values
    sns.barplot(x=Legnedary_index, y=Legnedary_values)
    plt.show()
#print(LegendByGen())

def LegendByType():
    type_index = pokemon.groupby('Type 1').sum().Legendary.sort_values(ascending=False).index
    type_vals = pokemon.groupby('Type 1').sum().Legendary.sort_values(ascending=False).values
    sns.barplot(x=type_index,y=type_vals)
    plt.show()
#print(LegendByType())

def Correlation():
    labels = pokemon[['Name','Type 1', 'Type 2','Total', 'HP', 'Attack', 'Defense','Sp. Atk','Sp. Def','Speed', 'Generation',
                      'Legendary']]
    matrix = sns.heatmap(labels.corr(), annot=True)
    plt.show()
#print(Correlation())


def pokemonStat():
    stat = pokemon[pokemon['Name'] == 'Blastoise']
    data = [go.Scatterpolar(r=[stat['HP'].values[0], stat['Attack'].values[0], stat['Defense'].values[0],
                               stat['Sp. Atk'].values[0], stat['Sp. Def'].values[0], stat['Speed'].values[0]],
                            theta = ['HP','Attack','Defense','Sp. Atk','Sp. Defense','Speed'],
                            fill='toself')]
    layout = go.Layout(polar= dict(radialaxis=dict(visible=True, range=[0,250])),showlegend=False, title="Blastoise's Stats")
    fig = go.Figure(data=data, layout=layout)
    fig.show()
#print(pokemonStat())

def CharizardStat():
    stat = pokemon[pokemon['Name'] == 'Charizard']
    data = [go.Scatterpolar(r=[stat['HP'].values[0], stat['Attack'].values[0], stat['Defense'].values[0],
                               stat['Sp. Atk'].values[0], stat['Sp. Def'].values[0], stat['Speed'].values[0]],
                            theta=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Defense', 'Speed'],
                            fill='toself')]
    layout = go.Layout(polar=dict(radialaxis=dict(visible=True, range=[0, 250])), showlegend=False,
                       title="Charizard's Stats")
    fig = go.Figure(data=data, layout=layout)
    fig.show()
#print(CharizardStat())

def FireScatter():
    Gen1Attack = pokemon['Attack'][pokemon['Type 1'] == 'Fire'][pokemon['Generation'] == 1]
    Gen1Defense = pokemon['Defense'][pokemon['Type 1'] == 'Fire'][pokemon['Generation'] == 1]
    Names = pokemon['Name'][pokemon['Type 1'] == 'Fire'][pokemon['Generation'] == 1]
    scatter = px.scatter(x=Gen1Defense, y=Gen1Attack, text=Names)
    scatter.show()
#print(FireScatter())

def WaterScatter():
    Gen1Attack = pokemon['Attack'][pokemon['Type 1'] == 'Water'][pokemon['Generation'] == 1]
    Gen1Defense = pokemon['Defense'][pokemon['Type 1'] == 'Water'][pokemon['Generation'] == 1]
    Names = pokemon['Name'][pokemon['Type 1'] == 'Water'][pokemon['Generation'] == 1]
    water_Scatter = px.scatter(x=Gen1Defense,y=Gen1Attack, text=Names)
    water_Scatter.show()
#print(WaterScatter())

def GrassScatter():
    Gen1Attack = pokemon['Attack'][pokemon['Type 1']=='Grass'][pokemon['Generation']==1]
    Gen1Defense = pokemon['Defense'][pokemon['Type 1']=='Grass'][pokemon['Generation']==1]
    Names = pokemon['Name'][pokemon['Type 1']=='Grass'][pokemon['Generation']==1]
    grass_scatter = px.scatter(x=Gen1Defense,y=Gen1Attack, text=Names)
    grass_scatter.show()
#print(GrassScatter())

def OverallCount():
    count = sns.countplot(pokemon['Type 1'])
    count.set_xticklabels(count.get_xticklabels(),rotation=90)
    plt.show()
#print(OverallCount())

def GenerationCount():
    sns.countplot(pokemon['Generation'])
    plt.show()
#print(GenerationCount())

def Gen1Plot():
    water = pokemon[(pokemon['Type 1'] == 'Water')][pokemon['Generation'] == 1]
    fire = pokemon[(pokemon['Type 1'] == 'Fire')][pokemon['Generation'] == 1]
    grass = pokemon[(pokemon['Type 1'] == 'Grass')][pokemon['Generation'] == 1]
    Normal = pokemon[(pokemon['Type 1'] == 'Normal')][pokemon['Generation'] == 1]
    Psychic = pokemon[(pokemon['Type 1'] == 'Psychic')][pokemon['Generation'] == 1]
    Bug = pokemon[(pokemon['Type 1'] == 'Bug')][pokemon['Generation'] == 1]
    sns.set(style='whitegrid')
    plt.scatter(water['Attack'], water['Defense'], color='b', s=20, label='Water')
    plt.scatter(grass['Attack'], grass['Defense'], color='g', s=20, label='Grass')
    plt.scatter(fire['Attack'], fire['Defense'], color='r', s=20, label='Fire')
    plt.scatter(Normal['Attack'], Normal['Defense'], color='y', s=20, label='Normal')
    plt.scatter(Psychic['Attack'], Psychic['Defense'], color='violet', s=20, label='Psychic')
    plt.scatter(Bug['Attack'], Bug['Defense'], color='seagreen', s=20, label='Bug')
    plt.legend()
    plt.show()
#print(Gen1Plot())


def FireGen():
    fireGen1 = pokemon[(pokemon['Type 1']=='Fire')][pokemon['Generation']==1]
    fireGen2 = pokemon[(pokemon['Type 1'] == 'Fire')][pokemon['Generation']==2]
    fireGen3= pokemon[(pokemon['Type 1'] =='Fire')][pokemon['Generation']==3]
    fireGen4 = pokemon[(pokemon['Type 1']=='Fire')][pokemon['Generation']==4]
    fireGen5 = pokemon[(pokemon['Type 1']=='Fire')][pokemon['Generation']==5]
    fireGen6 = pokemon[(pokemon['Type 1']=='Fire')][pokemon['Generation']==6]
    plt.scatter(fireGen1['Attack'], fireGen1['Defense'], color='b', s=20, label='Generation 1')
    plt.scatter(fireGen2['Attack'], fireGen2['Defense'], color='g', s = 20, label='Generation 2')
    plt.scatter(fireGen3['Attack'], fireGen3['Defense'], color='r', s = 20, label='Generation 3')
    plt.scatter(fireGen4['Attack'], fireGen4['Defense'], color='y', s=20, label='Generation 4')
    plt.scatter(fireGen5['Attack'], fireGen5['Defense'], color='violet', s=20, label='Generation 5')
    plt.scatter(fireGen6['Attack'], fireGen6['Defense'], color='pink', s=20, label='Generation 6')
    plt.legend()
    plt.xlabel('Attack')
    plt.ylabel('Defense')
    plt.show()
#print(FireGen())

def WaterGen():
    WaterGen1 = pokemon[(pokemon['Type 1'] == 'Water')][pokemon['Generation'] == 1]
    WaterGen2 = pokemon[(pokemon['Type 1'] == 'Water')][pokemon['Generation'] == 2]
    WaterGen3 = pokemon[(pokemon['Type 1'] == 'Water')][pokemon['Generation'] == 3]
    WaterGen4 = pokemon[(pokemon['Type 1'] == 'Water')][pokemon['Generation'] == 4]
    WaterGen5 = pokemon[(pokemon['Type 1'] == 'Water')][pokemon['Generation'] == 5]
    WaterGen6 = pokemon[(pokemon['Type 1'] == 'Water')][pokemon['Generation'] == 6]
    plt.scatter(WaterGen1['Attack'], WaterGen1['Defense'], color='b', s=20, label='Generation 1')
    plt.scatter(WaterGen2['Attack'], WaterGen2['Defense'], color='g', s=20, label='Generation 2')
    plt.scatter(WaterGen3['Attack'], WaterGen3['Defense'], color='r', s=20, label='Generation 3')
    plt.scatter(WaterGen4['Attack'], WaterGen4['Defense'], color='y', s=20, label='Generation 4')
    plt.scatter(WaterGen5['Attack'], WaterGen5['Defense'], color='violet', s=20, label='Generation 5')
    plt.scatter(WaterGen6['Attack'], WaterGen6['Defense'], color='pink', s=20, label='Generation 6')
    plt.legend()
    plt.xlabel('Attack')
    plt.ylabel('Defense')
    plt.show()
#print(WaterGen())


def BoxPlot():
    plt.subplots(figsize=(15,5))
    sns.boxplot(x='Type 1', y='Attack', data=pokemon)
    plt.show()
    sns.boxplot(x='Type 1', y = 'Total', data=pokemon)
    plt.show()
    sns.boxplot(x='Type 1',y='Speed', data=pokemon)
    plt.show()
#print(BoxPlot())

def Swarm():
    sns.swarmplot(x='Type 1', y='Attack', data=pokemon)
    plt.show()
    sns.swarmplot(x='Type 1', y='Defense',data=pokemon)
    plt.show()
#print(Swarm())

def StatsByGen():
    stats = pokemon.groupby('Generation').mean()[['Attack', 'Defense', 'HP', 'Sp. Atk', 'Sp. Def', 'Speed']]
    stats.plot.line()
    plt.show()
#print(StatsByGen())

def AtackVsDef():
    sns.scatterplot(x='Defense',y='Attack',data=pokemon)
    plt.show()
#print(AtackVsDef())
