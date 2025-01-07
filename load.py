import sys
import pandas as pd
from dpre import preprocessing  # Import data preprocessing function

def load_data(file_path):
    """Load the dataset from the provided file path."""
    try:
        print(f"Reading file from path: {file_path}")
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please provide a valid path.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Ensure a file path is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python3 load.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Load the data
    df = load_data(file_path)

    # Save the DataFrame globally for the next stage
    globals()["df"] = df

    print("Pipeline Starting...")

    # Call data preprocessing function from dpre.py and pass the data frame
    df = preprocessing(df)

    # Call the next stage (EDA)
    from eda import eda
    eda(df)

