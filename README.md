# Coursera Capstone Project

# Introduction

For my *Capstone project* I will help an investor who is about to start a business of importing and selling **BIO: vegetables** and  **fruits**.


# Description and background

In the past few years my client have tried to start his dream business but he failed many times. So this time he consulted me for help and as a data scientist I decided to start by describing my approach.
- **NB**: our client wants to open his Bio store  in **Paris city** but no matter which neighbourhood.

1. **First**: we will search a list of all paris neighbourhoods.
2. **Second**: we will sort all neighbourhoods by the number of restaurants and fast foods
3. Then the **Third** step: is to inverse sort neighbourhoods by the number of store and super markets

# Data of our project

## Paris neighbourhoods data
To derive our solution, We leverage JSON data available at  the french government website: [https://www.data.gouv.fr/fr/datasets/r/e88c6fda-1d09-42a0-a069-606d3259114e](https://www.data.gouv.fr/fr/datasets/r/e88c6fda-1d09-42a0-a069-606d3259114e)

The JSON file has data about all the neighbourhoods in **France**; we will limit it to Paris using department code = 75.
columns we will be using are:
1.  _postal_code_: Postal codes for France
2.  _nom_comm_: Name of Neighborhoods in France
3.  _nom_dept_: Name of the boroughs, equivalent to towns in France
4.  _geo_point_2d_: Tuple containing the latitude and longitude of the Neighborhoods.

## Foursquare API
In this next step we will be using **Foursquare** data api to search for the number of restaurant in every **Paris** area.
And to have better idea on our concurrents we will look for the number of **stores** or **super markets** in all those areas

# Final Step
After all those researches we will provide to our client a list of all neighbourhoods with more restaurants and less concurrency and of course the results will be sorted and we let our customer choose were he will be openning his business
