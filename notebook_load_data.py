"""
Load functions
"""
import degrees
from degrees import load_data
directory = "/Users/duc/Desktop/CS50AI_code/P0_degrees/small"


"""
Testing area
"""
# Test load_data()
load_data(directory)

degrees.people

degrees.people["102"]["name"]

degrees.names

degrees.movies

list(degrees.names)

degrees.names.get('kevin bacon')

name = "Kevin Bacon"

name.lower()

degrees.names.get(name.lower())
degrees.names["kevin bacon"].add("555")
degrees.names["kevin bacon"]
list(degrees.names.get(name.lower()))
list(degrees.names.get(name.lower(), set()))

# Test person_id_for_name()
testID = degrees.person_id_for_name('kevin bacon')
print(testID)

name = "Demi Moore"
person_ids = list(degrees.names.get(name.lower(), set()))
print(person_ids)


# Test test_goal()
list_test = (("m_id_1234", "p_id_44"),
             ("M_id_2", "P_id_2")
             )
target_id = "p_id_44"

if any(target_id in list_element for list_element in list_test):
    print("yippie")
else:
    print("aaaw")


neighbors = (("m12353", "p12"), ("m8763", "p2389"), ("m032745", "p385"))
neighbors

target_false = "p386"

degrees.test_goalState(neighbors, target_false)

target_true = "p385"

degrees.test_goalState(neighbors, target_true)
