import pygame
from controllers.game_controller import GameController
from views.game_view import GameView

def main():
    # Inicialização do pygame
    pygame.init()

    # Configuração da tela
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load('assets/ufo.png')
    pygame.display.set_icon(icon)

    # Inicializa o controlador e a visão
    game_controller = GameController()
    game_view = GameView(screen)

    # Define o clock para controlar a taxa de FPS
    clock = pygame.time.Clock()

    running = True
    while running:
        # Limpa a tela a cada frame
        screen.fill((0, 0, 0))

        # Calcula o delta_time (tempo entre frames em segundos)
        delta_time = clock.tick(60) / 1000.0 
        
        # Verifica eventos para fechar o jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Disparo da bala
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_controller.fire_bullet()

        # Lidar com entrada do usuário para movimento suave
        game_controller.handle_input(delta_time)

        # Movimentar entidades
        game_controller.move_entities(delta_time)
        game_controller.bullet.move()

        # Desenhar entidades na tela
        game_view.draw_entity(game_controller.player)
        game_view.draw_entity(game_controller.bullet)

        for enemy in game_controller.enemies:
            game_view.draw_entity(enemy)

        # Verificar colisões e exibir a pontuação
        game_controller.check_collisions()
        game_view.show_score(game_controller.score, 10, 10)

        # Atualizar a tela
        pygame.display.update()

if __name__ == "__main__":
    main()
