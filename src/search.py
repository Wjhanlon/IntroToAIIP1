from problem import Node
from utils import memoize, PriorityQueue

def astar_search(problem, h=None):
    """A* search is best-first graph search with f(n) = g(n) + h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""

    #  __   __                  ____          _         _   _
    #  \ \ / /__  _   _ _ __   / ___|___   __| | ___   | | | | ___ _ __ ___
    #   \ V / _ \| | | | '__| | |   / _ \ / _` |/ _ \  | |_| |/ _ \ '__/ _ \
    #    | | (_) | |_| | |    | |__| (_) | (_| |  __/  |  _  |  __/ | |  __/
    #    |_|\___/ \__,_|_|     \____\___/ \__,_|\___|  |_| |_|\___|_|  \___|

    h = memoize(h or problem.h)
    # Be sure to read about hints in the IP 1 description.

    node = Node(problem.initial)
    frontier = PriorityQueue()
    frontier.put(node, h(node.state))


    #repeated state detection
    explored = set()

    while frontier:
        node, _ = frontier.pop()

        if problem.is_goal(node.state):
            return node

        explored.add(node.state)

        #expand Node
        for child in node.expand(problem):
            f = child.path_cost + h(child.state)
            if child.state not in explored and child not in frontier:
                frontier.put(child, f)
            elif child in frontier:
                if frontier[child] > f:

                    frontier.update_priority(child, f)

    return None

def ucs_search(problem):
    """Uniform Cost Search (UCS) is a search algorithm that expands the least
    cost node in the search tree. It is a special case of A* search, so try to
    reuse the astar_search function."""

    #  __   __                  ____          _         _   _
    #  \ \ / /__  _   _ _ __   / ___|___   __| | ___   | | | | ___ _ __ ___
    #   \ V / _ \| | | | '__| | |   / _ \ / _` |/ _ \  | |_| |/ _ \ '__/ _ \
    #    | | (_) | |_| | |    | |__| (_) | (_| |  __/  |  _  |  __/ | |  __/
    #    |_|\___/ \__,_|_|     \____\___/ \__,_|\___|  |_| |_|\___|_|  \___|

    return astar_search(problem, lambda n: 0)
