# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.

my_string = "Names are powerful things; you should be careful whom you share yours with. You never know when a person might turn your name against you."
my_number = 345
my_book_list = ["To Sleep in a Sea of Stars","The Invisible Life of Addie LaRue","Dune","Akata Witch","The Giver","Magic Steeped in Poison"]
do_i_love_reading = True

#print(my_number.isnumeric())
# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 

first_three_of_my_string = my_string[0:3]
print(first_three_of_my_string)

# Exercise 3: Use an index to grab the first element from your list.

book_one = my_book_list[0]
print(book_one)

# Exercise 4: Create a new number variable that adds 10 to your original number.

new_number = my_number + 10
print(new_number)

# Exercise 5: Use an index to get the last element in your list.

book_last = my_book_list[-1]
print(book_last)

# Exercise 6: Use split to transform the following string into a list.

names = 'harry,alex,susie,jared,gail,conner'

list_of_names = names.split(',')
print(list_of_names)

# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. 
# Create a new string that takes the uppercase word and the rest of the original string.

first_word = my_string[0:5]

first_word_upper = first_word.upper()

my_new_sentence = f'{first_word_upper}{my_string[5:]}'

print(my_new_sentence)

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

my_num_string = f"I have read {my_number} books this year."
print(my_num_string)

# Exercise 9: Print “hello world”.

print("hello world")