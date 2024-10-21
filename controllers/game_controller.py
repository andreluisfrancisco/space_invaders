import pygame
import random
from models.player_model import Player
from models.enemy_model import Enemy
from models.bullet_model import Bullet
from services.collision_service import CollisionService

class GameController:
    def __init__(self):
        self.player = Player(pygame.image.load('assets/player.png'), 370, 480)
        self.bullet = Bullet(pygame.image.load('assets/bullet.png'), 0, 480, 10)
        self.enemies = [Enemy(pygame.image.load('assets/enemy.png'), random.randint(0, 735), random.randint(50, 150), 4, 40) for _ in range(6)]
        self.collision_service = CollisionService()
        self.score = 0
        self.player_speed = 200  # Velocidade de movimento (pixels por segundo)

    def move_entities(self, delta_time):
        """Atualiza a posição das entidades com base no delta_time"""
        self.player.move(delta_time)  # Passa o delta_time para ajustar o movimento do player
        for enemy in self.enemies:
            enemy.move()

    def check_collisions(self):
        # Verifica colisão entre a bala e os inimigos
        for enemy in self.enemies:
            if self.bullet.rect.colliderect(enemy.rect):
                # Quando a bala colide com o inimigo
                print("Colisão detectada: Bala e Inimigo")
                self.enemies.remove(enemy)  # Remove inimigo após colisão
                self.bullet.reset()  # Reseta a bala ou a remove
                self.score += 1

        # Verifica colisão entre o jogador e os inimigos
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                # Quando o jogador colide com o inimigo
                print("Colisão detectada: Jogador e Inimigo")
                self.game_over()

    def fire_bullet(self):
        """Fire bullet if ready"""
        if self.bullet.state == "ready":
            self.bullet.fire(self.player.x)

    def handle_input(self, delta_time):
        """Handle continuous input for smooth movement"""
        keys = pygame.key.get_pressed()  # Get the current state of all keys

        # Ajusta a mudança de posição com base no delta_time
        if keys[pygame.K_LEFT]:
            self.player.x_change = -self.player_speed * delta_time  # Move left
        elif keys[pygame.K_RIGHT]:
            self.player.x_change = self.player_speed * delta_time   # Move right
        else:
            self.player.x_change = 0  # Stop movement if no keys are pressed

    def game_over(self):
        """Lógica de fim de jogo"""
        print("Fim de Jogo!")
        pygame.quit()  # Encerra o pygame
        quit()  # Encerra o programa
