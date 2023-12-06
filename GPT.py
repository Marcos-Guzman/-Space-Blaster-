import pygame
import sys

class Scorer:
    def __init__(self):
        self.score = 0

    def add_points(self, points):
        """Add points to the current score."""
        if points < 0:
            print("Points cannot be negative. Please provide a positive value.")
        else:
            self.score += points

    def subtract_points(self, points):
        """Subtract points from the current score."""
        if points < 0:
            print("Points cannot be negative. Please provide a positive value.")
        elif points > self.score:
            print("Cannot subtract more points than the current score.")
        else:
            self.score -= points

    def get_score(self):
        """Return the current score."""
        return self.score

# Create an instance of the Scorer class
game_scorer = Scorer()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Add and subtract points (you can modify this based on your input method)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        game_scorer.add_points(10)
    if keys[pygame.K_s]:
        game_scorer.subtract_points(5)

    # Get the current score
    current_score = game_scorer.get_score()

    # Display the score on the screen in the top-left corner
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {current_score}", True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(30)
