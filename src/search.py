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

    node = Node(problem.start)
    #min prio queue? define hueristic and then put into prio queue as lambda cost. Minimize the n: n.path_cost + h(n)
    frontier = PriorityQueue()
    frontier.append(node)

    #repeated state detection
    explored = set()

    while frontier:
        node = frontier.pop()

        if node.state == problem.goal:
            return node

        explored.add(node.state)

        #expand Node
        for child in node.expand():
            if child not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if frontier[child] > child.path_cost() + h(child):
                    frontier.remove(child)
                    frontier.append(child)

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

    node = Node(problem.start)
    frontier = PriorityQueue()
    frontier.append(node)

    explored = set()

    while frontier:
        node = frontier.pop()
        if node.state == problem.goal:
            return node
        explored.add(node.state)

        for child in node.expand():


    return None
