# %%
from pathlib import Path

from pandas import DataFrame, read_csv

path = Path("cases/Statistics/data")


def strip_data(path: Path, float_format: int) -> DataFrame:
    """Read and write a CSV file with a specific float format."""

    df = read_csv(path, index_col=0)

    df.to_csv(path, float_format=f"%.{float_format}f")
    return df


for csv_file in path.glob("*.csv"):
    print(csv_file)
    if csv_file.stem == "verdamping":
        float_format = 4
        strip_data(csv_file, float_format=float_format)
