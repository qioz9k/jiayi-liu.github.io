 #Import required library (mandatory for plotting)
import matplotlib.pyplot as plt
print("\n===== Task 3: Population Growth Rate Calculation =====")

# Step 1: Define population dataset (2020 & 2024, unit: million)
population_data = {
    'UK': [66.7, 69.2],
    'China': [1426, 1410],
    'Italy': [59.4, 58.9],
    'Brazil': [208.6, 212.0],
    'USA': [331.6, 340.1]
}
print(f"\nStep 1: Population dataset (2020, 2024):")
for country, pop in population_data.items():
    print(f"   {country}: {pop[0]} (2020), {pop[1]} (2024) million")

# Step 2: Calculate percentage change for each country
# PSEUDOCODE: percent_change = (2024_pop - 2020_pop) / 2020_pop * 100
pop_change = {}
for country, (pop2020, pop2024) in population_data.items():
    change = (pop2024 - pop2020) / pop2020 * 100
    pop_change[country] = round(change, 2)

# Step 3: Print percentage change results
print(f"\nStep 3: Population percentage change (2020-2024):")
for country, pct in pop_change.items():
    print(f"   {country}: {pct:.2f}%")

# Step 4: Sort countries by percentage change (descending)
sorted_countries = sorted(pop_change.items(), key=lambda x: x[1], reverse=True)
print(f"\nStep 4: Sorted by change rate (descending):")
for country, pct in sorted_countries:
    print(f"   {country}: {pct:.2f}%")

# Step 5: Find country with largest increase/decrease
largest_increase = sorted_countries[0]
largest_decrease = sorted_countries[-1]
print(f"Step 5: Largest increase: {largest_increase[0]} ({largest_increase[1]:.2f}%)")
print(f"        Largest decrease: {largest_decrease[0]} ({largest_decrease[1]:.2f}%)")

# Step 6: Plot well-labelled bar chart (save to 'Practical 5' folder)
# PSEUDOCODE: Plot bar chart for population change, save to experiment folder
countries = [x[0] for x in sorted_countries]
changes = [x[1] for x in sorted_countries]
colors = ['green' if c > 0 else 'red' for c in changes]

plt.figure(figsize=(9, 6))
bars = plt.bar(countries, changes, color=colors)
plt.title('2020-2024 Population Percentage Change by Country', fontsize=14)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Percentage Change (%)', fontsize=12)
plt.axhline(y=0, color='black', linestyle='-')  # Add zero line for reference

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + (0.1 if height>0 else -0.5),
             f'{height:.2f}%', ha='center')

# Save chart to 'Practical 5' folder (uncomment if folder exists)
# plt.savefig('Practical 5/population_change.png')
plt.tight_layout()
plt.show()