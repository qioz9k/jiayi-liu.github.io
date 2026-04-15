# Import numpy and matplotlib
# Set total population N = 10000
# Set infection rate beta = 0.3
# Set recovery rate gamma = 0.05
# Set simulation time steps = 1000
# Initialize S=9999, I=1, R=0
# Create empty lists to store S, I, R over time
# Append initial values to lists
# Repeat for 1000 time steps:
#     Calculate new infected using binomial trial
#     Calculate new recovered using binomial trial
#     Update S, I, R values
#     Append new values to lists
# Plot S, I, R against time
# Add labels, title, legend
# Show and save the plot



import numpy as np
import matplotlib.pyplot as plt

N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

S = 9999
I = 1
R = 0

S_list = [S]
I_list = [I]
R_list = [R]

for _ in range(time_steps):
    new_infected = np.random.binomial(S, beta * I / N)
    new_recovered = np.random.binomial(I, gamma)
    
    S -= new_infected
    I = I + new_infected - new_recovered
    R += new_recovered
    
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('Stochastic SIR Model')
plt.legend()
plt.savefig('SIR.png')
plt.show()