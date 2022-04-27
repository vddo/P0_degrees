class Node():
    def __init__(self, person_id, con_movie_id):
        self.con_movie_id = con_movie_id


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    # Checks if node (= combination fo person_id and movie_id)
    # already exists
    def contains_node(self, person_id, movie_id):
        return any(node.person_id == person_id
                   and node.con_movie_id == movie_id
                   for node in self.frontier
                   )

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
