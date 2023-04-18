#The Debuggers - NAO challenge 2022 - Giacomo Caroli & Lucia Gasperini


from move import Move

""" each move is coded with a name (file name) ,calculated duration, 
    preconditions and postconditions (present only if necessary)
"""

stand = Move('11-Stand', 3.38, {'standing': True}, {'standing': True})
arms_opening = Move('4-Arms_opening', 12.70, {}, {})
rotation_footL = Move('13-Rotation_foot_LLeg', 12.61, {'standing': True}, {'standing': True})
move_backward = Move('8-Move_backward', 4.82, {'standing': True}, {'standing': True})
crouch = Move('6-Crouch', 4.18, {'standing': True}, {'standing': True})
diagonal_left = Move('9-Diagonal_left', 6.90, {'standing': True}, {'standing': True})
right_arm = Move('2-Right_arm', 15.18, {}, {})
sit = Move('16-Sit', 21.58, {'standing': True}, {'standing': False})
move_forward = Move('7-Move_forward', 6.45, {'standing': True}, {'standing': True})
union_arms = Move('5-Union_arms', 8.90, {}, {})
diagonal_right = Move('10-Diagonal_right', 5.00, {'standing': True}, {'standing': True})
double_movement = Move('3-Double_movement', 10.88, {'standing': True}, {'standing': True})
rotation_footR = Move('12-Rotation_foot_RLeg', 11.32, {'standing': True}, {'standing': True})
stand_zero = Move('15-StandZero', 4.56, {'standing': True}, {'standing': True})
stand_init = Move('14-StandInit', 5.18, {'standing': True}, {'standing': True})
sit_relax = Move('17-SitRelax', 23.18, {'standing': True}, {'standing': False})
rotation_handgun = Move('1-Rotation_handgun_object', 5.76, {'standing': True}, {'standing': True})

Rhythm = Move('Rhythm', 2.95,  {'standing': True},  {'standing': True}),

wave = Move('Wave', 3.72, {}, {})
glory = Move('Glory', 3.28,  {}, {})
clap = Move('Clap', 4.10,  {}, {})
joy = Move('Joy', 4.50,  {}, {})
bow = Move('Bow', 3.86, {'standing': True}, {'standing': True})

#nuove obbligatorie
wipe_forehead = Move('Wipe_Forehead', 5.12, {}, {})
hello = Move('Hello', 4.64, {}, {})

#nuove transizioni
air_guitar = Move('AirGuitar', 4.04, {'standing': True}, {'standing': True})
arm_dance = Move('ArmDance', 5.46, {'standing': True}, {'standing': True})
happy_birthday = Move('Happy_Birthday', 9.86, {'standing': True}, {'standing': True})
sprinkler = Move('Sprinkler', 9.76, {'standing': True}, {'standing': False})

hands_on_hips = Move('Hands_on_Hips', 1.78, {}, {})
cameOn = Move('ComeOn', 3.52, {}, {})
dab = Move('Dab', 6.11, {'standing': True}, {'standing': True})
danceMove = Move('DanceMove', 6.11, {'standing': True}, {'standing': True})
pulpFiction = Move('PulpFiction', 5.54, {}, {})
theRobot = Move('TheRobot', 6.06, {'standing': True}, {'standing': True})

shuffle = Move('Shuffle', 6.79, {'standing': True}, {'standing': True})

#Duplicates to increase variety
hands_on_hips2 = Move('Hands_on_Hips2', 1.78, {}, {})
cameOn2 = Move('ComeOn2', 3.52, {}, {})
air_guitar2 = Move('AirGuitar2', 4.04, {'standing': True}, {'standing': True})
hello2 = Move('Hello2', 4.64, {}, {})


add_on = [wave,glory,joy,bow,hands_on_hips2, clap]


def get_transitions():

    list = [stand, arms_opening,  move_backward, move_forward, diagonal_right, diagonal_left,
     right_arm, union_arms, double_movement, air_guitar,
     hands_on_hips, cameOn, danceMove, theRobot, shuffle, rotation_handgun,  sprinkler, arm_dance, pulpFiction , happy_birthday, dab] #rotation_footR, rotation_footL,

    list = list + add_on

    return list



def get_starting_move():
    return stand_init

def get_ending_move():
    return crouch

def get_compulsory():

    return [stand_init, sit, sit_relax, stand, wipe_forehead, stand_zero, hello, crouch ]


def get_move_by_name(name):
    list1 = get_transitions()
    list2 = get_compulsory()
    for move in list1:
        if move.get_name() == name:
            return move
    for move in list2:
        if move.get_name() == name:
            return move


def calculate_time(path): # calculate the total duration of a path
    time = 0.0
    for move_name in path:
        time += get_move_by_name(move_name).get_duration()
    return time
