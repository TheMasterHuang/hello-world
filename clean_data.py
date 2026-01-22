import pandas as pd

def load_csv_with_fallback(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path, encoding="utf-8")
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="latin1")

def to_snake_case(name: str) -> str:
    return (
        name.strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
    )

def main():
    # 1. Load data
    df = load_csv_with_fallback("raw_data.csv")

    # 2. Inspect
    print("=== INFO (before) ===")
    print(df.info())
    print("\n=== HEAD (before) ===")
    print(df.head())

    # 3. Clean column names
    df.columns = [to_snake_case(col) for col in df.columns]

    # 4. Handle missing values
    numeric_cols = df.select_dtypes(include=["number"]).columns
    categorical_cols = df.select_dtypes(exclude=["number"]).columns

    for col in numeric_cols:
        # Use median to reduce the impact of outliers
        df[col] = df[col].fillna(df[col].median())

    for col in categorical_cols:
        df[col] = df[col].fillna("Unknown")

    # 5. Deduplicate
    df = df.drop_duplicates()

    # 6. Time handling
    for col in df.columns:
        if "date" in col or "time" in col:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Inspect after cleaning
    print("\n=== INFO (after) ===")
    print(df.info())
    print("\n=== HEAD (after) ===")
    print(df.head())

    # 7. Export
    df.to_csv("cleaned_data.csv", index=False)

if __name__ == "__main__":
    main()
