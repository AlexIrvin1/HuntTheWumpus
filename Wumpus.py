# Alex Irvin
# Wumpus

import random

class Room:
    def __init__(self, number):
        self.number = number
        self.tunnels = []
        self.has_pit = False
        self.has_bats = False
        self.has_wumpus = False
    
    def connect(self, other_room):
        # Connect this room to another room (two-way connection)
        self.tunnels.append(other_room)
        other_room.tunnels.append(self)

# Create the cave system

def create_cave_system():
    rooms = {i: Room(i) for i in range(1, 13)}

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
            if rooms[neighbor] not in rooms[room].tunnels:
                rooms[room].connect(rooms[neighbor])
    return rooms

# Scatter hazards around the cave
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
        self.arrows = 3

    def move(self, target_room):
        if target_room in self.current_room.tunnels:
            self.current_room = target_room
        else:
            print("You can't move that way!")

    def shoot_arrow(self, target_room, wumpus_room):
        if target_room in self.current_room.tunnels:
            self.arrows -= 1
            if target_room == wumpus_room:
                print("You hear a satisfying roar as your arrow hits the Wumpus! You win!")
                return True  # Game over, Wumpus is defeated
            else:
                print("Your arrow echoes through the tunnels, but the Wumpus lives!")
                if self.arrows == 0:
                    print("You're out of arrows! Game Over!")
                    return False  # Game over, no arrows left
        else:
            print("You can't shoot that way!")
        return None

def give_hints(player):
    # Check for nearby pits
    if any(room.has_pit for room in player.current_room.tunnels):
        print("You feel a cold breeze... something is definitely down there.")
    
    # Check for nearby bats
    if any(room.has_bats for room in player.current_room.tunnels):
        print("You hear the sound of frantic wings flapping in the darkness.")
    
    # Check for nearby Wumpus
    if any(room.has_wumpus for room in player.current_room.tunnels):
        print("You smell something awful... like Bryson Groves.")

# Check for nearby hazards
def check_for_hazards(player):
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

# Main game loop
def main():
    rooms = create_cave_system()
    wumpus_room = place_hazards(rooms)
    player = Player(random.choice(list(rooms.values())))

    while True:
        print(f"\nYou are in Room {player.current_room.number}.")
        print(f"Connected rooms: {[r.number for r in player.current_room.tunnels]}")
        print(f"Arrows remaining: {player.arrows}")
        give_hints(player)

        # Move or shoot
        action = input("Move or Shoot? (m/s): ").strip().lower()
        if action == 'm':
            try:
                target_number = int(input("Enter room number to move to: "))
                target_room = rooms.get(target_number)
                if target_room:
                    player.move(target_room)
                    if not check_for_hazards(player):
                        break
                else:
                    print("Invalid room number.")
            except ValueError:
                print("Please enter a valid room number.")

        elif action == 's':
            try:
                target_number = int(input("Enter room number to shoot into: "))
                target_room = rooms.get(target_number)
                if target_room:
                    result = player.shoot_arrow(target_room, wumpus_room)
                    if result is True or result is False:
                        break
                else:
                    print("Invalid room number.")
            except ValueError:
                print("Please enter a valid room number.")

        else:
            print("Choose 'm' to move or 's' to shoot.")

# Run the game
main()
