class Player():
    def __init__(self):
        self._name = None
        self._hp = 100
        self._actions = ["talk", "attack", "flee"]
        self._movement = ["forward", "backward", "left", "right"]

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

    def get_movement(self):
        return self._movement

    def __str__(self):
        return "Player: " + str(self._name) + " HP: " + str(self._hp) + " Actions: " + str(self._actions)
