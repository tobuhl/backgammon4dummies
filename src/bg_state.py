last_point = 24  # use as a const: do not change!

class Points:
    def __init__(self):
        self.color = None
        self.count = 0

    def setPoint(self, color, count):
        self.color = color
        self.count = count

    def __str__(self):
        return str(self.count) + "[" + str(self.color) + "]"


class Move:
    def __init__(self, source, target):
        """ Represents a move: Consists of source and target """
        self.source = source
        self.target = target
        diff = target - source
        if diff < -6 or diff > 6:
            raise ValueError("Unvalid move: Source %d, Target: %d"
                             % (source, target))
        # moving a token exatly behind the board might be legal
        if 0 > target > last_point + 1:
            raise ValueError("Unvalid move: Target %d"
                             ", violates board boundaries" % (target))

def enum(**named_values):
    return type('Enum', (), named_values)
Color = enum(Black='black', White='white')

class Player:
    def __init__(self, name, color):
        """
        This class represents a player

        >>> p1 = Player("Tom", 'white')
        >>> p2 = Player("Bobby", 'black')
        """

        if color not in Color.Black and color not in Color.White:
            raise ValueError('color not valid')
        self.color = color
        self.name = name
        self.kicked_tokens = 0

    def get_state(self):
        r"""
        Returns printable state of a player

        >>> p1 = Player("Tom", 'white')
        >>> p1.get_state()
        'Tom\twhite\t0'
        """
        return "%s\t%s\t%d" % (self.name, self.color, self.kicked_tokens)


