
#Exercise 0.1

"""
By using the slicing syntax change the following collections.

After slicing:
1. ['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
2. ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
3. ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
4. ['Hello', 'World', 'Huston', 'we', 'are', 'here']  -> ['are']
5. ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
6. ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
7. ('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
8 'Hello World Huston we are here' -> 'World Huston we'"""

print("\n>>>Exercise 0.1 - Slicing<<<")
lst1 = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
lst2 = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
lst3 = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
lst4 = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
lst5 = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
lst6 = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
tup7 = ('Hello', 'World', 'Huston', 'we', 'are', 'here')

new1 = lst1[1:5]
print(f"lst1 sliced = {new1}")

new2 = lst2[0:2]
print(f"lst2 sliced = {new2}")

new3 = lst3[4:6]
print(f"lst3 sliced = {new3}")

new4 = list(lst4[4])
print(f"lst4 sliced = {new4}")

new5 = list(lst5[0] + " " + lst5[2] + " " + lst5[4])
print(f"lst5 sliced = {new5}")

new6 = lst6[::-1]
print(f"lst5 sliced = {new6}")

new_tup_7 = list(tup7[1:-2])
print(f"lst7 sliced = {new_tup_7}")

string8 = ['Hello','World','Huston','we','are','here']
new8 = string8[1:4]
print(f"lst8 sliced = {new8}")

#Exercise 1 - build in functions
"""
Create a list like this: names = ['George', 'Bejamin', 'Thomas', 'John']
Look at this list of pythons build in functions.
Try all of these in the interpretor (on a list you create). e.g len(names)
Not all will work on lists, but try it out and see what works.
"""

print("\n>>>Exercise 1 - build in functions<<<")
names = ['George', 'Bejamin', 'Thomas', 'John']
print("Trying many functions in Python!!!")
print(f"Sorted on length = {sorted(names, reverse=True, key=len)}")
print(id(names))
print(len(names))
print(tuple(names))
print(type(names))
print(all(names))

#Exercise 1.1 - Tuple or list?

"""
#Claus, 51, male, clbo@kea.dk, 31011970-1313                                                                      ANSWER = Tuple 
#Bmw, Toyota, Hyundai, Skoda, Fiat, Volvo                                                                         ANSWER = List  
#Claus, Henning, Torben, Carl, Tine                                                                               ANSWER = List  
#‘Hello’, ‘World’, ‘Huston’, ‘we’, ‘are’, ‘here’                                                                  ANSWER = List  
#Rolling Stones, Goats Head Soup, 31 August 1973, 46:56                                                           ANSWER = Tuple 
#40.730610, -73.935242, New York City, NY, USA; 31.739847, 65.755920, Kandahar, Kandahar Province, Afghanistan;   ANSWER = Tuple
"""

#Exercise 2 - Sort a text

"""
1. Create a function that takes a string as a parameter and returns a list.
2. The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.
"""
print("\n>>>Exercise 2 - Sort a text<<<")
def sorting_letters(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å']
    lst = list(word)
    for x in word:
        for y in vowels:
            if x == y:
                lst.remove(x)
    lst.sort()
    return lst

print(f"Vowels removed and consonant sorted in the word = {sorting_letters('minecraft')}")

#Exercise 3 - Sort a list

"""
1. Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
2. Sort this list by using the sorted() build in function.
3. Sort the list in reversed order.
4. Sort the list on the lenght of the name.
5. Sort the list based on the last letter in the name.
6. Sort the list with the names where the letter ‘a’ is in the name first.
"""

print("\n>>>Exercise 3 - Sort a list<<<")
l = ["Claus", "Ib", "Per"]
l_first_a = []
print(f"1. List created = {l}")
print(f"2. List sorted {sorted(l)}")
print(f"3. List sorted in reversed order {sorted(l, reverse=True)}")
print(f"4. List sorted on the length of the name {sorted(l, key=len)}")
print(f"5. List sorted based on the last letter in the name {sorted(l, key = lambda x:x[-1])}")
def first_a(x):
    l_first_a.append(x.find('a'))
    return l_first_a
print(f"6. List sorted based on the names where the letter ‘a’ is in the name first. {sorted(l, key=first_a)}")


#Exercise 4 - Text editor plugin simulation

s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'

"""
1. Count the number of characters including blank spaces.
2. Count the number of characters excluding blank spaces.
3. Count the number of words.
"""

print("\n>>>Exercise 4 - Text editor plugin simulation<<<")
s_without_linebreak = s.replace("\n\n", "")
print(f"1. Number of characters including blank spaces = {len(s_without_linebreak)}")
s_without_spaces = s.replace(" ", "")
print(f"2. Number of characters excluding blank spaces = {(len(s_without_spaces.strip()))}")
print(f"3. Number of characters excluding blank spaces = {(len(s_without_linebreak.split())+1)}")


#Exercise 4 - Files

"""
1. Create a file and call it lyrics.txt (it does not need to have any content)
2. Create a new file and call it songs.docx and in this file write 3 lines of text to it.
3. Open and read the content and write it to your terminal window. * you should use both the read(), readline(), 
nd readlines() methods for this. (so 3 times the same output).
"""

print("\n>>>Exercise 4 - Files<<<")
lyrics_file = open("lyrics.txt", "w")
print(f"1. File created = {lyrics_file.name}")
lyrics_file.close()
songs_file = open("songs.docs", "w")
songs_file.write("This is a new song file\nWe will play some\nLounge music!!!")
songs_file = open("songs.docs", "r")
print(f"2. The content of the songs file are:\n\n{songs_file.read()}\n")
songs_file = open("songs.docs", "r")
print(f"3. The content of the songs file are in a list:{songs_file.readlines()}")
songs_file.close()


#Exercise 5 - Sort a list of tuples

"""
1. Based on this list of tuples: [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]
2. Sort the list so the result looks like this: [(2, 1), (3, 1), (10, 1), (1, 2), (2, 2), (2, 2), (3, 2), (10, 4), (1, 5)]

This is first sorted by the last element in the tuple and then the first element in the tuple.
You should do this in 1 step, but it might help you to try it out in 2 steps first.
"""


print("\n>>>Exercise 5 - Sort a list of tuples<<<")

tuples_list = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]
new_list = sorted(tuples_list, key=lambda tup: (tup[1], tup[0]))
print(f"The list sorted by last element and then first element in the tuple = {new_list}")