"""
Example Module
"""
print("Imported my_example_module...")

test = "Test String"
test_2 = "test"

def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    
    return -1

class Thing():
    def __init__(self, why):
        self.why = why