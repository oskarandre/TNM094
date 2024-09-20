import pygame

class ParticleMassController:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Particle Mass Controller")
        self.clock = pygame.time.Clock()

        # Font initialization
        pygame.font.init()
        self.font = pygame.font.Font(None, 24)

        # Initial value for particle mass
        self.particle_mass = 10000

    def run(self):
        running = True
        while running:
            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            # Draw text input box
            text_surface = self.font.render(f"Particle Mass: {self.particle_mass}", True, (0, 0, 0))
            self.screen.blit(text_surface, (20, 20))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def get_particle_mass(self):
        return self.particle_mass