import pandas as pd

# Load your file
df = pd.read_csv("Patients_CRG.csv", header=None, dtype=str, keep_default_na=False)

# Function to clean and deduplicate caregivers in one row
def clean_row(row):
    caregivers = row.dropna().astype(str).tolist()
    # Keep the original values (no stripping of Crg or amounts)
    cleaned = [c.strip() for c in caregivers if c.strip() != ""]
    unique = list(dict.fromkeys(cleaned))  # keep order, remove duplicates
    return ", ".join(unique)

# Apply function to each row
df["Unique_Caregivers"] = df.apply(clean_row, axis=1)

# Save to new CSV
output_path = "unique_Patients_CRG_per_row.csv"
df.to_csv(output_path, index=False)

print(df.head())

