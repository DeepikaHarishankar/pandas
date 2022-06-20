
# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
def name():
    user_name = input("Enter a name: ").upper()
    try:
        output = [new_dict[item] for item in user_name]
    except KeyError:
        print('Sorry, only letters in alphabets please')
        name()
    else:
        print(output)
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(new_dict)
name()

