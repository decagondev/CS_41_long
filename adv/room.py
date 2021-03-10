# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.is_lit = False # denote if the room is light enough to see items
        self.contents = []
