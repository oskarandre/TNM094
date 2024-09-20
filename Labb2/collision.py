
import math

def handle_collisions(particles):
#=====================Update particles and detect collisions================================================================================================================
            
    # Loop through all particles to update their positions
    # This is done before checking for collisions to prevent particles from getting stuck inside each other
    for i, particle1 in enumerate(particles):
        particle1.update()
        # Check for collision between particles
        # Loop through all particles again to compare each pair of particles
        for j, particle2 in enumerate(particles):
            # Check for collision between particles
            if i != j:
                distance = math.sqrt((particle1.position[0] - particle2.position[0]) ** 2 + (particle1.position[1] - particle2.position[1]) ** 2)
                if distance <= (particle1.radius + particle2.radius):  # Use sum of radius for collision detection
            
                    # Calculate relative velocity
                    # Relative velocity is the difference between the velocities of the two particles
                    relative_velocity = [particle2.velocity[0] - particle1.velocity[0], particle2.velocity[1] - particle1.velocity[1]]
                    
                    # Calculate direction of collision
                    # Direction is a vector pointing from particle1 to particle2
                    # It is calculated by subtracting the position of particle1 from the position of particle2
                    direction = [particle2.position[0] - particle1.position[0], particle2.position[1] - particle1.position[1]]

                    # Calculate magnitude of direction
                    # Magnitude is the length of the vector
                    # It is calculated using the Pythagorean theorem
                    magnitude = math.sqrt(direction[0] ** 2 + direction[1] ** 2)

                    # Normalize direction
                    # Normalize means to scale the vector so that its magnitude is 1
                    if magnitude != 0:
                        direction[0] /= magnitude
                        direction[1] /= magnitude

                    # Calculate dot product of relative velocity and direction
                    # Dot product is a measure of how much of one vector is pointing in the direction of another
                    dot_product = relative_velocity[0] * direction[0] + relative_velocity[1] * direction[1]

                    # Calculate impulse
                    # Impulse is the change in momentum
                    # Impulse = (2 * dot_product) / (mass1 + mass2)
                    impulse = (2 * dot_product) / (particle1.mass + particle2.mass)

                    # Apply impulse to velocities
                    # Impulse is the change in momentum
                    particle1.velocity[0] += impulse * particle2.mass * direction[0]
                    particle1.velocity[1] += impulse * particle2.mass * direction[1]
                    particle2.velocity[0] -= impulse * particle1.mass * direction[0]
                    particle2.velocity[1] -= impulse * particle1.mass * direction[1]
                    
                    # Adjust positions to prevent overlapping
                    # Overlap is the difference between the sum of the radius and the distance between the particles
                    # The overlap is divided by two and subtracted from the position of the first particle and added to the position of the second particle
                    # This way, the particles are moved away from each other by half the overlap
                    # This is done to prevent the particles from getting stuck inside each other
                    overlap = (particle1.radius + particle2.radius) - distance
                    overlap /= 2
                    particle1.position[0] -= overlap * direction[0]
                    particle1.position[1] -= overlap * direction[1]
                    particle2.position[0] += overlap * direction[0]
                    particle2.position[1] += overlap * direction[1]
     #================border collision==============================================================================================================================================
    
# Check if particle has collided with the window border
# If so, reverse the velocity and dampen it
def check_border_collision(particle, WIDTH, HEIGHT):
    if particle.position[0] <= 0 or particle.position[0] >= WIDTH:
        particle.velocity[0] *= -0.6
        if particle.position[0] <= 0:
            particle.position[0] = 0
        else:
            particle.position[0] = WIDTH
    if particle.position[1] <= 0 or particle.position[1] >= HEIGHT:
        particle.velocity[1] *= -0.6
        if particle.position[1] <= 0:
            particle.position[1] = 0
        else:
            particle.position[1] = HEIGHT

#=================Line collision==============================================================================================================================================
def check_line_collision(particle, LINEXY1, LINEXY2):

    # Line segment endpoints
    x1, y1 = LINEXY1[0], LINEXY1[1]
    x2, y2 = LINEXY2[0], LINEXY2[1]

    # Line equation coefficients
    A = y2 - y1
    B = x1 - x2
    C = A * x1 + B * y1

    # Calculate distance from particle to line
    distance = abs(A * particle.position[0] + B * particle.position[1] - C) / ((A**2 + B**2) ** 0.5)

    # Calculate collision thresholds
    collision_threshold = particle.radius

    # Check if particle has collided with the line
    if distance <= collision_threshold:

       # Check if the particle is within the line segment bounds
        if min(x1, x2) <= particle.position[0] <= max(x1, x2) and min(y1, y2) <= particle.position[1] <= max(y1, y2):
            
            # Calculate the line normal vector
            normal = [y2 - y1, x1 - x2]
            normal_magnitude = (normal[0]**2 + normal[1]**2)**0.5
            normalized_normal = [normal[0] / normal_magnitude, normal[1] / normal_magnitude]

            # Calculate the dot product of the particle velocity and the normal
            dot_product = 2 *(particle.velocity[0] * normalized_normal[0] + particle.velocity[1] * normalized_normal[1])

            # Reflect the velocity across the normal
            particle.velocity[0] -= dot_product * normalized_normal[0]
            particle.velocity[1] -= dot_product * normalized_normal[1]

        