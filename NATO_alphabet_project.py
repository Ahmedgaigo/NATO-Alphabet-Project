import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# remember when you read the data, it is stored as a DataFrame
nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
dictionary = {row.letter: row.code for (index, row) in nato_data.iterrows()}


def generate_phonetic():
	input_name = input("Enter the name: ").upper()
	try:
		# remember list comprehension
		phonetic = [dictionary[letter] for letter in input_name]
	except KeyError:
		print("Sorry, only letters in the alphabet please.")

		# recursion
		generate_phonetic()
	else:
		print(phonetic)


generate_phonetic()
