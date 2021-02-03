import pandas as pd
import math as math

def handle_alphabets(string):
    new_one = string
    for position in range(len(string)):
        if string[position].isalpha() or (string[position] == ':') or (string[position] == '-') \
                or (string[position] == ',') or (string[position] == '/') or (string[position] == " "):
            character = string[position]
            new_one = new_one.replace(character, "")
    return new_one

def calculate_the_mean(string):
    new_one = string[1:]
    if '$' in new_one:
        number = new_one.split('$')
        return (int(number[0]) + int(number[1])) / 2
    return new_one

def clean_up_characters(string):
    new_one = str(string)[:-2]
    return new_one


if __name__ == '__main__':


    dataframe = pd.read_csv("data/scraped_real_estate.csv")
    
    for i in range(239):
        dataframe.at[i, 'Price'] = handle_alphabets(dataframe.at[i, 'Price'])
        dataframe.at[i, 'Price'] = calculate_the_mean(dataframe.at[i, 'Price'])
        dataframe.at[i, 'Lot area'] = clean_up_characters(dataframe.at[i, 'Lot area'])
        dataframe.at[i, 'Lot area'] = handle_alphabets(dataframe.at[i, 'Lot area'])

    dataframe.to_csv(path_or_buf="processed_data.csv")

    dataframe = pd.read_csv("data/processed_data_nsw_dataset.csv")

    for i in range(239):
        if not(dataframe.at[i, 'Price'] >= 1):
            dataframe.drop(i, inplace=True)

    dataframe = pd.read_csv('data/processed_nsw_dataset.csv')

    for i in range(223):
        if math.isnan(dataframe.at[i, 'Lot area']) or not(dataframe.at[i, 'Lot area'] >= 1):
            dataframe.drop(i, inplace=True)

    dataframe["Type"] = dataframe["Type"].map({
        'Vacant land' : 0,
        'Apartment / Unit / Flat' : 1,
        'Semi-Detached' : 2,
        'House' : 3,
        'New House & Land' : 4,
        'Duplex' : 5,
        'Villa' : 6
    })

    dataframe.to_csv('fully_processed_and_mapped_nsw.csv')










