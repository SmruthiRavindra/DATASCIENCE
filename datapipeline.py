import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder

def extract_data(file_path):
    
    return pd.read_csv(file_path)

def preprocess_data(df):
    
    imputer = SimpleImputer(strategy='mean')
    df[df.select_dtypes(include=['number']).columns] = imputer.fit_transform(df.select_dtypes(include=['number']))
    
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = LabelEncoder().fit_transform(df[col])
    
    return df

def transform_data(df):
    
    scaler = StandardScaler()
    df[df.columns] = scaler.fit_transform(df)
    return df

def load_data(df, output_path):
    
    df.to_csv(output_path, index=False)

def main():
    input_file = "C:\\Users\\srush\\Desktop\\Data Science\\customers-100.csv"
    output_file = "C:\\Users\\srush\\Desktop\\Data Science\\empty_data.csv"

    
    df = extract_data(input_file)
    df = preprocess_data(df)
    df = transform_data(df)
    load_data(df, output_file)
    
    print("ETL process completed successfully! Data saved to:", output_file)

if __name__ == "__main__":
    main()
