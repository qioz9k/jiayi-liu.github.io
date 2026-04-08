def calculate_protein_mass(protein_sequence):

    mass_table = {
        'G': 57.02,
        'A': 71.04,
        'S': 87.03,
        'P': 97.05,
        'V': 99.07,
        'T': 101.05,
        'C': 103.01,
        'I': 113.08,
        'L': 113.08,
        'N': 114.04,
        'D': 115.03,
        'Q': 128.06,
        'K': 128.09,
        'E': 129.04,
        'M': 131.04,
        'H': 137.06,
        'F': 147.07,
        'R': 156.10,
        'Y': 163.06,
        'W': 186.08
    }

    total_mass = 0.0

    for aa in protein_sequence:
        if aa not in mass_table:
            return f"Error: invalid amino acid '{aa}'"
        total_mass += mass_table[aa]

    return total_mass


if __name__ == "__main__":
    sequence = "GASPV"
    mass = calculate_protein_mass(sequence)
    print("Sequence:", sequence)
    print("Total mass:", mass)