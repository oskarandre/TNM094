import pygame
import sys
from renderer import Renderer
from collision import handle_collisions, check_border_collision, check_line_collision
from gravity import apply_gravity_to_particles, gravity_to_center
from emitter import add_particle, explode, add_emitter, remove_emitter

#import timeit
#import time
#import objgraph
#import unittest
#import pytest
from memory_profiler import profile


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
        self.gravity = 9.82 * (1 / 500)
        self.mass = 1000

    @profile
    def update(self):
        self.renderer.screen.fill((0, 0, 0))
        
        self.renderer.display_spawn_mass(self.mass/1000)

        #==========================================Mouse and Keyboard===============
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse input
            # Add small particles on left click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    add_emitter(self, pygame.mouse.get_pos(), self.mass)
                    #add_particle(self, pygame.mouse.get_pos(), 10000)

            # Remove emitter on right click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    remove_emitter(self, pygame.mouse.get_pos())
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    explode(self, pygame.mouse.get_pos(), 20, self.mass)

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
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_UP:
                    self.mass += 1000
                if event.key == pygame.K_DOWN:
                    if self.mass > 1000:
                        self.mass -= 1000

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
            
        
        #===========================Apply forces to particles========================================================================================================
        
        # Apply gravity to particles
        # Gravity is applied as a force proportional to the mass of the particle
                    # F = mg -> g = 9.82 m/s² 
                    # g is scaled down by a factor of 1/500 to make the particles fall slower
        # The force is applied in the direction of the gravity vector
                    
        if self.particles: # If there are particles
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
            check_line_collision(particle, LinePointXY1, LinePointXY2)

            #remove paricles if lifespan is less then 0
            particle.lifespan -= 1
            if particle.lifespan <= 0:
                self.particles.remove(particle)
            
            #=======================Draw particles================================================================================================================================
            self.renderer.draw_particle((int(particle.position[0]), int(particle.position[1])), particle.radius, (255, 255, 255))

        # Draw line
        self.renderer.draw_wall((255,255,255), LinePointXY1, LinePointXY2, 4)

        # Update the display
        self.renderer.update()     


if __name__ == "__main__":
    WIDTH, HEIGHT = 1200, 700
    LinePointXY1, LinePointXY2 = [900, 350], [720, 210]

    ps = ParticleSystem(WIDTH, HEIGHT)
    pygame.init()

    while True:
        #objgraph.show_most_common_types()
        ps.update()



