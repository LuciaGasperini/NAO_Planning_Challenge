#The Debuggers - NAO challenge 2022 - Giacomo Caroli & Lucia Gasperini


"""defining the class representing the single move of the NAO robot"""


class Move:

    def __init__(self, name, duration, preconditions, postconditions):
        self.name = name
        self.duration = duration
        self.preconditions = preconditions
        self.postconditions = postconditions

    def get_name(self):  # returns name of the move
        return self.name

    def get_duration(self):  # returns duration of the move
        return self.duration

    def get_preconditions(self):  # returns list of preconditions
        return self.preconditions

    def get_postconditions(self):  # returns list of postconditions
        return self.postconditions

    def __str__(self):
        return self.name + ' : ' + str(self.duration)

