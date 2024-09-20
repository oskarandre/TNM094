import math

def apply_gravity_to_particles(particles, x_gravity, y_gravity):
    #print(x_gravity, y_gravity)
    # Apply gravity to particles
    for particle in particles:
        particle.apply_force([x_gravity*particle.mass, y_gravity * particle.mass])


#=========================Gravity functions===========================================================================================================================
def gravity_to_center(particles, gravity, width, height):
    #print(gravity)
    center = [width / 2, height / 2]
    for particle in particles:
        # Calculate direction vector from particle to center
        direction = [center[0] - particle.position[0], center[1] - particle.position[1]]
        # Calculate the distance between the particle and the center
        distance = math.sqrt(direction[0] ** 2 + direction[1] ** 2)
        # Ensure that distance is not zero to avoid division by zero
        if distance != 0:
            # Normalize the direction vector
            direction = [component / distance for component in direction]
            # Apply force towards the center
            force = [(gravity*5) * component * particle.mass for component in direction]
            particle.apply_force(force)