import random
import math

#===========================Particle class============================================================================================================================


# Represents a particle with mass, position, velocity and acceleration
class Particle:

    # Initialize particle with position and mass
    # Random initial velocity and angle
    # Radius is calculated from mass
    def __init__(self, position, mass, initialVelocity = random.uniform(0.05, 0.4)):
        self.position = list(position)
        self.acceleration = [0, 0]
        self.lifespan = random.randint(200, 400)

        initialAngle = random.uniform(0, 2 * math.pi)
        #initialVelocity = random.uniform(0.05, 0.4)
        self.velocity = [initialVelocity * math.cos(initialAngle), initialVelocity * math.sin(initialAngle)]
        
        self.mass = mass
        self.radius = ((3*mass)/(4*math.pi)) ** (1/3)         #Sphere density : volume = (4/3) × π × r3, mass = volume × density. 1000 kg/m³
    
    #=================Apply force=======================================================================================================================================
    # Apply force to particle
    # F = ma -> a = F/m
    def apply_force(self, force):
        if force == [0,0]:
            self.acceleration[0] = 0
            self.acceleration[1] = 0  

        else:
            self.acceleration[0] += force[0] / self.mass
            self.acceleration[1] += force[1] / self.mass
    #======================Update====================================================================================================================================
    
    # Update particle position and velocity
    def update(self):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    
   