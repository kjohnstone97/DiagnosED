from pathlib import Path

import pandas as pd

app_dir = Path(__file__).parent
ecds_df = pd.read_csv(app_dir / "ecds_df.csv")