import pandas as pd
import numpy as np
import tkVisuals as tkv

compare_value=0
aqiThresh = 151
popThresh = 524500
tphosThresh = 0.05

class Main():
    data = pd.read_csv('data.csv')
    new_columns = {}
    compare_value=0
    
    def population_increase(data):
        change = data['population'].diff()
        average_inc_per_year = change.mean()
        change = pd.Series(change, name="population_change")
        return (change, average_inc_per_year)
    
    def aqi_change(data):
        change = data['aqi'].diff()
        change = pd.Series(change, name="aqi_change")
        return (change)
    
    def water_change(data):
        change = data['tphos'].diff()
        change = pd.Series(change, name="tphos_change")
        return (change)
    
    def safeness_of_water(data):
        safeness = np.where(data['tphos']<0.05, 1, -1)
        safeness = pd.Series(safeness, name="tphos_safe")
        return safeness
    
    def compare_years():
        data = pd.read_csv('data_result.csv')
        years = (int(tkv.input1.get()), int(tkv.input2.get()))
        compare_value = str(tkv.chosenChange.get())
        year1_value = data[compare_value].iloc[years[0]-2043]
        year2_value = data[compare_value].iloc[years[1]-2043]
        # print(year1_value - year2_value)
        compare_value = year2_value - year1_value
        tkv.labelText.set(compare_value)
        # return year1_value - year2_value
    
    def graph_values(property):
        data = pd.read_csv('data_result.csv')
        return data[property].to_list()
    
    def aqi_percentage():
        data = pd.read_csv('data_result.csv')
        aqi_percentage = (data['aqi'].iloc[-1])/aqiThresh
        return aqi_percentage
    def population_percentage():
        data = pd.read_csv('data_result.csv')
        pop_percentage = (data['population'].iloc[-1])/popThresh
        return pop_percentage
    def tphos_percentage():
        data = pd.read_csv('data_result.csv')
        tphos_percentage = (data['tphos'].iloc[-1])/tphosThresh
        return tphos_percentage
    
    new_columns = population_increase(data)[0]
    new_columns = pd.concat([new_columns, aqi_change(data), water_change(data), safeness_of_water(data)], axis=1)
    data = pd.concat([data, new_columns], axis=1)
    
    data.to_csv("data_result.csv")