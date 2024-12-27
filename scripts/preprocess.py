import pandas as pd

# Load the dataset
data = pd.read_csv("data/MachineLearningRating_v3.txt", sep="|")

# Example preprocessing: fill missing values with mode
for column in data.select_dtypes(include=['object']).columns:
    data[column].fillna(data[column].mode()[0], inplace=True)

# Save preprocessed data
data.to_csv("data/preprocessed_data.csv", index=False)
print("Preprocessing complete. Data saved to data/preprocessed_data.csv.")
