"""
https://youtu.be/9N6a-VLBa2I

Working with JSON data using the json module.

JSON = JavaScript Object Notation       # Was inspired by JavaScript but is now independent of any one language
    - Very common data format for storing some information.
    - Commonly used when fetching data from online APIs.
    - Also used for configuration files and different kinds of data that can be saved on your local machine.


You can convert JSON data back into Python and this process is called "deserialization" or "decoding"
    - loads() means that you're loading json data into python data as a string
    - load() means that you're loading json data into python data as a file/not as a string

We can also dump the JSON file (which has been converted from the Python dictionary) into a file
    - dumps() means that you're dumping Python data into json data as a string
    - dump() means that you're dumping Python data into json data as a file/not a string
"""

def func1():
    """
    Introduction to JSON
    """
    import json

    # The following "people_string" is a string that happens to be JSON compatiable/valid JSON,
# The following JSON file (in string format) has a key called "people" and the value of people is an array consisting of 2 objects and each object has a key of "name", "phone", "emails", and "has_license" 
# In other words, this a string of JSON code
    people_string = """
    {
        "people": [
            {
                "name": "John Smith",
                "phone": "615-555-7164",
                "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
                "has_license": false
            }, 
            {
                "name": "Jane Doe",
                "phone": "560-555-5153",
                "emails": ["janedoe@bogusemail.com", "jane.doe@work-place.com"],
                "has_license": true
            }
        ]
    }
    """

    # We can load this string into a Python objet so that we can work with the data more easily
    # In order to load "people_string" into Python from a string, we can use the "json.loads(people_string)"
    data = json.loads(people_string)
    
    print(data) # Returns the dictionary with a key of "people" and a value of a list of 2 dictionaries
    print(type(data)) # Just as proof, we can see that this is actually a dictionary


def func2():
    """
    When we load JSON into a Python object, it uses the following conversion table to convert from JSON to Python.
    We call this serialization or encoding.

    Python           VS     JSON
    dict             |      object 
    list             |      array 
    str              |      string
    int              |      number (int)
    float            |      number (real)
    True             |      true
    False            |      false
    None             |      null

    For example, a JSON object would be converted into a Python dictionary, a JSON array would be converted into a Python list,
    etc.  
    """
    import json

    people_string = """
    {
        "people": [
            {
                "name": "John Smith",
                "phone": "615-555-7164",
                "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
                "has_license": false
            }, 
            {
                "name": "Jane Doe",
                "phone": "560-555-5153",
                "emails": ["janedoe@bogusemail.com", "jane.doe@work-place.com"],
                "has_license": true
            }
        ]
    }
    """

    data = json.loads(people_string)
    
    print(data) # Notice how the things like the blooean values for "has_license" has changed from lowercase "true" to uppercase "True"


def func3():
    """
    Once we convert the JSON data (in string format) to Python, we are able to use it like a regular python dictionary, list, string, int, etc.
    """
    import json

    people_string = """
    {
        "people": [
            {
                "name": "John Smith",
                "phone": "615-555-7164",
                "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
                "has_license": false
            }, 
            {
                "name": "Jane Doe",
                "phone": "560-555-5153",
                "emails": ["janedoe@bogusemail.com", "jane.doe@work-place.com"],
                "has_license": true
            }
        ]
    }
    """

    data = json.loads(people_string) # We can now use "data" like it's a regular dictionary in Python
    
    for individuals in data["people"]:
        print(individuals["name"])
        print(individuals["phone"])


