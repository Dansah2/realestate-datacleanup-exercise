import numpy as np
import pandas as pd


def highest_lowest_cost(df: pd.DataFrame, calc_type: str) -> None:
    """
    Locates the home with the highest cost and prints out the amount and address

    Parameters: 
    df: a dataframe
    calc_type: a string; enter "h" to calculate the highest costing home or "l" 
    to calculate the lowest costing home.

    Returns: None

    Raises:
    ValueError: If the dataframe is empty or the dataframe does not contain the 
    correct columns, or calc_type does not contain the correct string.

    """
    if df.empty:
        print("The DataFrame is empty.")
        return
    
    if 'price' not in df.columns or 'address' not in df.columns:
        print("Either the 'price' / 'address' columns are missing.")
        return
    
    if calc_type not in ["h", "l"]:
        print('You must entera string value for the parameter calc_type; either h for highest price or l for lowest price')
        return
    
    calc_type = calc_type.lower()

    if calc_type == 'h':
        highest_cost_index = df['price'].idxmax()

        address = df.loc[highest_cost_index, 'address']

        price = df.loc[highest_cost_index, 'price']

        print(f"the house with address {address} is the most expensive and its price is {price} USD")
    
    elif calc_type == 'l':
        lowest_cost_index = df['price'].idxmin()

        low_address = df.loc[lowest_cost_index, 'address']

        low_price = df.loc[lowest_cost_index, 'price']

        print(f"the house with address {low_address} is the cheapest and its price is {low_price} USD")


def largest_smallest_home(df: pd.DataFrame, calc_type: str) -> None:
    """
    Locates the largest home and prints out the size and address

    Parameters: 
    df: a dataframe
    calc_type: a string; enter "s" to calculate the smallest home or "l" 
    to calculate the largest home.

    Returns: None

    Raises:
    ValueError: If the dataframe is empty or the dataframe does not contain 
    the correct columns or calc_type is not the correct string value.
    """
    if df.empty:
        print("The DataFrame is empty.")
        return
    if 'price' not in df.columns or 'address' not in df.columns:
        print("Either the 'price' / 'address' columns are missing.")
        return
    if calc_type not in ['s', 'l']:
        print("You must provide one of the following string values for calc_type: l to calculated the largest home and s to calculate the smallest home")
        return
    
    calc_type = calc_type.lower()

    if calc_type == 'l':
        largest_index = df['surface'].idxmax()

        largest_address = df.loc[largest_index, 'address']

        largest_surface = df.loc[largest_index, 'surface']

        print(f"the biggest house is located at {largest_address} and its surface is {largest_surface} meters")

    if calc_type == 's':
        smallest_index = df['surface'].idxmin()

        smallest_address = df.loc[smallest_index, 'address']

        smallest_surface = df.loc[smallest_index, 'surface']

        print(f"the smallest house is located at {smallest_address} and its surface is {smallest_surface} meters")

def pop_mean_price(df: pd.DataFrame, pop_name: str) -> None:
    """
    Calculates the population mean price and prints it to the consol

    Parameters:
    df: Dataframe
    pop_name: Population name

    Returns: None

    Raises: ValueError if the dataframe is empty, or if the population 
    name provided does not exist in the dataset.
    """
    if df.empty:
        print('The Dataframe is empty')
        return
    if pop_name not in df['level5'].values:
        print('The population name provided in not contained in the dataset')
        return

    arro_data = df[df['level5'] == pop_name]
    price_mean = arro_data['price'].mean()
    print(f"{pop_name} mean price: {price_mean}")

def pps(df: pd.DataFrame, pop_name1: str, pop_name2: str) -> None:
    """
    Calculates the price per square meter of a given population.

    Parameters:
    df: Dataframe


    Returns: None

    Raises: ValueError if the Dataframe is empty or if the population 
    name is not inculded in the data. 
    """
    if df.empty:
        print('The Dataframe is empty')
        return
    if pop_name1 not in df['level5'].values:
        print('The first population name provided in not contained in the dataset')
        return
    if pop_name2 not in df['level5'].values:
        print('The second population name provided in not contained in the dataset')
        return
    
    
    pps_data = df[df['level5'].isin([pop_name1, pop_name2])]

    df['pps'] = pps_data['price'] / pps_data['surface']

    pps_1 = df[df['level5'] == pop_name1]['pps'].mean()

    pps_2 = df[df['level5'] == pop_name2]['pps'].mean()

    print(f"The average price per square meter of {pop_name1} is {pps_1} and {pop_name2} is {pps_2}")