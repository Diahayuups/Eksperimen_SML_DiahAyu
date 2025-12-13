import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocessing_pipeline(input_path, output_path):
    df = pd.read_csv(input_path)

    X = df.drop(columns=["target"])
    y = df["target"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
    df_clean = X_scaled.copy()
    df_clean["target"] = y.values

    df_clean.to_csv(output_path, index=False)
    return df_clean


if __name__ == "__main__":
    preprocessing_pipeline(
        input_path="breast_cancer_raw.csv",
        output_path="preprocessing/breast_cancer_clean.csv"
    )
