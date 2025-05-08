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