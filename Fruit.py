#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 11:30:07 2023

@author: wenxinyu
"""
from queue import PriorityQueue
from copy import deepcopy



def heuristic(state):
    count = 0
    for col in range(10):
        for row in range(2):
            if int(state[row][col][1:]) > int(state[row+1][col][1:]):
                count += 1
    return count

def successors(state):
    for row in range(3):
        for col in range(10):
            if row < 2 and state[row][col][0] == state[row+1][col][0]:
                yield swap(state, (row, col), (row + 1, col))
            if col < 9:
                yield swap(state, (row, col), (row, col + 1))
            # 添加水平交换条件
            if row < 2 and col < 9 and state[row][col][0] == state[row+1][col][0] and state[row+1][col+1][0] == state[row][col+1][0]:
                yield swap(state, (row, col), (row + 1, col + 1))



def swap(state, pos1, pos2):
    new_state = [list(col) for col in state]
    new_state[pos1[0]][pos1[1]], new_state[pos2[0]][pos2[1]] = new_state[pos2[0]][pos2[1]], new_state[pos1[0]][pos1[1]]
    return tuple(tuple(col) for col in new_state)







def a_star(initial_state):
    open_list = PriorityQueue()
    open_list.put((heuristic(initial_state), 0, initial_state, []))
    closed_list = set()

    while not open_list.empty():
        _, g, state, path = open_list.get()

        if state in closed_list:
            continue
        closed_list.add(state)

        if heuristic(state) == 0:
            return path + [state]

        for successor in successors(state):
            if successor not in closed_list:
                tentative_g = g + 1
                open_list.put((tentative_g + heuristic(successor), tentative_g, successor, path + [state]))

    return None

initial_state = (
    ('B8', 'A15', 'O1', 'A6', 'B9', 'O12', 'A17', 'B10', 'O3', 'A4'),
    ('A25', 'B18', 'O11', 'A16', 'B19', 'O22', 'A7', 'B20', 'O13', 'A14'),
    ('A5', 'B28', 'O21', 'A26', 'B29', 'O28', 'A27', 'B30', 'O23', 'A24'),
)

solution = a_star(initial_state)
if solution is not None:
    print("Solution found:")
    for step, state in enumerate(solution):
        print(f"Step {step}:")
        for col in state:
            print(col)
else:
    print("No solution found.")
