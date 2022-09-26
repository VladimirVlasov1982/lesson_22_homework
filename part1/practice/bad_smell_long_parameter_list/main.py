class Unit:

    def __init__(self, field, state):
        self.state = state
        self.field = field
        self.speed = 1
        self.y = 0
        self.x = 0

    def _get_speed(self):
        if self.state == "fly":
            return self.speed * 1.2
        elif self.state == "crawl":
            return self.speed * 0.5
        else:
            raise ValueError("Эк тебя раскарячило")

    def move(self, direction):
        speed = self._get_speed()

        if direction == "UP":
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == "DOWN":
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == "LEFT":
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == "RIGHT":
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)
