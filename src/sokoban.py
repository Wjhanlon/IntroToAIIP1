from problem import Problem

#  __   __                  ____          _         _   _
#  \ \ / /__  _   _ _ __   / ___|___   __| | ___   | | | | ___ _ __ ___
#   \ V / _ \| | | | '__| | |   / _ \ / _` |/ _ \  | |_| |/ _ \ '__/ _ \
#    | | (_) | |_| | |    | |__| (_) | (_| |  __/  |  _  |  __/ | |  __/
#    |_|\___/ \__,_|_|     \____\___/ \__,_|\___|  |_| |_|\___|_|  \___|
class Sokoban(Problem):
    """
    A Sokoban problem instance for search algorithms.
    Come up with your own representation for the state.
    """

    def __init__(self, board):
        """
        Initializes the Sokoban problem.
        :param board: List of strings, each string represent a row of the game board
        """
        self.rows = len(board)
        self.columns = len(board[0])
        initial_state = tuple(tuple(row) for row in board)
        super().__init__(initial_state)

    def actions(self, state):
        """Returns the list of valid actions from the current state."""
        valid_actions = []
        player_row = None
        player_col = None

        for row in range(self.rows):
            for col in range(self.columns):
                if state[row][col] == 'P' or state[row][col] == '#':
                    player_row = row
                    player_col = col

        directions = [('U', -1, 0), ('D', 1, 0), ('L', 0, -1), ('R', 0, 1)]

        for direction, direction_row, direction_col in directions:
            new_row = player_row + direction_row
            new_col = player_col + direction_col

            if state[new_row][new_col] == '%':
                continue

            if state[new_row][new_col] == 'b' or state[new_row][new_col] == 'B':
                box_row = new_row + direction_row
                box_col = new_col + direction_col
                if state[box_row][box_col] == '%' or state[box_row][box_col] == 'b' or state[box_row][box_col] == 'B':
                    continue

            valid_actions.append(direction)
        return valid_actions


    def result(self, state, action):
        """Returns the resulting state after applying the action."""
        new_state = [list(row) for row in state]

        player_row = None
        player_col = None

        for row in range(self.rows):
            for col in range(self.columns):
                if new_state[row][col] == 'P' or new_state[row][col] == '#':
                    player_row = row
                    player_col = col

        moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        direction_row, direction_col = moves[action]
        new_row = player_row + direction_row
        new_col = player_col + direction_col

        if new_state[new_row][new_col] == 'b' or new_state[new_row][new_col] == 'B':
            box_row = new_row + direction_row
            box_col = new_col + direction_col

            if new_state[box_row][box_col] == ' ':
                new_state[box_row][box_col] = 'b'
            elif new_state[box_row][box_col] == '.':
                new_state[box_row][box_col] = 'B'

            if new_state[new_row][new_col] == 'b':
                new_state[new_row][new_col] = 'P'
            elif new_state[new_row][new_col] == 'B':
                new_state[new_row][new_col] = '#'

        else:
            if new_state[new_row][new_col] == '.':
                new_state[new_row][new_col] = '#'
            else:
                new_state[new_row][new_col] = 'P'

        if new_state[player_row][player_col] == '#':
            new_state[player_row][player_col] = '.'
        else:
            new_state[player_row][player_col] = ' '

        return tuple(tuple(row) for row in new_state)

    def is_goal(self, state):
        """Checks if all boxes are on goal positions."""
        for row in range(self.rows):
            for col in range(self.columns):
                if state[row][col] == '.' or state[row][col] == '#':
                    return False
        return True

    def h(self, state):
        """Heuristic function for the problem. This should return a
        non-negative estimate of the cost to reach the goal from the
        given state."""
        total_cost = 0
        boxes = []
        goals = []

        for row in range(self.rows):
            for col in range(self.columns):
                if state[row][col] == '.' or state[row][col] == '#':
                    goals.append((row, col))
                if state[row][col] == 'b':
                    boxes.append((row, col))

        for box in boxes:
            nearest = float('inf')
            for goal in goals:
                distance = abs(box[0] - goal[0]) + abs(box[1] - goal[1])
                if distance < nearest:
                    nearest = distance

            total_cost += nearest

        return total_cost
