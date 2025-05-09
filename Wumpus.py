# Alex Irvin
# Wumpus

import random

class Room:
    def __innit__(self, number):
        self.number = number
        self.tunnels = []
        self.has_pit = False
        self.has_bats = False
        self.has_wumpus = False
    
    def connect(self, other_room):
        self.tunnels.append(other_room)
        other_room.tunnels.append(self)
        
def create_cave_system():
    # Create all rooms
    rooms = {i: Room(i) for i in range(1, 21)}

    connections = {
        1: [3, 8, 11],
        2: [4, 7, 12],
        3: [1, 6, 10],
        4: [2, 5, 9],
        5: [4, 6, 11],
        6: [3, 5, 12],
        7: [2, 8, 10],
        8: [1, 7, 9],
        9: [4, 8, 12],
        10: [3, 7, 11],
        11: [1, 5, 10],
        12: [2, 6, 9]
    }

    for room, neighbors in connections.items():
        for neighbor in neighbors:
            rooms[room].connect(rooms[neighbor])

    return rooms

def place_hazards(rooms):
    # Add pits
    for _ in range(2):
        random.choice(list(rooms.values())).has_pit = True

    # Add bats
    for _ in range(2):
        random.choice(list(rooms.values())).has_bats = True

    # Add the Wumpus
    wumpus_room = random.choice(list(rooms.values()))
    wumpus_room.has_wumpus = True
    return wumpus_room

class Player:
    def __init__(self, start_room):
        self.current_room = start_room

    def move(self, target_room):
        if target_room in self.current_room.tunnels:
            self.current_room = target_room
        else:
            print("You can't move that way!")

def checkHazards(player):
    if player.current_room.has_pit:
        print("You fell into a bottomless pit! GG's Game Over!")
        return False
    elif player.current_room.has_bats:
        print("Giant bats whisk you away to a random room!")
        player.current_room = random.choice(list(player.current_room.tunnels))
    elif player.current_room.has_wumpus:
        print("You stumbled into the Wumpus's lair! Game Over!")
        return False
    return True
