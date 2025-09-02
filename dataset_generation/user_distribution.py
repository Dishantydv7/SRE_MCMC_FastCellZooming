import numpy as np
import pandas as pd

# Parameters for user distribution
num_distributions = 800
rows = 200
cols = 200
min_users = 2000
max_users = 6000

# Initialize an empty list to store flattened grids
all_distributions = []

for i in range(num_distributions):
    # Initialize an empty grid for the current distribution
    grid = np.zeros((rows, cols), dtype=int)
    
    # Random total number of users for this distribution
    total_users = np.random.randint(min_users, max_users + 1)
    
    # Randomly assign users to cells in the grid (with replacement)
    # The 'replace=True' allows for multiple users in a single cell
    user_indices = np.random.choice(rows * cols, size=total_users, replace=True)
    
    # Populate the grid
    for idx in user_indices:
        row_idx = idx // cols
        col_idx = idx % cols
        grid[row_idx, col_idx] += 1
    
    # Flatten the grid into a 1D array and store it
    all_distributions.append(grid.flatten())

# Convert the list of arrays to a DataFrame and save to CSV
df = pd.DataFrame(all_distributions)
df.to_csv("user_distributions.csv", index=False)

print("User distributions generated and saved to user_distributions.csv")
print("CSV shape:", df.shape)