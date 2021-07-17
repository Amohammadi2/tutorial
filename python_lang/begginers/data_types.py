# Tutorial

# [python numeric data types]
# 10 : int
# 20.5465 : float



# [python strings]
# "Ashkan Mohammadi" : str
# 'Ashkan Mohammadi' : str
# ''' Ashkan Mohammadi ''' : str
# """ Ashkan Mohammadi """ : str



# [python variable declration]
a = 10
b = 20.5465
full_name = "Ashkan Mohammadi"


# [python arithmatics]
# 20 + 30 # addition
# 50 - 10 # subtraction
# 10 * 20 # multiplication
# 20 / 5  # division
# 10 / 3  # = 3.333...
# 10 // 3 # = 3 floor division
# 2 ** 8  # power calculation

width = 100
height = 200
area = width * height
perimeter  = (width + height) * 2 # use parenthesis to specify operator precedence


# [python print function]
# syntax: print (arg_1, arg_2, arg_n...) -> [None] prints args to terminal
# print (a, b, full_name)


# [python input function]
# syntax: input(msg: str) -> [str] returns user input
question = "How old are you?"
age = input (question)

print("You are ", age, "years old")








# [python complex data types]
# list -> [1, 2, 3]
# tuple -> (1, 2, 3)
# dictionary -> {"first_name": "Ashkan", "last_name": "Mohammadi"}
students = [
    {
        "first_name": "some one",
        "last_name": "some last name",
    },
    {
        "first_name": "some one",
        "last_name": "some last name",
    },
    {
        "first_name": "some one",
        "last_name": "some last name",
    },
]