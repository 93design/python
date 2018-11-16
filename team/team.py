#!/bin/python3

from random import choice

#create a list of players from a file
players = ["jamie","test"]

print('Players:', players)


teamNames = []
file = open('teams.txt', 'r')
teamNames = file.read().splitlines()
print('Team names:', teamNames)


teamA = []
teamB = []


while len(players) > 0:
  

  playerA = choice(players)
  teamA.append(playerA)

  players.remove(playerA)

  if players == []: 
    break
  
  playerB = choice(players)
  teamB.append(playerB)

  players.remove(playerB)


teamNameA = choice(teamNames)
teamNames.remove(teamNameA)
teamNameB = choice(teamNames)
teamNames.remove(teamNameB)

print('\nHere are your teams:\n')
print(teamNameA, teamA)
print(teamNameB, teamB)