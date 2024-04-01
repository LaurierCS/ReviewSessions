class hashset:
    def __init__(self, load=2, capacity=100):

        self._load = load
        # how much on average each slot can take

        self._items = 0
        self._capacity = capacity
        self._slots = [[] for i in range(capacity)]

    def _find_key(self, item):
        # key > len(self._slots)
        # runtime error

        key = hash(item) % self._capacity
        # distributes hashes evenly against 1 to capacity
        return self._slots[key]

    def insert(self, item):
        # maintain uniqueness
        # maintain speed

        slot = self._find_key(item)

        canInsert = not item in slot

        if canInsert:
            # load * slots = total capacity of hashset
            # if items > total capacity -> slow :[

            slot.append(item)
            self._items += 1

            if self._items > self._load * self._capacity:
                self._rehash()

        return canInsert

    def _rehash(self):
        temp = self._slots

        self._capacity = self._capacity * 2 + 1

        self._slots = [[] for i in range(self._capacity)]

        while temp:
            curSlot = temp.pop()

            while curSlot:
                curItem = curSlot.pop()
                key = self._find_key(curItem)
                self._slots[key].append(curItem)
        return

    def remove(self, key):
        slot = self._find_key(self, key)
        removed = None
        if key in slot:
            self._items -= 1
            removed = slot.pop(slot.index(key))
        return removed


class studentApartment:
    def __init__(self, ppl_per_room=10, number_rooms=5) -> None:
        self.ppl_per_room = ppl_per_room
        self.number_rooms = number_rooms
        self.total_people = 0
        self.apartment_capacity = self.number_rooms * self.ppl_per_room
        self.apartment = []

        for i in range(number_rooms):

            room = []
            self.apartment.append(room)

    def _find_room(self, person):
        key = hash(person) % self.number_rooms
        room = self.apartment[key]
        return room

    def _kick_out_guest(self, person):
        room = self._find_room(person)
        kicked_out = False
        if person in room:
            kicked_out = True
            self.total_people -= 1
            self.room.pop(self.room.index(person))
        return kicked_out

    def _invite_guest(self, person):
        room = self._find_room(person)
        if person in room:
            print("This person is already in the room!")
            can_enter = False
        else:
            room.append(person)
            self.total_people += 1
            if self.total_people > self.apartment_capacity:
                print("We gotta find a new apartment!")

    def _find_new_apartment(self):
        self.number_rooms = self.number_rooms * 2 + 1
        self.apartment = []
        self.apartment_capacity = self.number_rooms * self.ppl_per_room

        for i in range(self.number_rooms):
            room = []
            self.apartment.append(room)

        moving_truck = self.apartment

        moving_truck.drive_to_new_apartment()

        while moving_truck:
            unload_box = moving_truck.pop()

            while unload_box:
                item_from_box = unload_box.pop()
                room = self._find_room()
                room.append(item_from_box)
        return


class hashmap:
    def __init__(self, load=2, capacity=100):
        self._load = load
        self._capacity = capacity
        self._slots = [[] for i in range(capacity)]
        self._items = 0

    def _find_slot(self, key):
        key = hash(key)
        key %= self._capacity
        return self._slots[key]

    def _assign(self, key, value):
        slot = self._find_slot(key)
        found = False
        for i in range(len(slot)):
            if slot[i][0] == key:
                slot[i][1] = value
                found = True
        if found:
            slot.append([key, value])
            self._items += 1
            if self._itesm > self._load * self._capacity:
                self.rehash()
        return

    def rehash(self):
        temp = self._slots
        self._capacity = self._capacity * 2 + 1
        self._slots = [[] for i in range(self._capacity)]
        while temp:
            slot = temp.pop()
            while slot:
                key, value = slot.pop()
                slot = self._find_slot(key)
                slot.append([key, value])
        return

    def is_in(self, key):
        slot = self._find_slot(key)
        found = False
        for i in range(len(slot)):
            if slot[i][0] == key:
                found = True
        return found

    def query(self, key):
        slot = self._find_slot(key)
        value = None
        for i in range(len(slot)):
            if slot[i][0] == key:
                value = slot[i][1]
        return value
