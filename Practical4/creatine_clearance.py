"""
Pseudocode (Lab Document Requirement):
1. Define input variables: age, weight, gender, Creatinine (Cr)
2. Validate input legitimacy (by priority):
   - Age validation: age < 100
   - Weight validation: 20 < weight < 80
   - Creatinine validation: 0 < Cr < 100
   - Gender validation: gender is male/female (case insensitive)
3. If validation fails: print specific error message (clearly indicate which variable is wrong)
4. If validation passes: calculate CrCl:
   - Basic formula: CrCl = [(140 - age) × weight] / (72 × Cr)
   - Female adjustment: CrCl × 0.85
5. Print calculation result (2 decimal places for clarity)
"""

age = 45               # Age (years)
weight = 65            # Weight (kg)
gender = "female"      # Gender (male/female, case-insensitive e.g. Female)
cr = 80                # Creatinine concentration (μmol/l)

# age = 101
# weight = 18  # Weight < 20kg
# cr = 105     # Creatinine > 100μmol/l
# gender = "man" # Invalid gender

error_msg = ""  # Initialize error message string

# 1. Validate age (Priority 1)
if age >= 100:
    error_msg = f"Age error: {age} years ≥ 100, must be less than 100"
# 2. Validate weight (Priority 2)
elif not (20 < weight < 80):
    error_msg = f"Weight error: {weight}kg, must be between 20-80kg (exclusive)"
# 3. Validate creatinine concentration (Priority 3)
elif not (0 < cr < 100):
    error_msg = f"Cr error: {cr}μmol/l, must be between 0-100μmol/l (exclusive)"
# 4. Validate gender (Priority 4, case-insensitive)
elif gender.lower() not in ["male", "female"]:
    error_msg = f"Gender error: {gender}, must be male or female (case insensitive)"

if error_msg == "":
    # Calculate CrCl using the basic formula
    crcl = (140 - age) * weight / (72 * cr)
    # Female adjustment: multiply by 0.85 (convert to lowercase to avoid case issues)
    if gender.lower() == "female":
        crcl = crcl * 0.85
    # Print result (2 decimal places, meets lab output requirements)
    print("=== Creatinine Clearance (CrCl) Calculation Result ===")
    print(f"Input parameters: age={age}y, weight={weight}kg, gender={gender}, Cr={cr}μmol/l")
    print(f"CrCl = {crcl:.2f} ml/min")
else:
    # Validation failed, print specific error
    print("❌ INVALID INPUT:", error_msg)