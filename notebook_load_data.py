import degrees
from degrees import load_data
directory = "/Users/duc/Desktop/CS50AI_code/P0_degrees/small"


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
