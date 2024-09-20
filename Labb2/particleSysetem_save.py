import pygame
import sys
import random
import math
from renderer import Renderer
from particle import Particle
from collision import handle_collisions, check_border_collision
from gravity import apply_gravity_to_particles, gravity_to_center
from emitter import add_particle, explode, add_emitter, remove_emitter
from GUI import ParticleMassController

#=========================Particle System===========================================================================================================================
class ParticleSystem:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.renderer = Renderer(width, height)
        self.particles = []
        self.emitters = []
        self.gravity_active_up = False
        self.gravity_active_right = False
        self.gravity_active_down = False
        self.gravity_active_left = False
        self.gravity_active_center = False
        self.gravity = 9.82 * (1 / 50)
        self.controller = ParticleMassController(width, height)


    def is_alive(self):
            return self.lifespan > 0

    def update(self):
        self.renderer.screen.fill((0, 0, 0))
        
        #==========================================Mouse and Keyboard===============================================================================================================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse input
            # Add small particles on left click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    add_emitter(self, pygame.mouse.get_pos(), 1000)
                    #add_particle(self, pygame.mouse.get_pos(), 10000)

            # Add large particles on right click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    remove_emitter(self, pygame.mouse.get_pos())
                    #add_emitter(self, pygame.mouse.get_pos(), 100000)
                    #add_particle(self, pygame.mouse.get_pos(), 100000)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    explode(self, pygame.mouse.get_pos(), 30, 1000)

            # Keyboard input
            # Set gravity direction based on key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.gravity_active_up = True        
                if event.key == pygame.K_d:
                    self.gravity_active_right = True
                if event.key == pygame.K_s:
                    self.gravity_active_down = True 
                if event.key == pygame.K_a:
                    self.gravity_active_left = True
                if event.key == pygame.K_SPACE:
                    self.gravity_active_center = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.gravity_active_up = False
                if event.key == pygame.K_d:
                    self.gravity_active_right = False        
                if event.key == pygame.K_s:
                    self.gravity_active_down = False
                if event.key == pygame.K_a:
                    self.gravity_active_left = False
                if event.key == pygame.K_SPACE:
                    self.gravity_active_center = False      
            
                self.controller.process_events([event])

            self.controller.update(pygame.time.Clock().tick(60) / 1000.0)
        #===========================Apply forces to particles========================================================================================================
        
        # Apply gravity to particles
        # Gravity is applied as a force proportional to the mass of the particle
                    # F = mg -> g = 9.82 m/s² 
                    # g is scaled down by a factor of 1/500 to make the particles fall slower
        # The force is applied in the direction of the gravity vector

        
            # if self.gravity_active_up:
            #      apply_gravity_to_particles(self.particles, 0, -self.gravity)

            # if self.gravity_active_right:
            #     apply_gravity_to_particles(self.particles, self.gravity, 0)

            # if self.gravity_active_down:
            #     apply_gravity_to_particles(self.particles, 0, self.gravity)

            # if self.gravity_active_left:
            #     apply_gravity_to_particles(self.particles, -self.gravity, 0)
           
            # if self.gravity_active_center:
            #     gravity_to_center(self.particles, self.gravity, self.width, self.height)

            # if not (self.gravity_active_up or self.gravity_active_right or self.gravity_active_down or self.gravity_active_left or self.gravity_active_center):
            #     apply_gravity_to_particles(self.particles, 0, 0)

            # Apply gravity to particles
            apply_gravity_to_particles(self.particles,
                                   int(self.gravity_active_right)*self.gravity - int(self.gravity_active_left)*self.gravity,
                                   int(self.gravity_active_down)*self.gravity - int(self.gravity_active_up)*self.gravity)

                # Apply gravity to center if active
            if self.gravity_active_center:
                gravity_to_center(self.particles, self.gravity, self.width, self.height)
        

        #=========================Update particles===========================================================================================================================    

        # Handle collisions between particles
        handle_collisions(self.particles)
                
        # Handle emitter particles
        for emitter in self.emitters:
            emitter['framecounter'] += 1

            if emitter['framecounter'] % 30 == 0:
                add_particle(self, emitter['position'], emitter['mass'])
            
            self.renderer.draw_emitter(emitter['position'], 5, (255, 0, 0))

        # Check for border collisions
        for particle in self.particles:
            check_border_collision(particle, self.width, self.height)

            #remove paricles if lifespan is less then 0
            particle.lifespan -= 1
            if particle.lifespan <= 0:
                self.particles.remove(particle)
            
            #=======================Draw particles================================================================================================================================
            self.renderer.draw_particle((int(particle.position[0]), int(particle.position[1])), particle.radius, (255, 255, 255))

        # Update the display
        self.renderer.update()
        self.controller.draw_ui(self.renderer.screen)

        



if __name__ == "__main__":
    WIDTH, HEIGHT = 1200, 700
    #GRAVITY = 9.82 * (1 / 500)
    PARTICLE_RADIUS = 10

    ps = ParticleSystem(WIDTH, HEIGHT)
    clock = pygame.time.Clock()
    
    while True:
        ps.update()
        pygame.display.flip()
        clock.tick(60)