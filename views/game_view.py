import pygame

class GameView:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def draw_entity(self, entity):
        self.screen.blit(entity.image, (entity.x, entity.y))

    def show_score(self, score, x, y):
        score_text = self.font.render(f"Score : {score}", True, (255, 255, 255))
        self.screen.blit(score_text, (x, y))

    def game_over(self):
        over_font = pygame.font.Font('freesansbold.ttf', 64)
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        self.screen.blit(over_text, (200, 250))
