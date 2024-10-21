class Player:
    def __init__(self, image, x, y):
        self.image = image  # Imagem do jogador
        self.x = x  # Posição inicial X
        self.y = y  # Posição inicial Y
        self.x_change = 0  # Mudança na posição X para o movimento

        # Definir o retângulo do jogador (hitbox)
        self.rect = self.image.get_rect()  # Cria o rect com base no tamanho da imagem
        self.rect.topleft = (self.x, self.y)  # Define a posição inicial do rect

    def move(self, delta_time):
        """Movimenta o jogador com base na entrada"""
        self.x += self.x_change  # Atualiza a posição X do jogador
        self.rect.x = self.x  # Atualiza a posição do rect com a nova posição
