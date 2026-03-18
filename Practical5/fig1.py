# Import necessary libraries
import matplotlib.pyplot as plt

# Set plot font (avoid garbled text)
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['axes.unicode_minus'] = False

# ==============================================================================
# Task 1: Gene Expression Analysis (Core Code)
# ==============================================================================
print("===== Task 1: Gene Expression Analysis =====")

# Step 1: Create initial gene expression dictionary (5 genes)
gene_expression = {
    'TP53': 12.4,
    'EGFR': 15.1,
    'BRCA1': 8.2,
    'PTEN': 5.3,
    'ESR1': 10.7
}
print("\n1. Initial gene expression dictionary:")
print(gene_expression)

# Step 2: Add new gene MYC (expression value = 11.6)
gene_expression['MYC'] = 11.6
print("\n2. Dictionary after adding MYC:")
print(gene_expression)

# Step 3: Plot bar chart for gene expression
# PSEUDOCODE: Extract gene names (x-axis) and expression values (y-axis)
genes = list(gene_expression.keys())
expressions = list(gene_expression.values())

plt.figure(figsize=(8, 5))
plt.bar(genes, expressions, color='lightblue')
plt.title('Gene Expression Levels', fontsize=14)
plt.xlabel('Gene Name', fontsize=12)
plt.ylabel('Expression Level', fontsize=12)
plt.tight_layout()
plt.show()

# Step 4: Query gene expression value (with error handling)
# PSEUDOCODE: Modify 'gene_of_interest' to query different genes
gene_of_interest = 'EGFR'

if gene_of_interest in gene_expression:
    print(f"\n3. Expression of {gene_of_interest}: {gene_expression[gene_of_interest]}")
else:
    print(f"\n3. Error: {gene_of_interest} not found in dataset")

# Step 5: Calculate average expression value
# PSEUDOCODE: Average = total expression / number of genes
total = sum(gene_expression.values())
count = len(gene_expression)
average = total / count

print(f"\n4. Average expression: {average:.2f}")


