#The Debuggers - NAO challenge 2022 - Giacomo Caroli & Lucia Gasperini

import moves
from nao import Nao
from reporting import *
from search import *
import subprocess
import os
import sys
from time import sleep

def play_music(path): # music playback by subprocess
    # subprocess.Popen(['mpg123', '-q', path]).wait()
    subprocess.Popen(['mpg123', '-q', path])

# state = (current_move,counter,timer)

minimum_moves_counter = 2
compulsory = moves.get_compulsory() # return [stand_init, sit, sit_relax, stand, wipe_forehead, stand_zero, hello, crouch ]

""" We have to iterate over all the mandatory moves and for each one invoke the search algorithm.
    To liven things up a bit, we chose to require that the mandatory moves be
    executed within certain time instants (times[])
"""

final_path = []

# return [stand_int, sit, sit_relax, stand, wipe_forehead, stand_zero, hello, crouch ]
times = [25.0, 20.0, 18.0, 10.0, 15.0, 10.0, 15.0]  # sum of all (7) these + compulsory move times = music time <= 3 minutes

last_path = []

for i in range(len(compulsory) - 1): # iterate for each mandatory move

    print(i)

    #retrieval start and goal state
    starting_state = (compulsory[i], 0, 0.0)
    goal_state = (compulsory[i + 1], minimum_moves_counter, times[i])

    final_path.append(str(compulsory[i].get_name()))

    # generate the solution via search algorithm
    n = Nao(starting_state, goal_state, last_path)
    soln = breadth_first_tree_search(n)
    path = path_actions(soln)

    print(path)

    time = moves.calculate_time(path)
    print(str(time))

    last_path += path

    final_path += path  # update the complete list with calculated moves

final_path.append(moves.crouch.get_name()) # add to the list the final move

print(final_path)
time = moves.calculate_time(final_path)

print('Time: ' + str(time / 60.0))

# now iterate for each item in the list to launch the respective files in python
# 1) retrieval of the directory, IP and port

directory = os.getcwd() #working folder
ip = sys.argv[1]
port = sys.argv[2]

#print(directory)

moves_foler = directory + '/MOSSE_ROBOT_NAO/'
music_path = directory + '/music.mp3'

print(moves_foler)
print(music_path)

print('connecting to ip: ' + ip + ' port: ' + port)

play_music(music_path) # play music in subprocess

sleep(1) #for syncronize the song with the movements

for move_name in final_path:  # for each element of final_path
    print('running: ' + move_name)
    os.system("python2 " + moves_foler + move_name + '.py ' + ip + ' ' + port)

"""
report([
        breadth_first_tree_search,
        breadth_first_graph_search,
        #depth_first_tree_search,
        depth_first_graph_search,
        astar_search
    ],
        [n1])
"""
