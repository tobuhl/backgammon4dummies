class move:
    def __init__(self, source, target):
        """ Represents a move: Consists of source and target """
        self.source = source
        self.target = target
        diff = target - source
        if diff < -6 or diff > 6:
            raise ValueError("Unvalid move: Source %d, Target: %d"
                             % (source, target))
        if target > 24:
            raise ValueError("Unvalid move: Target %d"
                             ", violates board boundaries" % (target))


class player:
    def __init__(self, name, color):
        """
        This class represents a player

        >>> p1 = player("Tom", 'white')
        >>> p2 = player("Bobby", 'black')
        """
        def enum(**named_values):
            return type('Enum', (), named_values)

        Color = enum(Black='black', White='white')
        if color not in Color.Black and color not in Color.White:
            raise ValueError('color not valid')
        self.player_name = name


class state:
    def __init__(self, state_array, current_player):
        """ This class represents the state of a backgammon game """
        if state_array is None:
            self.tokens = [[0 for y in range(2)] for x in range(25)]
            self.tokens[1][0] = 'black'
        else:
            self.tokens = state_array
        self.dice_roll = [0] * 2
        self.current_player = current_player

    def change_state(self):
        """ Executes a move """

    def proposed_move_valid(self, move):
        """
        This method return True, if move is valid and False otherwise.
        Move is represented by source and target. Since the tokens are hold in
        a single array, the color of the token, that is moved is known
        implicitly.

        There are several things that may disqualify a move:
        1. The target field is already occupied by:
            a. more than 4 tokens with the same color
            b. more than one tokens with the other color
        2. The move violates board boundaries (i.e. moves beyond the end)
        3. The current player tries to move a token, that does not belong to
            him.

        >>> st1 = state(None, 'black')
        >>> mv = move(1, 5)
        >>> st1.proposed_move_valid(mv)
        True

        """
        if self.current_player != self.tokens[move.source][0]:
            return False
        if self.tokens[move.source][0] != self.tokens[move.target][0] \
           and self.tokens[move.target][1] > 1:
            return False
        if self.tokens[move.source][0] == self.tokens[move.target][0] \
           and self.tokens[move.target][1] > 4:
            return False
        if move.target > 24:
            return False
        # otherwise, move is valid
        return True
