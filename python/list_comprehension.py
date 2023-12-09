# List comprehension
# new_list = [new_item for item in list] 
prev_list = [1,2,3] 
new_list = [i * 2 for i in prev_list]
print(prev_list)
print(new_list)

#List Comprehension could be used for list, range, string, tuple
language = "Python"
new_list1 = [letter for letter in language]
print(new_list1)

#Conditional List Comprehension
# new_list = [new_item for item in list if condition] 
prev_list2 = [-1, 10, 18, -10, 2, -90, 60, 45, 20]
new_list2 = [number for number in prev_list2 if number > 0]
print(new_list2)

prev_list3 = [-1, 10, 18, -10, 2, -90, 60, 45, 20]
new_list3 = [number * number for number in prev_list3 if number < 0]
print(new_list3)

sentence = 'My name is Assiya'

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

#print(is_consonant('k'))
consonants = [i for i in sentence if is_consonant(i)] 
print(consonants)


# new_list = [new_item if condition for item in list]
prev_list4 = [-1, 10, 18, -10, 2, -90, 60, 45, 20]
new_list4 = [number if number > 0 else 0 for number in prev_list4]
print(new_list4)

def get_number(number):
    if number > 0:
        return number
    else:
        return 'negative number'
    
prev_list5 = [-1, 10, 18, -10, 2, -90, 60, 45, 20]
new_list5 = [get_number(number)for number in prev_list5]
print(new_list5)
