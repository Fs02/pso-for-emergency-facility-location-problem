import numpy as np
import math
import visual

max_iter = 1000
pop_size = 100
facility = 1
c1 = 2
c2 = 2

class Particle:
    pass

def facility_coverage(position, world):
    fitness = 0.0
    for x in xrange(world.shape[0]):
        for y in xrange(world.shape[1]):
            distance = 999999999999.0
            for f in range(position.shape[0]/2):
                distance = min(distance, np.abs(x - position[f * 2 + 0]) + np.abs(y - position[f * 2 + 1]))

            demand = world[x, y]
            fitness += distance * demand
    return 1/fitness

world = np.loadtxt(open("map.csv","rb"),delimiter=",",skiprows=0)

v = visual.Visual(world)

# Initialize the particles
particles = []
for i in range(pop_size):
    p = Particle()
    # each facility have 2 axis (x, y) coordinates
    p.position = np.random.random_integers(0, world.shape[0], 2 * facility)
    p.velocity = 0.0
    p.fitness = 0.0
    particles.append(p)

gbest = particles[0]

i = 0
while i < max_iter:
    for p in particles:
        fitness = facility_coverage(p.position, world)
        if fitness > p.fitness:
            p.fitness = fitness
            p.best = p.position

        if fitness > gbest.fitness:
            gbest = p

        velocity = p.velocity + c1 * np.random.rand() * (p.best - p.position) \
                                + c2 * np.random.rand() * (gbest.position - p.position)
        p.position = p.position + velocity

    i += 1

    stats = "Iterations : " + str(i) + "\nFitness    : " + str(gbest.fitness)
    v.update(particles, stats)
    if i % (max_iter/10) == 0:
        print str(gbest.position) + " => " + str(gbest.fitness)

print '\nParticle Swarm Optimisation\n'
print 'Population size : ', pop_size
print 'c1              : ', c1
print 'c2              : ', c2
print 'facility        : ', facility

print 'RESULTS\n', '-'*7
print 'gbest fitness   : ', gbest.fitness
print 'gbest params    : ', gbest.position
print 'iterations      : ', i

raw_input("Press Enter to continue...")
