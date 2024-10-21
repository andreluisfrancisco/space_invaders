class Enemy:
    def __init__(self, image, x, y, speed_x, speed_y):
        self.image = image  # Imagem do inimigo
        self.x = x  # Posição inicial X
        self.y = y  # Posição inicial Y
        self.speed_x = speed_x  # Velocidade de movimento horizontal
        self.speed_y = speed_y  # Velocidade de movimento vertical

        # Definir o retângulo do inimigo (hitbox)
        self.rect = self.image.get_rect()  # Cria o rect com base no tamanho da imagem
        self.rect.topleft = (self.x, self.y)  # Define a posição inicial do rect

    def move(self):
        """Movimenta o inimigo e atualiza sua posição"""
        self.x += self.speed_x
        self.rect.x = self.x  # Atualiza a posição do rect com base na nova posição

        # Faz o inimigo mudar de direção quando atinge as bordas da tela
        if self.x <= 0 or self.x >= 735:  # Limites da tela
            self.speed_x *= -1  # Inverte a direção
            self.y += self.speed_y  # Move para baixo
            self.rect.y = self.y  # Atualiza a posição vertical do rect
