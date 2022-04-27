class Node():
    def __init__(self, person_id, con_movie_id):
        # from original util.py
        # self.state = state
        # self.parent = parent
        # self.action = action
        self.person_id = person_id  # new node preferences
        self.con_movie_id = con_movie_id
        # self.movie_ids = movie_ids
        # self.order = order+1
        # self.neighbors = neighbors
        # self.persons_on_path = persons_on_path


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

# To be tested#
    def contains_node(self, person_id, movie_id):
        for node in self.frontier:
            if any(person_id == node.person_id and movie_id == node.movie_id):
                return

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
