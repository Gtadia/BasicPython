"""
Lists
"""

def func1():
# Lists: ordered, mutable, and allows duplicate elements
    mylist = ["Mercedes Benz", "Porsche", "BMW"]
    print(mylist)

    mylist2 = [5, True, "apple", "apple"]
    print(mylist2)

    item = mylist[1]
    print(item)

    item = mylist[-1] # Last item
    print(item)

    item = mylist[-2] # Second to last item
    print(item)


def func2():
    # You can iterate through a list as so.
    mylist = ["Mercedes Benz", "Porsche", "BMW"]
    for i in mylist:
        print(i)


def func3():
    # You can check if an item is in the list
    mylist = ["Mercedes Benz", "Porsche", "BMW"]
    if "BMW" in mylist:
        print(True)
    else:
        print(False)


def func4():
    # You can check the length of your list
    mylist = ["Mercedes Benz", "Porsche", "BMW"]
    print(len(mylist))


def func5():
    # You can append items (add items to the end) to a list (becuse it is mutable)
    mylist = ["Mercedes Benz", "Porsche", "BMW"]
    mylist.append("Kia")
    print(mylist)


def func6():
    # You can add items at a specific index of a list (it moves the other items to the right)
    mylist = ["Mercedes Benz", "Porsche", "BMW"]
    mylist.insert(1, "Toyota")
    print(mylist)


def func7():
    # You can reverse the list
    mylist = ["Mercedes Benz", "Porsche", "BMW"]
    item = mylist.reverse()
    print(mylist)
    print(item) # You can't do this because .reverse() only reverses the list and not return anything that can be saved as a variable
    print(mylist) # This is a "permanent" change to the list


def func9():
    # You can remove certain items (and see which item that you have removed)
    mylist = ["Mercedes Benz", "Porsche", "BMW"]
    removed = mylist.pop() # removes the last item in the list (if you don't specify the index)
    print(removed) # You can see which item was removed
    print(mylist) # You can see that the item as been removed from the list


def func10():
    mylist = ["Mercedes Benz", "Porsche", "BMW"]
    # The same thing happens as it did above except that I didn't save the removed item in a variable and I specified a specific index to remove the item
    print(mylist.pop(1))
    print(mylist)


def func11():
    # You can remove certain items (the item itself, not the item in a specific index)
    mylist = ["Mercedes Benz", "Porsche", "BMW"]
    removed = mylist.remove("BMW")
    print(removed) # You can see that you cannot see which item was removed, unlike .pop()
    print(mylist) # If the item does not exist in the list, you will get an error (a value error)

def func12():
    # You can remove all items
    mylist = ["Mercedes Benz", "Porsche", "BMW"]
    cleared = mylist.clear()
    print(mylist)
    print(cleared) # You can see that .clear() does not return the values that it deleted, because it deletes literally everything


def func13():
    # You can have your list be sorted in ascending order (it will put strings in alphabetical order)
    mylist = [4, 3, 1, -1, -5, 10]
    item = mylist.sort()
    print(item) # This does nothing because the .sort() sorts the list and does not have anything that can be saved as a variable
    print(mylist) # This completely changes the list (like, it kindof permanently changes it, until you change it again)


def func14():
    mylist = [4, 3, 1, -1, -5, 10]
    new_list = sorted(mylist) # You can use this isntead to not change the original list but have a sorted copy of it.
    print(new_list)
    # In a sorted list, you can reverse the sorting order of how the sorted() method sorts.


def func15():
    # How to create a new list with the same value duplicated several times
    mylist = [0] * 5
    print(mylist) # prints out a list with 5 zeros.


def func16():
    # You can concatenate lists
    mylist = [0] * 5
    mylist2 = [1, 2, 3, 4, 5]
    new_list = mylist + mylist2
    print(new_list)


def func17():
    # You can slice your lists
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = mylist[1:5]
    print(a) # prints out index 1 to index 4

    a = mylist[:5]
    print(a) # prints out from index 0 (beginning) to index 4

    a = mylist[1:]
    print(a) # prints out from index 1 to index 8 (the end)

    a = mylist[::2]
    print(a) # prints out from the beginning to the end with a step of 2 (iterating by 2)

    a = mylist[::-4]
    print(a) # prints out from the beginning to the end with a step of 4 and the list being read backwards
    
    a = mylist[3:7:3]
    print(a) # prints out index 3 to index 6 with a step of/iterates by 3

    a = mylist[-1:-6:-1]
    print(a) # prints out index 8 to index 3 and iterating backwards


def func18():
    """
    When you make a list equal to another list, both lists will be linked together so when you modify one list, you will
    modify the other as well.
    
    In other words, you have do something different if you want to create a copy that is independent from the original 
    list.
    """
    list_original = ["banana", "cherry", "apple"]
    list_copy = list_original
    list_copy.append("lemon")
    print(list_copy)
    print(list_original)


def func19():
    # You can make a TRUE copy of a list that is independent from the original list
    list_original = ["banana", "cherry", "apple"]
    list_copy = list_original.copy()
    list_copy.append("lemon") # only appends "lemon" to "list_copy" and doesn't change "list_original"
    print(list_copy)
    print(list_original)


def func20():
    # ANOTHER way to make a TRUE copy of a list that is independent from the original list
    list_original = ["banana", "cherry", "apple"]
    list_copy = list_original[:]
    list_copy.append("lemon") # only appends "lemon" to "list_copy" and doesn't change "list_original"
    print(list_copy)
    print(list_original)


def func21():
    # QUICKLY modifying the contents of a list using list comprehensions
    a = [1, 2, 3, 4, 5, 6]
    b = [i*i for i in a]
    c = [(x+x)*x for x in b]
    # list_name = [<expression> for <new_variable_that_you_can_create_in_this_spot> in <original_list_name>]
    print(a)
    print(b)
    print(c)


def func22():
    """
    You can turn a string into a list of characters
    """
    mylist = list("ABCDEFGH")
    print(mylist)



# type the name of the function that you want to run here
func22()