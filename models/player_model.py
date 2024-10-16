class Player:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.x_change = 0  # A mudança na posição X é inicializada como 0

    def move(self, delta_time):
        self.x += self.x_change
        # Limitar o movimento do player para não sair da tela
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736
