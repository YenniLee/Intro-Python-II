# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room): 
        self.name = name 
        self.current_room = current_room
        self.items = []
    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else: 
            print('Cannot go that way...')
    def add_items(self, name):
        items_in_room = self.current_room.get_items()
        if len(items_in_room): 
            for item in items_in_room:
                if item.name:
                    self.current_room.items.remove(item)
                    self.items.append(item)
                    item.on_take()
    def drop_items(self, name):
        if len(self.items):
            for item in self.items:
                self.current_room.items.append(item)
                self.items.remove(item)
                item.on_drop()
    def current_inventory(self):
        if len(self.items) > 0:
                print('You have the following items:')
                for item in self.items:
                    print(item.name)
        else:
            print('You have no items in your inventory.')