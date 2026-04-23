# Define population data
a = 5.08  # Population in 2004
b = 5.33  # Population in 2014
c = 5.55  # Population in 2024

# Calculate population growth for two decades
d = b - a  # Growth 2004-2014: 0.25 (million)
e = c - b  # Growth 2014-2024: 0.22 (million)

# Print calculation results
print("=== Scotland Population Growth Calculation ===")
print(f"Growth 2004-2014: {d} million")
print(f"Growth 2014-2024: {e} million")

# Determine growth trend
is_decelerating = d > e  # 0.25 > 0.22 → True (decelerating)
print(f"Is population growth decelerating: {is_decelerating}")
print(f"Conclusion: Scotland population growth: {'decelerating' if is_decelerating else 'accelerating'}")

# Boolean operation section
X = True
Y = False

# Operation result
M = X or Y

# Print boolean operation result
print("=== Boolean [X or Y] Operation ===")
print(f"X = {X}, Y = {Y}, M = X or Y = {M}")