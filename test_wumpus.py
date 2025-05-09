# Alex Irvin
# Wumous Test

import unittest
from wumpus import Room, create_cave_system, place_hazards, Player

class TestHuntTheWumpus(unittest.TestCase):

    def test_room_connections(self):
        rooms = create_cave_system()
        # Check if room 1 connects to 3, 8, and 11
        self.assertEqual(sorted([r.number for r in rooms[1].tunnels]), [3, 8, 11])
        # Check if room 7 connects to 2, 8, and 10
        self.assertEqual(sorted([r.number for r in rooms[7].tunnels]), [2, 8, 10])

    def test_place_hazards(self):
        rooms = create_cave_system()
        wumpus_room = place_hazards(rooms)
        # Check if Wumpus is in one of the rooms
        wumpus_count = sum(room.has_wumpus for room in rooms.values())
        self.assertEqual(wumpus_count, 1)

        # Check if there are exactly 2 pits and 2 bat rooms
        pit_count = sum(room.has_pit for room in rooms.values())
        bat_count = sum(room.has_bats for room in rooms.values())
        self.assertEqual(pit_count, 2)
        self.assertEqual(bat_count, 2)

    def test_player_movement(self):
        rooms = create_cave_system()
        player = Player(rooms[1])
        # Move to a connected room
        player.move(rooms[3])
        self.assertEqual(player.current_room, rooms[3])

        # Try moving to a non-conne
