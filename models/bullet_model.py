class Bullet:
    def __init__(self, image, x, y, speed):
        self.image = image  # Imagem da bala
        self.x = x  # Posição inicial X
        self.y = y  # Posição inicial Y
        self.speed = speed  # Velocidade da bala
        self.state = "ready"  # Estado da bala (ready/fired)

        # Definir o retângulo da bala (hitbox)
        self.rect = self.image.get_rect()  # Retângulo com base na imagem
        self.rect.midtop = (x, y)  # Inicializa o retângulo com a posição

    def fire(self, x):
        """Faz o disparo da bala"""
        self.state = "fired"
        self.x = x  # A posição horizontal da bala é a mesma do jogador
        self.rect.midtop = (self.x, self.y)  # Atualiza a posição do rect

    def move(self):
        """Move a bala se estiver disparada"""
        if self.state == "fired":
            self.y -= self.speed
            self.rect.y = self.y  # Atualiza a posição do rect da bala

        # Resetar a bala se sair da tela
        if self.y <= 0:
            self.reset()

    def reset(self):
        """Reseta a bala após o disparo"""
        self.state = "ready"
        self.y = 480  # Posição inicial para o disparo subsequente
        self.rect.midtop = (self.x, self.y)  # Atualiza a posição do rect
