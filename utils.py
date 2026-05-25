from pathlib import Path
from typing import Optional

import pandas as pd


def load_data(path: Optional[str] = None) -> pd.DataFrame:
	"""Load the Titanic CSV into a pandas DataFrame.

	If `path` is not provided, this function will look for `data/titanic.csv`
	located next to the repository root by resolving the current file's
	parent directory.

	Args:
		path: Optional path to the CSV file. If not given, defaults to
			`data/titanic.csv` relative to this repository.

	Returns:
		A pandas DataFrame with the Titanic data.
	"""
	if path is None:
		base = Path(__file__).resolve().parent
		csv_path = base / "data" / "titanic.csv"
	else:
		csv_path = Path(path)

	return pd.read_csv(csv_path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
	"""
	Clean a pandas DataFrame by:
	  - Dropping rows where the passenger class column is missing (auto-detects column name)
	  - Converting all categorical (object or category dtype) columns to lowercase
	Args:
	    df: Input pandas DataFrame
	Returns:
	    Cleaned pandas DataFrame
	"""

	# Try to find the passenger class column (case-insensitive, strip spaces)
	possible_names = ["pclass", "class", "passenger class"]
	col_map = {col.strip().lower(): col for col in df.columns}
	class_col = None
	for name in possible_names:
		if name in col_map:
			class_col = col_map[name]
			break

	if class_col is None:
		raise ValueError("Could not find a passenger class column (e.g., 'pclass', 'class') in DataFrame.")

	# Drop rows only where the class column is missing
	df_clean = df.dropna(subset=[class_col]).copy()

	# Convert categorical columns to lowercase
	for col in df_clean.select_dtypes(include=["object", "category"]).columns:
		df_clean[col] = df_clean[col].str.lower()

	return df_clean


