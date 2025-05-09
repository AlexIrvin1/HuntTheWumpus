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

    # Manually connect the rooms to match the dodecahedron structure
    connections = {
        1: [2, 5, 6],
        2: [1, 3, 8],
        3: [2, 4, 10],
        4: [3, 5, 12],
        5: [1, 4, 7],
        6: [1, 7, 11],
        7: [5, 6, 8],
        8: [2, 7, 9],
        9: [8, 10, 12],
        10: [3, 9, 11],
        11: [6, 10, 12],
        12: [4, 9, 11]
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

