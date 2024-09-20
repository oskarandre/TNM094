import pytest

class Particle:
    def __init__(self, radius=0, lifetime=0):
        self.radius = radius
        self.lifetime = lifetime

#SCENARIO("Explosion emitter")
class Explosion:
    def __init__(self, radius=0):
        self.radius = radius

    def addParticle(self, particles, lifetime):
        particles.append(Particle(radius=4, lifetime=lifetime))

@pytest.fixture
def emitter():
    return Explosion(radius=1)

#GIVEN("test_explosion_emitter") 
def test_explosion_emitter(emitter):
    #WHEN("add 5 particles to the emitter")
    particles = []
    for _ in range(5):
        emitter.addParticle(particles, lifetime=5)

    #REQUIRED("particles should have length 5")
    assert len(particles) == 5

    #REQUIRED("particles should have radius 4 and lifetime 5")
    for particle in particles:
        assert particle.radius == pytest.approx(4)
        assert particle.lifetime == pytest.approx(5)
