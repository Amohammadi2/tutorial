students = ['Ashkan', 'Amirreza', 'Ali']

# accessing items
first_student = students[0]
second_student, third_student = students[1], students[2]
print (first_student, second_student, third_student)

# slicing
new_list = students[0:2] # first two students
# [1:] -> from the second item to the end
# [:4] -> from the first item to the forth item
# [:] -> from start to the end (create a shallow copy)

# slice assignment
new_list[0] = 'Sadegh'
new_list[0:3] = ['student_1', 'student_2', 'student_3']

# adding a new item
students.append('Alireza')
new_students = ['Mohammadali', 'Arash', 'Keivan']
# append a list to the original one
some_list = students + new_students # makes a copy and doesn't mutate the original list
students.extend(new_students) # mutates the original one as well

# removing an item
students.pop(2) # remove the third item
students.remove('Ashkan') # remove 'Ashkan' from list

# mutability
my_list = [1, 2, 3]
my_list2 = my_list
my_list3 = my_list.copy() # my_list[:]
my_list2.append(4)

# checking equality
print (my_list == my_list2)
print (my_list == my_list3)