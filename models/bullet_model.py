class Bullet:
    def __init__(self, image, x, y, y_change):
        self.image = image
        self.x = x
        self.y = y
        self.y_change = y_change
        self.state = "ready"

    def fire(self, x):
        self.x = x
        self.state = "fire"

    def move(self):
        if self.state == "fire":
            self.y -= self.y_change
        if self.y <= 0:
            self.state = "ready"
            self.y = 480
