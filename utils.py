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
		  - Dropping rows with missing values
		  - Converting all categorical (object or category dtype) columns to lowercase
		Args:
			df: Input pandas DataFrame
		Returns:
			Cleaned pandas DataFrame
		"""
		# Drop rows with missing values
		df_clean = df.dropna().copy()

		# Convert categorical columns to lowercase
		for col in df_clean.select_dtypes(include=["object", "category"]).columns:
			df_clean[col] = df_clean[col].str.lower()

		return df_clean


