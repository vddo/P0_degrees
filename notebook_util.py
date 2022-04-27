# Load stuff
import util
import degrees

directory = "/Users/duc/Desktop/CS50AI_code/P0_degrees/small"


# Working space
Node_0 = util.Node(person_id='p123', con_movie_id=None)

print(Node_0.con_movie_id)


# Simulate main()
directory = "small"
degrees.load_data(directory)
source = '398'  # Sally Field
target = "129"  # stared with Tom Hanks in Forrest Gump
# end

Start = degrees.shortest_path(source, target)
Start.con_movie_id
Start.person_id

# Testing util.contains_node()
# First with empty froniter
# Then with two nodes added with util.add()
frontier = util.QueueFrontier()
frontier.contains_node('p123', None)
frontier.add(util.Node(person_id='p123', con_movie_id=None))
frontier.add(util.Node(person_id='p444', con_movie_id='m222'))
frontier.contains_node('p123', None)


frontier.frontier
frontier.frontier[0].person_id


Node_0.person_id

for node in frontier.frontier:
    print(node.person_id)
for node in frontier.frontier:
    print(node.person_id)

any(frontier.frontier == 'p123')
any(node.person_id == 'p123' for node in frontier.frontier)
any(node.person_id == 'p123'
    and node.con_movie_id == None
    for node in frontier.frontier
    )

any(node.person_id == 'p444'
    and node.con_movie_id == None
    for node in frontier.frontier
    )

any(node.person_id == 'p444'
    and node.con_movie_id == 'm222'
    for node in frontier.frontier
    )