def func4():
    """
    We can convert a Python file back into JSON, even after we modified it in Python first before converting it to JSON (as a Python string).
    
    We can covnert Python back into a JSON (as a string in Python) using "json.dumps(<variable>)".
    """
    import json

    people_string = """
    {
        "people": [
            {
                "name": "John Smith",
                "phone": "615-555-7164",
                "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
                "has_license": false
            }, 
            {
                "name": "Jane Doe",
                "phone": "560-555-5153",
                "emails": ["janedoe@bogusemail.com", "jane.doe@work-place.com"],
                "has_license": true
            }
        ]
    }
    """

    data = json.loads(people_string)

    for person in data["people"]:
        del person["emails"] # We are modifying the dictionary by deleteing stuff from it
    
    new_string = json.dumps(data) # This converts the "data" dictionary without the "phone" key (because it was deleted) as a JSON (as a python multiline string)
    print(new_string) # Just printing out the JSON version


def func5():
    """
    When we convert from Python to JSON, it doesn't indent the code unless we tell it to.

    In order to have the JSON version of python code be indented, we can type "indent = <number of times to indent">" inside of "json.dumps()"
        "json.dumps(<variable/python_code>, indent=<# of indents>)"
    """
    import json

    people_string = """
    {
        "people": [
            {
                "name": "John Smith",
                "phone": "615-555-7164",
                "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
                "has_license": false
            }, 
            {
                "name": "Jane Doe",
                "phone": "560-555-5153",
                "emails": ["janedoe@bogusemail.com", "jane.doe@work-place.com"],
                "has_license": true
            }
        ]
    }
    """

    data = json.loads(people_string)
    
    new_string = json.dumps(data, indent=1) # adds only one indent for every line that needs that indent
    print(new_string)
    

def func6():
    """
    You can sort the keys (sorting the keys in alphabetical order)
        Another thing you can do to clean up your JSON when dumping it to a string. 

    "json.dumps(<variable>, sort_keys=<boolean value>)"
    """
    import json

    people_string = """
    {
        "people": [
            {
                "name": "John Smith",
                "phone": "615-555-7164",
                "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
                "has_license": false
            }, 
            {
                "name": "Jane Doe",
                "phone": "560-555-5153",
                "emails": ["janedoe@bogusemail.com", "jane.doe@work-place.com"],
                "has_license": true
            }
        ]
    }
    """

    data = json.loads(people_string)
    
    new_string = json.dumps(data, indent=2, sort_keys = True)
    print(new_string)


def func7():
    """
    How to load JSON files into Python objects and then write those Python objects back into JSON files

    If we wanted to load the "states.json" file into a Python object, then we can use the "json.load" method. 


    THE DIFFERENCE BETWEEN "json.loads" and "json.load" 
        - .loads        =           loads a string into a Python object
        - .load         =           loads a JSON file into a Python object
    """
    import json
    
    with open("states.json") as file_object: 
        data = json.load(file_object) 

    for a_state in data["states"]:
        print(a_state["name"], a_state["abbreviation"])

    print(type(data)) # You can see that this is stored as a dictionary (or it could be stored as any other object, just not in this case) (REMEMBER: JSON objects = Python dictionaries)
    


def func8():
    """
    We can also write Python objects out into a JSON file.

    THE DIFFERENCE BETWEEN "json.dumps" and "json.dump" 
    - .dumps        =           dumps a Python object into a string
    - .dump         =           dumps a Python object into a JSON file


    "json.dump(<Python Ojbect that you want to convert>, <the file that you want to dump to>)
    """
    import json

    with open("states.json") as f:
        data = json.load(f)

    with open("new_states.json", "w") as f: # We are opening/creating a new file to write the Python-to-JSON-conversion to
        json.dump(data, f, sort_keys=True, indent=5) # indent and sort_keys also works


def func9():
    """
    A Real-World Example

    Since it's pretty common for websites to return JSON from their APIs (because it's easy to parse), our real-world 
    example is going to do exactly that.
    """
    import json
    from urllib.request import urlopen # built-in/standard library module

    with urlopen("http://date.jsontest.com") as response:
        source = response.read()

    data = json.loads(source)
    print(json.dumps(data, indent=2)) # Since just straight up returning the JSON file returns a string in a single line with /n, loading and then dumping it will help to clear the JSON
    # Example output: b'{\n   "date": "06-28-2022",\n   "milliseconds_since_epoch": 1656429745740,\n   "time": "03:22:25 PM"\n}\n'


