import random

class Enemy:
    def __init__(self, image, x, y, x_change, y_change):
        self.image = image
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change

    def move(self):
        self.x += self.x_change
        if self.x <= 0 or self.x >= 736:
            self.x_change *= -1
            self.y += self.y_change

    def reset_position(self):
        self.x = random.randint(0, 735)
        self.y = random.randint(50, 150)
