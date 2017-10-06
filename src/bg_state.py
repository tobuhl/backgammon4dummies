class points:
    def __init__(self):
        self.color = None
        self.count = 0


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
        self.color = color
        self.name = name
        self.kicked_tokens = 0

    def get_state(self):
        r"""
        Returns printable state of a player

        >>> p1 = player("Tom", 'white')
        >>> p1.get_state()
        'Tom\twhite\t0'
        """
        return "%s\t%s\t%d" % (self.name, self.color, self.kicked_tokens)


class state:
    def __init__(self, state_array, current_player, current_opponent):
        """ This class represents the state of a backgammon game """
        if state_array is None:
            self.tokens = [points() for x in range(25)]
            # [[0 for y in range(2)] for x in range(25)]
            # self.tokens[1].color = 'black'  # only for testing
        else:
            self.tokens = state_array
        self.dice_roll = [0] * 2
        if current_player == current_opponent:
            raise ValueError("Current Player and current opponent cannot be"
                             "equal.")
        self.current_player = current_player
        self.current_opponent = current_opponent

    def set_token(self, point, count, color):
        """
        Places 'count' token of 'color' @ 'point'

        >>> p1 = player("Tom", 'white')
        >>> p2 = player("Bobby", 'black')
        >>> st1 = state(None, p1, p2)
        >>> st1.set_token(1, 1, 'black')
        """
        self.tokens[point].count = count
        self.tokens[point].color = color

    def get_state(self):
        r"""
        Returns a state

        >>> p1 = player("Tom", 'white')
        >>> p2 = player("Bobby", 'black')
        >>> st1 = state(None, p1, p2)
        >>> st1.set_token(1, 1, 'white')
        >>> mv = move(1, 4)
        >>> st1.proposed_move_valid(mv)
        True
        >>> st1.change_state(mv, p1, p2)
        >>> st1.get_state()[:56]
        '0, 0, None\n1, 0, None\n2, 0, None\n3, 0, None\n4, 1, white\n'
        """
        s = ""
        for i in range(len(self.tokens)):
            s += "%d, %d, %s\n" % (i, self.tokens[i].count, self.tokens[i].color)
        return s

    def set_current_roles(self, current_player, current_opponent):
        self.current_player = current_player
        self.current_opponent = current_opponent

    def change_state(self, move, current_player, current_opponent):
        """
        Executes a move
        User must check validity of move first by calling proposed_move_valid()

        >>> p1 = player("Tom", 'white')
        >>> p2 = player("Bobby", 'black')
        >>> st1 = state(None, p1, p2)
        >>> st1.set_token(1, 1, 'white')
        >>> mv = move(1, 5)
        >>> st1.proposed_move_valid(mv)
        True
        >>> st1.change_state(mv, p1, p2)
        """
        self.tokens[move.source].count -= 1
        if self.tokens[move.source].count == 0:
            self.tokens[move.source].color = None
        self.tokens[move.target].count += 1
        if self.tokens[move.target].color != current_opponent:
            current_opponent.kicked_tokens += 1
        if self.tokens[move.target].color != current_player.color:
            self.tokens[move.target].color = current_player.color

        self.set_current_roles(current_player, current_opponent)

    def proposed_move_valid(self, move):
        """
        This method returns True, if move is valid and False otherwise.
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

        >>> p1 = player("Tom", 'white')
        >>> p2 = player("Bobby", 'black')
        >>> st1 = state(None, p1, p2)
        >>> st1.set_token(1, 1, 'white')
        >>> mv = move(1, 5)
        >>> st1.proposed_move_valid(mv)
        True
        >>> mv = move(2, 5)
        >>> st1. proposed_move_valid(mv)
        Invalid move: Player tries to move opponents or no token.
        False

        """
        if self.current_player.color != self.tokens[move.source].color:
            print("Invalid move: Player tries to move opponents or no token.")
            return False
        if self.tokens[move.source].color != self.tokens[move.target].color \
           and self.tokens[move.target].count > 1:
            print("Invalid move: Player tries kick multiple opponents tokens.")
            return False
        if self.tokens[move.source].color == self.tokens[move.target].color \
           and self.tokens[move.target].count > 4:
            print("Invalid move: Player tries to move to a full house.")
            return False
        if move.target > 24:
            print("Invalid move: Player tries to move beyond the board.")
            return False
        # otherwise, move is valid
        return True