def func10():
    """
    We can encode an object into a JSON file
    """
    import json 

    class User:
        def __init__(self, name, age):
            self.userName = name
            self.userAge = age

    user = User("Max", 27)
    # userJSON = json.dumps(user) # Using this on its own will not work so we need to create our own encoding function.
    def encode_user(obj):
        """
        If the object, which we are going to pass in the variable user (an object), is an instance variable of the class User. We are going to
        return a dictionary with the name and age that contains the object "user"'s name (userName) and age (userAge) respectively.

        If the object "user" is not an instance of the class User, we are going to throw in a TypeError with the same error message that it gives us when we try to run "json.dumps()"
        without this custom encoding function.
        """
        if isinstance(obj, User):  # isinstance will check whether an object is an instance of a class (An instance of a class is... a member of a given class that has specified values rather than variables)
            return {'name': obj.userName, 'age': obj.userAge, obj.__class__.__name__: "hi"} # obj.__class__.__name__ is there just to return the class name so you can literally put anything in for the value part of the dictionary.
        else:
            raise TypeError("Object of type User is not JSON serializable")

    userJSON = json.dumps(user, default=encode_user) # We are passing in the object "user" and using "default=" to make "json.dumps" run using our custom encoding function.
    print(userJSON)


def func11():
    """
    Using the custom JSON encoder class, we can just encode the json file directly by calling the class and ".encode" (and specifying what we want to encode)
    """
    import json
    from json import JSONEncoder

    class User:
        def __init__(self, name, age):
            self.userName = name
            self.userAge = age

    user = User("Max", 27)

    class myUserEncoder(JSONEncoder): # This class is the same as the class that was used in the code above
        def default(self, obj):
            if isinstance(obj, User):
                return {"name": obj.userName, "age": obj.userAge, obj.__class__.__name__: "MIT"}
            else:
                return JSONEncoder.default(self, obj)

    userJSON = myUserEncoder().encode(user)
    print(userJSON)


def func12():
    """
    Using the custom JSON encoder class, we can just encode the json file directly by calling the class and ".encode" (and specifying what we want to encode)
    """
    import json
    from json import JSONEncoder

    class User:
        def __init__(self, name, age):
            self.userName = name
            self.userAge = age

    user = User("Max", 27)
    
    class myUserEncoder(JSONEncoder): # This class is the same as the class that was used in func11
        def default(self, obj):
            if isinstance(obj, User):
                return {"name": obj.userName, "age": obj.userAge, obj.__class__.__name__: "MIT"}
            else:
                return JSONEncoder.default(self, obj)

    userJSON = myUserEncoder().encode(user) # encoding directly using the ".encode" function
    print(userJSON)


def func13():
    """
    When you create custom objects, you can also decode them

    In other words, we can undo what was done in func10 through func12
    """
    # FUNC 12
    import json
    from json import JSONEncoder

    class User:
        def __init__(self, name, age):
            self.userName = name
            self.userAge = age

    user = User("Max", 27)
    
    class myUserEncoder(JSONEncoder): # This class is the same as the class that was used in func11
        def default(self, obj):
            if isinstance(obj, User):
                return {"name": obj.userName, "age": obj.userAge, obj.__class__.__name__: "MIT"}
            else:
                return JSONEncoder.default(self, obj)

    userJSON = myUserEncoder().encode(user) # encoding directly using the ".encode" function
    print(userJSON)
    # FUNC 12

    def decode_user(myDictionary):
        if User.__name__ in myDictionary:
            return User(name=myDictionary["name"], age=myDictionary['age'])
        return myDictionary

    user = json.loads(userJSON, object_hook=decode_user) # we're using the userJSON variable from func 12
    print(type(user))
    print(user.__name__())    



# type the name of the function that you want to run here
func9()