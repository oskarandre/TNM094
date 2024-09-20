import pygame

class Renderer:
    #==================Initialize===================================================================================================================================
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Particle System")
        self.clock = pygame.time.Clock()

       
    #==================Draw particle===================================================================================================================================
    def draw_particle(self, position, radius, color):
        pygame.draw.circle(self.screen, color, position, radius)

    #==================Draw emitter====================================================================================================================================
    def draw_emitter(self, position, radius, color):
        pygame.draw.circle(self.screen, color, position, radius)

    #==================Draw mass====================================================================================================================================
    # Display spawn particle mass
    def display_spawn_mass(self, mass):
        font = pygame.font.SysFont('arial', 36)
        text = font.render(f"Spawn Mass: {mass}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

    #==================Draw wall====================================================================================================================================
    def draw_wall(self, color, start_pos, end_pos, width):
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)
    
    #==================Update=========================================================================================================================================
    def update(self):
        pygame.display.flip()
        self.clock.tick(60)
        print(self.clock.get_fps())



    


