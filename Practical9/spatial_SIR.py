# Import numpy and matplotlib.pyplot
# Create 100x100 population grid with all 0 (susceptible)
# Randomly choose one position and set it to 1 (infected)
# Set beta = 0.3, gamma = 0.05
# Set time steps = 100
# For each time step:
#     Make a copy of the population grid
#     Find all infected points (value = 1)
#     For each infected point, check all 8 neighbours
#     If neighbour is valid and susceptible, infect with probability beta
#     For infected points, recover with probability gamma (set to 2)
#     Update population
# Plot grid at steps 0,10,30,50,80,100
# Use viridis colormap:
#     0 (susceptible) = dark purple
#     1 (infected) = blue-green
#     2 (recovered) = yellow
# Turn off axes
# Show and save the figure



import numpy as np
import matplotlib.pyplot as plt

# Create 100x100 susceptible population
population = np.zeros((100, 100))

# Random initial infected point
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

beta = 0.3
gamma = 0.05
time_steps = 100

plt.figure(figsize=(10, 10), dpi=150)
plot_steps = [0, 10, 30, 50, 80, 100]

for step in range(time_steps + 1):
    new_pop = population.copy()

  
    infectedIndex = np.where(population == 1)
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]

        for xNeighbour in range(x-1, x+2):
            for yNeighbour in range(y-1, y+2):
                if (xNeighbour, yNeighbour) != (x, y):
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour != 100 and yNeighbour != 100:
                        if new_pop[xNeighbour, yNeighbour] == 0:
                            new_pop[xNeighbour, yNeighbour] = np.random.choice(range(2), 1, p=[1-beta, beta])[0]

    # Recovery process
    infected_rec = np.where(new_pop == 1)
    for i in range(len(infected_rec[0])):
        x_r = infected_rec[0][i]
        y_r = infected_rec[1][i]
        if np.random.random() < gamma:
            new_pop[x_r, y_r] = 2

    population = new_pop

    if step in plot_steps:
        plt.subplot(3, 2, plot_steps.index(step)+1)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time = {step}')
        plt.axis('off')

plt.tight_layout()
plt.savefig('spatial_SIR.png')
plt.show()