def func1():
    # list[start(inclusive): end (exclusive): step]
    example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(example_list[::-1]) # This is equal to (example_list[-1:: -1])
    # If you want more examples, you can check out "3-Lists_Tuples_and_Sets"


def func2():
    sample_text = "The quick brown fox jumps over the lazy dog" # REMEMBER: Strings are just like lists where each index is a character
    print(sample_text)
    print(sample_text[3: 21: 3]) # You can slice strings like text
    print(sample_text[::-1]) # Therefore, this is how you can reverse text
 

# type the name of the function that you want to run here
func2()