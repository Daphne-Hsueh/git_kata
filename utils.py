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

