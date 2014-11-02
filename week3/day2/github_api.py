import requests
import json
from directed_graph import DirectedGraph


class GitHubSocialNetwork:

    def __init__(self, user):
        self.user = user
        self.graph = DirectedGraph()

    def __followers_caller(self, user):
        client_id = "f8be3d072416ea05b379"
        client_secret = "63f1f862a9c6c2b892dcc577f462b1cb0f095722"
        data = 'https://api.github.com/users/{}/following'.format(user)
        data += '?client_id={}&client_secret={}'.format(client_id, client_secret)
        return data

    def __graph_level_builder(self, user, graph):
        r = requests.get(self.__followers_caller(user))
        for follower in json.loads(r.text):
            graph.add_edge(user, follower["login"])

    def __graph_builder(self, user, depth, graph, max_depth):
        if (depth > max_depth):
            return
        self.__graph_level_builder(user, graph)
        for follower in graph.graph[user]:
            self.__graph_builder(follower, depth + 1, graph, max_depth)

    def __graph_init(self, max_depth):
        if (max_depth >= 4):
            raise ValueError("So Deep")
        self.__graph_builder(self.user, 0, self.graph, max_depth)

    def following(self):
        graph = DirectedGraph()
        self.__graph_level_builder(self.user, graph)
        return graph.graph[self.user]

    def is_following(self, followed):
        return followed in self.following()

    def steps_to(self, username):
        self.__graph_init(3)
        return self.graph.steps_between(self.user, username)