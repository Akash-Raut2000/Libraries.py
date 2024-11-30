import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create sample data
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Score': [85, 90, 88]}
df = pd.DataFrame(data)

# Calculate average age and score
average_age = np.mean(df['Age'])
average_score = np.mean(df['Score'])

# Display results
print(f"Average Age: {average_age}, Average Score: {average_score}")

# Plot data
plt.bar(df['Name'], df['Score'], color='skyblue')
plt.title("Scores by Name")
plt.xlabel("Name")
plt.ylabel("Score")
plt.show()
