import random
from particle import Particle


def add_emitter(self, position, mass):
        # Add emitter to list of emitters
        # Emitters are used to create particles
        # Emitters have a position, number of particles, mass and max initial velocity
        self.emitters.append({
                'position': position,
                'mass': mass,
                'framecounter': 0
        })

def remove_emitter(self, position):

        radius = 3

        for emitter in self.emitters:
                if ((emitter['position'][0] - radius <= position[0] <= emitter['position'][0] + radius) and (emitter['position'][1] - radius <= position[1] <= emitter['position'][1] + radius)):
                        self.emitters.remove(emitter)
                        break

def add_particle(self, position, mass):
        self.particles.append(Particle(position, mass, 3))


def explode(self, position, num_particles, mass):
        initialVelocity = random.uniform(5, 10)
        #self.particles.append(Particle(position, mass, initialVelocity))

        for _ in range(num_particles):
            particle = Particle(position, mass, initialVelocity)
            self.particles.append(particle)
