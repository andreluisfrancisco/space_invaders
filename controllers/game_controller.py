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
        """Check for bullet-enemy collisions"""
        for enemy in self.enemies:
            if self.collision_service.is_collision(self.bullet, enemy) and self.bullet.state == "fire":
                self.bullet.y = 480
                self.bullet.state = "ready"
                self.score += 1
                enemy.reset_position()

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
