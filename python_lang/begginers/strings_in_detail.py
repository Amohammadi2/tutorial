# python strings

#sentence = 'I'm Ashkan Mohammadi'
sentence = 'I\'m Ashkan Mohammadi' # use \ to escape quote
sentence = "I'm Ashkan Mohammadi"  # or use double quotes
print (sentence)



sentence_2 = '"That\'s it", Ashkan said'
print (sentence_2)



sentence_3 = "Hello!\nHow are you?" # use \n to create a new line
sentence_3 = """
Hello
How are you?
"""
print (sentence_3)


first_name = "Ashkan"
last_name = "Mohammadi"
full_name = first_name + ' ' + last_name # concatenation: 'Ashkan' + ' ' + 'Mohammadi' = 'Ashkan Mohammadi'
print (full_name)



new_string = first_name * 5 # multiplication
print (new_string)



string_number = "45"
integer_number = 45
print (string_number * 2)
print (integer_number * 2)


# string subscription
first_character = full_name[0]
second_character = full_name[1]
last_character = full_name[-1]
second_last_character = full_name[-2]

fist_6_characters = full_name[0:6]
fist_6_characters = full_name[:6] # ommited first index defaults to 0

from_character_2_up_to_7 = full_name[1:7] # before 
from_second_character_up_to_end = full_name[1:]  # ommited second index defaults to the size of string

# out_of_range_character = full_name[100]
out_of_range_slice = full_name[45:] # returns an empty string
out_of_range_slice = full_name[:56] # returns the original string 

print (first_character)
print (second_character)
print (last_character)
print (second_last_character)
print (fist_6_characters)
print (from_character_2_up_to_7)
print (from_second_character_up_to_end)



# strings are immutable
original = "original string"
# original[0] = 'm' # trying to change the first character to 'm' will result in an error
another = 'abc' + original[3:] # 'abc' + 'ginal string' = 'abcginal string'

first_name_len = len(first_name) # returns its size
full_name_len = len(full_name)

print(first_name_len)

my_new_first_name = "Ilia"
my_new_full_name = my_new_first_name + full_name[6:] # 'Ilia' + ' Mohammadi' = 'Ilia Mohammadi'

print (my_new_full_name)