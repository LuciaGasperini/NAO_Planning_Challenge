#The Debuggers - NAO challenge 2022 - Giacomo Caroli & Lucia Gasperini


import moves
from reporting import *
import random

# retrieving list of transitions and mandatory moves
transitions = moves.get_transitions()
compulsory = moves.get_compulsory()

#random.shuffle(transitions)  # transitions are blended to limit repetition

"""
no check is made on the minimum number of mandatory transitions because the algorithm already generates choreography that conforms to the request.
"""

""" the state is represented by a tuple of 3 values
    (current_move,counter,timer)
    --> current_move = current move running/just made
    --> counter = represents the number of moves (transitions) so far made in the interval between two mandatory moves
    --> timer = keeps the elapsed time as the sum of the times of the moves made
    
    !!! mind that both initial and goal in the constructor are two states!
        so the composition should be considered as follows:
        initial = ([initial move],0,0) #also indicate the time of the initial move
        goal = ([final move],[number of moves transition],[desired execution time])
"""

time_tolerance = 2.0  # tolerance in time control
max_move_counter = 2 # maximum number of transitions (2)


class Nao(Problem):

    def __init__(self, initial, goal, last_path):
        self.initial = initial
        self.goal = goal
        self.last_path = last_path
        self.clear()  # according to some policies, some transitions already used are eliminated to increase variety

        Problem.__init__(self, initial, goal)

    def clear(self):
        for move_name in self.last_path:  # path = move name list
            move = moves.get_move_by_name(move_name)  # retrieve the object from the name
            if move in transitions:
                transitions.remove(move)

    def check_goal(self, state, next_move):

        """control over goal achievement and compatibility"""

        current_move, counter, timer = state  # retrieve the state

        preconditions = next_move.get_preconditions()
        postconditions = current_move.get_postconditions()

        for pre in preconditions:  # for each precondition
            if pre in postconditions:  # if it is present in the postconditions
                if preconditions[pre] != postconditions[pre]:  # one not respected returns false all
                    return False

        return True

    def check_compatibility(self, state, next_move):

        """ this function checks the compatibility between the transition of two moves
            for each precondition of next_move, I iterate over current_move to see if it is present
            and whether the same is met. One discrepancy and return False
            + check on time
        """
        current_move, counter, timer = state  # retrieve the state

        preconditions = next_move.get_preconditions()
        postconditions = current_move.get_postconditions()

        timer_goal = self.goal[2]  # retrieve the desired timer asked during construction process

        for pre in preconditions:  # for each precondition
            if pre in postconditions:  # if it is present in the postconditions
                if preconditions[pre] != postconditions[pre]:  # one not respected returns false all
                    return False

        # time compatibility check
        if (timer + next_move.get_duration()) > (timer_goal + time_tolerance):
            return False

        """ other controls are not carried out at the moment...perhaps it could (in the future) be
            integrated some control on which move is better for another
            with some index there movement like entropy
        """

        return True

    def actions(self, state):

        """ starting with the state, I return a list with possible next steps """

        current_move, counter, timer = state  # retrieve the state
        result = []  # the result list is a list of strings

        for move in transitions:  # Iterate on all transitions to find possible sequences
            if self.check_compatibility(state, move) and (current_move != move):  # if the move is compatible and not just done I will add it
                result.append(move.get_name())

        return result

    def result(self, state, action):

        """ action is a string: retrieve the move and enter it into the state
            + have to calculate the new computed time and return updated state
        """

        current_move, counter, timer = state  # retrieve the state

        for m in transitions:  # retrieve the move object from its denominative
            if m.get_name() == action:
                move = m
                break

        if action == None:
            print("ERROR, no moves found!!!")
            return None

        counter += 1  # increase the counter of the moves (transitions) used
        timer += move.get_duration()  # increase the overall time of transitions

        return (move, counter, timer)  # return the new state

    def goal_test(self, state):

        """ devo controllare se:
            1) ho rispettato il vingolo di tempo dato
            2) ho rispettato il numero minimo di mosse
            3) la mossa corrente è compatibile con quella di goal
               --> alias la mossa goal è elencata come plausibile nel dizionario della corrente
            ritorno = True/False
        """

        current_move, counter, timer = state  # retrieve the state

        move_goal = self.goal[0]  # retrieve the goal state
        counter_goal = self.goal[1]  # retrieve the counter goal
        timer_goal = self.goal[2]  # retrieve from goal state the desired timer

        if (timer > (timer_goal - time_tolerance)) and (timer < (timer_goal + time_tolerance)):
            if counter >= counter_goal:
                if self.check_goal(state,
                                   move_goal):  # check the compatibility between the current state and the goal state
                    #print('timer: ' + str(counter))
                    return True

        if counter < counter_goal:  # If I have not reached the minimum transitions counter.
            return False

        return False

"""
    def h(self, node):  # metodo euristico da ridefinire!!!
        m, c, b = node.state
        return m + c - b
"""