class State:
    def __init__(self, state_array, current_player, current_opponent):
        """ This class represents the state of a backgammon game """
        if state_array is None:
            self.tokens = [Points() for x in range(26)]
            # [[0 for y in range(2)] for x in range(25)]
            # self.tokens[1].color = 'black'  # only for testing
        else:
            self.tokens = state_array
        # self.dice_roll = [0] * 2
        if current_player == current_opponent:
            raise ValueError("Current Player and current opponent cannot be"
                             "equal.")
        self.current_player = current_player
        self.current_opponent = current_opponent      

    def set_token(self, point, count, color):
        r"""
        Places 'count' token of 'color' @ 'point'

        >>> p1 = Player("Tom", 'white')
        >>> p2 = Player("Bobby", 'black')
        >>> st1 = State(None, p1, p2)
        >>> st1.set_token(1, 1, 'black')
        >>> st1.get_state()[:45]
        '0, 0, None\n1, 1, black\n2, 0, None\n3, 0, None\n'
        """
        self.tokens[point].count = count
        self.tokens[point].color = color

    def get_state(self):
        r"""
        Returns a state

        >>> p1 = Player("Tom", 'white')
        >>> p2 = Player("Bobby", 'black')
        >>> st1 = State(None, p1, p2)
        >>> st1.set_token(1, 1, 'white')
        >>> mv = Move(1, 4)
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

        >>> p1 = Player("Tom", 'white')
        >>> p2 = Player("Bobby", 'black')
        >>> st1 = State(None, p1, p2)
        >>> st1.set_token(1, 1, 'white')
        >>> mv = Move(1, 5)
        >>> st1.proposed_move_valid(mv)
        True
        >>> st1.change_state(mv, p1, p2)
        """
        self.tokens[move.target].count += 1
        if self.tokens[move.target].color != current_opponent: #what
            current_opponent.kicked_tokens += 1
        if self.tokens[move.target].color != current_player.color:
            self.tokens[move.target].color = current_player.color
        if current_player.color == 'white' and move.source == 0:
            current_player.kicked_tokens -= 1
        elif current_player.color == 'black' and move.source == 25:
            current_player.kicked_tokens -= 1
        else:
            self.tokens[move.source].count -= 1
        if self.tokens[move.source].count == 0:
            self.tokens[move.source].color = None

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
            a. if not all tokens are in the last quadrant, the move is not valid
            b. if all tokens are in the last quadrant, a move of more than
               one point behind the board boundary is not valid.
        3. The current player tries to move a token, that does not belong to
            him.
        4. The player tries to move tokens which are not kicked, while having
           kicked tokens

        >>> p1 = Player("Tom", 'white')
        >>> p2 = Player("Bobby", 'black')
        >>> st1 = State(None, p1, p2)
        >>> st1.set_token(1, 1, 'white')

        >>> mv = Move(1, 5)
        >>> st1.proposed_move_valid(mv)
        True

        >>> mv = Move(2, 5)
        >>> st1. proposed_move_valid(mv)
        Invalid move: Player tries to move opponent's or no token.
        False

        >>> st2 = State(None, p1, p2)
        >>> st2.set_token(23, 2, 'white')

        >>> mv = Move(23, 25)
        >>> st2.proposed_move_valid(mv)
        True

        >>> st2.set_token(1, 1, 'white')
        >>> st2.proposed_move_valid(mv)
        Invalid move: Player tries to move beyond the board.
        False

        >>> st2.set_token(2, 1, 'black')
        >>> st2.set_current_roles(p2, p1)
        >>> mv = Move(2, 0)
        >>> st2.proposed_move_valid(mv)
        True
        >>> st2.set_token(20, 1, 'black')
        >>> st2.proposed_move_valid(mv)
        Invalid move: Player tries to move beyond the board.
        False
        """
        if self.current_player.color == 'white':
            if self.current_player.kicked_tokens > 0 and move.source != 0:
                return False
        if self.current_player.color == 'black':
            if self.current_player.kicked_tokens > 0 and move.source != 25:
                return False
        if self.current_player.color != self.tokens[move.source].color \
           and (move.source != 0 and move.source != 25):
            print("Invalid move: Player tries to move opponent's or no token.")
            return False
        # check, if all tokens are in the last quadrant
        # if so, moving a token to point 0 or 25 is legal for white or black
        # player respectively.
        no_tokens_out_of_last_quadrant = True
        if self.tokens[move.source].color == 'white':
            for i in range(1, 19):
                if self.tokens[i].count > 0 and self.tokens[i].color == 'white':
                    no_tokens_out_of_last_quadrant = False
                    break
            if no_tokens_out_of_last_quadrant and move.target == last_point + 1:
                # print("Valid move: White tokens only in last quadrant.")
                return True
        if self.tokens[move.source].color == 'black':
            for i in range(7, 25):
                if self.tokens[i].count > 0 and self.tokens[i].color == 'black':
                    no_tokens_out_of_last_quadrant = False
                    break
            if no_tokens_out_of_last_quadrant and move.target == 0:
                # print("Valid move: Black tokens only in last quadrant.")
                return True
        if self.tokens[move.source].color != self.tokens[move.target].color \
           and self.tokens[move.target].count > 1:
            print("Invalid move: "
                  "Player tries to kick multiple opponent's tokens.")
            return False
        if self.tokens[move.source].color == self.tokens[move.target].color \
           and self.tokens[move.target].count > 4:
            print("Invalid move: Player tries to move to a full house.")
            return False
        if move.target > last_point or move.target < 1:
            print("Invalid move: Player tries to move beyond the board.")
            return False
        # otherwise, move is valid
        return True

    def check_final_state(self, current_player):
        """
        Checks, if current_player has won. Call after move is done.

        >>> p1 = Player("Tom", 'white')
        >>> p2 = Player("Bobby", 'black')
        >>> st1 = State(None, p1, p2)
        >>> st1.check_final_state(p1)
        True
        >>> p1.kicked_tokens = 1
        >>> st1.check_final_state(p1)
        False
        >>> mv = Move(0, 1)
        >>> st1.proposed_move_valid(mv)
        True
        >>> st1.check_final_state(p1)
        False
        >>> st1.change_state(mv, p1, p2)
        >>> mv = Move(1, 7)
        >>> st1.proposed_move_valid(mv)
        True
        >>> st1.change_state(mv, p1, p2)
        >>> mv = Move(7, 13)
        >>> st1.proposed_move_valid(mv)
        True
        >>> st1.change_state(mv, p1, p2)
        >>> mv = Move(13, 19)
        >>> st1.proposed_move_valid(mv)
        True
        >>> st1.change_state(mv, p1, p2)
        >>> mv = Move(19, 25)
        >>> st1.proposed_move_valid(mv)
        True
        >>> st1.change_state(mv, p1, p2)

        >>> st1.check_final_state(p1)
        True
        """
        if current_player.kicked_tokens > 0:
            return False
        no_tokens_left = True
        if current_player.color == 'white':
            for i in range(25):
                if self.tokens[i].color == current_player.color:
                    no_tokens_left = False
                    break
        if current_player.color == 'black':
            for i in range(1, 26):
                if self.tokens[i].color == current_player.color:
                    no_tokens_left = False
                    break
        return no_tokens_left

    def __str__(self):
        r"""
        Returns a humanreadable string, can be printed with:

        print(str(st1))

        >>> p1 = Player("Tom", 'white')
        >>> p2 = Player("Bobby", 'black')
        >>> st1 = State(None, p1, p2)
        >>> st1.check_final_state(p1)
        True
        >>> p1.kicked_tokens = 1
        >>> mv = Move(0, 1)
        >>> st1.proposed_move_valid(mv)
        True

        >>> st1.change_state(mv, p1, p2)
        >>> st1.__str__()[:56]
        '0:\t0[None]\n1:\t1[white]\n2:\t0[None]\n3:\t0[None]\n4:\t0[None]\n'
        """
        strOutput = ""
        fieldNr = 0
        for p in self.tokens:
            strOutput += str(fieldNr) + ":\t" + str(p) + "\n"
            fieldNr += 1
        return strOutput

    def difference(self, oldState):
        if self.tokens is None:
            raise ValueError("Error: Tokens not initialized!")

        if oldState is None:
            raise ValueError("Error: oldState not initialized!")

        if oldState.tokens is None:
            raise ValueError("Error: oldState.tokens not initialized!")

        strOutput = ""
        thisFieldNr = 0        
        for thisPoint in self.tokens:
            thatFieldNr = 0
            for thatPoint in oldState.tokens:
                if thisFieldNr==thatFieldNr:
                    if thisPoint.color != thatPoint.color or thisPoint.count != thatPoint.count:                
                        strOutput += str(thisFieldNr) + ":\t" + str(thatPoint) + " CHANGED [" + str(thatPoint.count - thisPoint.count) + "]\n"  
                    else:
                        strOutput += str(thisFieldNr) + ":\t" + str(thatPoint) + "\n"
                thatFieldNr += 1
            thisFieldNr += 1
        return strOutput


