import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, DARK_BLUE, WHITE

class GameManager:
    """
    Game manager class that manages the game rounds just like Pong.
    """
    def __init__(self, screen, font, title_font):
        self.screen = screen
        self.font = font
        self.title_font = title_font
        self.point_scored_time = 0
        self.point_pause_duration = 1000  # a second pause
        self.resetGame()
        
    def resetGame(self):
        self.score_left = 0
        self.score_right = 0
        self.round = 1
        self.rounds_won_left = 0
        self.rounds_won_right = 0
        self.game_state = "START"

    def resetRound(self):
        self.score_left = 0
        self.score_right = 0

    def point_scored(self, ball):
        self.point_scored_time = pygame.time.get_ticks()
        ball.reset()
        self.checkRoundOver()

    def checkRoundOver(self):
        winning_score_per_round = 3
        rounds_to_win_game = 3

        if self.score_left >= winning_score_per_round or self.score_right >= winning_score_per_round:
            if self.score_left > self.score_right:
                self.rounds_won_left += 1
            else:
                self.rounds_won_right += 1

            if self.rounds_won_left == rounds_to_win_game or self.rounds_won_right == rounds_to_win_game:
                self.game_state = "GAME_OVER"
            else:
                self.game_state = "ROUND_OVER"
                self.round += 1

            self.score_left = 0
            self.score_right = 0
        else:
            self.game_state = "PLAYING"

    def startNextRoundOrGame(self):
        if self.game_state == "START" or self.game_state == "GAME_OVER":
            self.resetGame()
        elif self.game_state == "ROUND_OVER":
            self.resetRound()
        self.game_state = "PLAYING"

    def drawStartScreen(self):
        title_surf = self.title_font.render("WELCOME TO AIR HOCKEY!", True, DARK_BLUE)
        start_surf = self.font.render("Press SPACE to start the game!", True, DARK_BLUE)
        particle_mode_surf_0 = self.font.render("Press 0: No Particle Emissions", True, DARK_BLUE)
        particle_mode_surf_1 = self.font.render("Press 1: Simple Particle Emissions", True, DARK_BLUE)
        particle_mode_surf_2 = self.font.render("Press 2: Complex Particle Emissions", True, DARK_BLUE)
        smoke_mode_surf_3 = self.font.render("Press 3: Complex Particle Emissions: Smoke", True, DARK_BLUE)
        
        self.screen.blit(title_surf, (SCREEN_WIDTH // 2 - title_surf.get_width() // 2, SCREEN_HEIGHT // 3))
        self.screen.blit(start_surf, (SCREEN_WIDTH // 2 - start_surf.get_width() // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(particle_mode_surf_0, (SCREEN_WIDTH // 2 - particle_mode_surf_0.get_width() // 2, SCREEN_HEIGHT // 2 + 40))
        self.screen.blit(particle_mode_surf_1, (SCREEN_WIDTH // 2 - particle_mode_surf_1.get_width() // 2, SCREEN_HEIGHT // 2 + 80))
        self.screen.blit(particle_mode_surf_2, (SCREEN_WIDTH // 2 - particle_mode_surf_2.get_width() // 2, SCREEN_HEIGHT // 2 + 120))
        self.screen.blit(smoke_mode_surf_3, (SCREEN_WIDTH // 2 - smoke_mode_surf_3.get_width() // 2, SCREEN_HEIGHT // 2 + 160))

        
        
        
    def drawGameScreen(self, paddle_left, paddle_right, ball):
        paddle_left.draw(self.screen)
        paddle_right.draw(self.screen)
        ball.draw(self.screen)

        pygame.draw.line(self.screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 2)

        score_left_surf = self.font.render(f"{self.score_left}", True, DARK_BLUE)
        score_right_surf = self.font.render(f"{self.score_right}", True, DARK_BLUE)
        self.screen.blit(score_left_surf, (SCREEN_WIDTH // 4, 20))
        self.screen.blit(score_right_surf, (3 * SCREEN_WIDTH // 4, 20))

        round_surf = self.font.render(f"Round {self.round}", True, DARK_BLUE)
        self.screen.blit(round_surf, (SCREEN_WIDTH // 2 - round_surf.get_width() // 2, 20))

        wins_left_surf = self.font.render(f"Wins: {self.rounds_won_left}", True, DARK_BLUE)
        wins_right_surf = self.font.render(f"Wins: {self.rounds_won_right}", True, DARK_BLUE)
        self.screen.blit(wins_left_surf, (20, SCREEN_HEIGHT - 40))
        self.screen.blit(wins_right_surf, (SCREEN_WIDTH - wins_right_surf.get_width() - 20, SCREEN_HEIGHT - 40))

        if self.game_state == "ROUND_OVER":
            round_over_surf = self.title_font.render("Round Over!", True, DARK_BLUE)
            next_round_surf = self.font.render("Press SPACE for next round", True, DARK_BLUE)
            self.screen.blit(round_over_surf, (SCREEN_WIDTH // 2 - round_over_surf.get_width() // 2, SCREEN_HEIGHT // 3))
            self.screen.blit(next_round_surf, (SCREEN_WIDTH // 2 - next_round_surf.get_width() // 2, SCREEN_HEIGHT // 2))

    def drawGameOverScreen(self):
        winner = "Left" if self.rounds_won_left > self.rounds_won_right else "Right" if self.rounds_won_right > self.rounds_won_left else "Tie"

        game_over_surf = self.title_font.render("Game Over!", True, DARK_BLUE)
        winner_surf = self.font.render(f"Winner: {winner}", True, DARK_BLUE)
        restart_surf = self.font.render("Press SPACE to restart", True, DARK_BLUE)

        self.screen.blit(game_over_surf, (SCREEN_WIDTH // 2 - game_over_surf.get_width() // 2, SCREEN_HEIGHT // 3))
        self.screen.blit(winner_surf, (SCREEN_WIDTH // 2 - winner_surf.get_width() // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(restart_surf, (SCREEN_WIDTH // 2 - restart_surf.get_width() // 2, SCREEN_HEIGHT * 2 // 3))

    def update(self, ball, paddle_left, paddle_right):
        current_time = pygame.time.get_ticks()
        
        if self.game_state == "PLAYING":
            if current_time - self.point_scored_time > self.point_pause_duration:
                ball.move()
                
                if ball.collidesWithPaddle(paddle_left) or ball.collidesWithPaddle(paddle_right):
                    ball.handlePaddleCollision(paddle_left if ball.collidesWithPaddle(paddle_left) else paddle_right)

                if ball.y - ball.radius <= 0 or ball.y + ball.radius >= SCREEN_HEIGHT:
                    ball.dy *= -1

                if ball.x - ball.radius <= 0:
                    self.score_right += 1
                    self.point_scored(ball)
                elif ball.x + ball.radius >= SCREEN_WIDTH:
                    self.score_left += 1
                    self.point_scored(ball)