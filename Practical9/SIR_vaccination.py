# Import numpy and matplotlib.pyplot
# Set N = 10000, beta = 0.3, gamma = 0.05, time_steps = 1000
# Define vaccination rates: [0,0.1,...,1.0]
# Create figure
# For each rate in vaccination rates:
#    vaccinated = int(N * rate)
#    S = N - vaccinated - 1
#    I = 1
#   R = 0
#    S_list = []
#    I_list = []
#    R_list = []
#    Append initial values
#    Loop for time_steps:
#        new_infected = binomial(S, beta * I / N)
#        new_recovered = binomial(I, gamma)
#        S -= new_infected
#       I = I + new_infected - new_recovered
#        R += new_recovered
#        I_list.append(I)
#    Plot I_list with label f'{int(rate*100)}%'
# Add labels, title, legend
# Save and show plot


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000
vacc_rates = np.arange(0, 1.1, 0.1)

plt.figure(figsize=(6,4), dpi=150)

for i, rate in enumerate(vacc_rates):
    vaccinated = int(N * rate)
    S = N - vaccinated - 1
    I = 1
    R = 0
    I_history = [I]
    
    for _ in range(time_steps):
        new_infected = np.random.binomial(S, beta * I / N)
        new_recovered = np.random.binomial(I, gamma)
        S -= new_infected
        I = I + new_infected - new_recovered
        R += new_recovered
        I_history.append(I)
    
    plt.plot(I_history, label=f'{int(rate*100)}%', color=cm.viridis(i*25))

plt.xlabel('Time')
plt.ylabel('Infected people')
plt.title('SIR with Different Vaccination Rates')
plt.legend(title='Vaccination rate')
plt.savefig('SIR_vaccination.png')
plt.show()