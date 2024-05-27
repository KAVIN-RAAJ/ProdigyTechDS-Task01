import matplotlib.pyplot as plt
import numpy as np

# Sample data for categorical variable (e.g., gender distribution)
categories = ['Male', 'Female', 'Other']
counts = [350, 400, 50]  # Example counts for each category

# Plotting the bar chart for gender distribution
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)  # Subplot 1
plt.bar(categories, counts, color=['blue', 'pink', 'green'])
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Gender Distribution')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Sample data for continuous variable (e.g., age distribution)
ages = np.random.randint(18, 80, size=1000)  # Example ages of 1000 individuals

# Plotting the histogram for age distribution
plt.subplot(1, 2, 2)  # Subplot 2
plt.hist(ages, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()
