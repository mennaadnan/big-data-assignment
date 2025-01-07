import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def preprocessing(df):
    # Remove null rows
    df.dropna(inplace=True)
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # Drop columns with unique values
    df.drop(['Order ID', 'Product ID'], axis=1, inplace=True)
    
    # Drop columns with data irrelevant to K means
    df.drop(["Delivery Date", "Date Order was placed"], axis=1, inplace=True)
    
    # Transform status column to lowercase
    df['Customer Status'] = df['Customer Status'].str.lower()
    
    # Transform status column from str to int
    le = LabelEncoder()
    df['Customer Status'] = le.fit_transform(df['Customer Status'])
    
    # Apply feature scaling on columns
    cols = df.columns
    ms = MinMaxScaler()
    df[cols] = ms.fit_transform(df[cols])

    # Save the preprocessed data to a CSV file
    df.to_csv("res_dpre.csv", index=False)
    
    return df  # Return the processed dataframe for the next script

