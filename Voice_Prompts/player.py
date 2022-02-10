class Player():
    def __init__(self):
        self._name = None
        self._hp = 100
        self._actions = ["talk", "attack",]
        self._TORCH = False
        self._SWORD = False
        self._GOLD = False
        self._player_location = 'Back of Cave'

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_hp(self):
        return self._hp
    
    def set_hp(self, hp):
        self._hp = hp

    def get_actions(self):
        return self._actions

    def get_TORCH(self):
        return self._TORCH
    
    def set_TORCH(self):
        self._TORCH = True

    def get_SWORD(self):
        return self._SWORD

    def set_SWORD(self):
        self._SWORD = True

    def get_GOLD(self):
        return self._GOLD

    def set_GOLD(self):
        self._GOLD = True

    def get_player_location(self):
        return self._player_location

    def update_location(self, new_location):
        self._player_location = new_location

    def __str__(self):
        return "Player: " + str(self._name) + " HP: " + str(self._hp)
