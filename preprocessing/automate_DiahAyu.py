import pandas as pd
from sklearn.preprocessing import StandardScaler
import os


def preprocessing_pipeline(input_path, output_path):
    # Load dataset
    df = pd.read_csv(input_path)

    # Pisahkan fitur dan target
    X = df.drop(columns=['target'])
    y = df['target']

    # Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

    # Gabungkan kembali
    df_clean = X_scaled.copy()
    df_clean['target'] = y.values

    # Pastikan folder output ada
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Simpan hasil preprocessing
    df_clean.to_csv(output_path, index=False)

    return df_clean


if __name__ == "__main__":
    preprocessing_pipeline(
        input_path="../namadataset_raw/breast_cancer_raw.csv",
        output_path="namadataset_preprocessing/breast_cancer_clean.csv"
    )
