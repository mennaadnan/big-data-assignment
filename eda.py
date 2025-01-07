def eda(df):
    print(df.info())
    print(df.describe().T)

    # Insight 1: Null values
    null_count = 0
    for count in df.isnull().sum():
        null_count += count  # Summing the null values
    with open("eda-in-1.txt", "a") as eda1:
        eda1.write(f"There are {null_count} rows with null content.\n")


    # Insight 2: Duplicates
    duplicated_count = df.duplicated().sum()
    with open("eda-in-2.txt", "a") as eda2:
        eda2.write(f"There are {duplicated_count} duplicated row(s) in the data.\n")

    # Insight 3: Unique values in 'Customer Status'
    unique_status = df['Customer Status'].unique()
    uniq_values = ', '.join(map(str, unique_status))  # Show before encoding
    with open("eda-in-3.txt", "a") as eda3:
        eda3.write(f"The column Customer Status has {len(df['Customer Status'].unique())} unique values: {uniq_values}\n")
    
    # Proceed to next stage (visualization)
    from vis import visualization
    visualization(df)
