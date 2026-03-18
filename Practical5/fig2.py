# Import required library (mandatory for plotting)
import matplotlib.pyplot as plt

# Set plot font to avoid garbled text (optimization only)
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['axes.unicode_minus'] = False

# ==============================================================================
# Task 2: Heart Rate Analysis (Fixed Version with English Pseudocode)
# ==============================================================================
print("\n===== Task 2: Heart Rate Analysis =====")

# Step 1: Define the heart rate dataset (given in experiment)
# PSEUDOCODE: Use a list to store resting heart rate data of 11 patients (unit: bpm)
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
print(f"Step 1: Heart rate dataset: {heart_rates}")

# Step 2: Count total number of patients
# PSEUDOCODE: Calculate patient count by getting the length of the heart rate list
patient_count = len(heart_rates)
print(f"Step 2: Total patients: {patient_count}")

# Step 3: Calculate average resting heart rate
# PSEUDOCODE: Average = sum of all heart rates / total number of patients
total_hr = sum(heart_rates)
avg_hr = total_hr / patient_count
print(f"Step 3: Average heart rate: {avg_hr:.1f} bpm")

# Step 4: Categorize heart rates into 3 groups
# PSEUDOCODE: Classify each heart rate → Low(<60), Normal(60-120), High(>120)
low_hr = 0    # Counter for low heart rate (<60 bpm)
normal_hr = 0 # Counter for normal heart rate (60-120 bpm)
high_hr = 0   # Counter for high heart rate (>120 bpm)

# Loop through each heart rate to count categories (indentation: 4 spaces)
for hr in heart_rates:
    if hr < 60:
        low_hr += 1
    elif 60 <= hr <= 120:
        normal_hr += 1
    else:
        high_hr += 1

# Step 5: Print category statistics
print(f"\nStep 4: Heart rate categories:")
print(f"   Low (<60 bpm): {low_hr} patients")
print(f"   Normal (60-120 bpm): {normal_hr} patients")
print(f"   High (>120 bpm): {high_hr} patients")

# Step 6: Find the category with the most patients
# PSEUDOCODE: Get the category name with the maximum patient count
hr_stats = {'Low': low_hr, 'Normal': normal_hr, 'High': high_hr}
largest_cat = max(hr_stats, key=hr_stats.get)
print(f"Step 5: Largest category: {largest_cat}")

# Step 7: Plot a well-labelled pie chart
# PSEUDOCODE: Create a pie chart to show heart rate distribution with percentage labels
labels = ['Low', 'Normal', 'High']
sizes = [low_hr, normal_hr, high_hr]
colors = ['lightcoral', 'lightgreen', 'lightskyblue']

# Create pie chart (simplified parameters for compatibility)
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Heart Rate Distribution')
plt.axis('equal')  # Ensure the pie chart is circular

# Mandatory: Show the plot (no plot will pop up without this line)
plt.show()

# Confirmation message
print("\nTask 2 completed successfully! Pie chart displayed.")

