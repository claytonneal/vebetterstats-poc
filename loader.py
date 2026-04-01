import re
from pathlib import Path
from typing import List

import pandas as pd

pattern = re.compile(r"rewards-events-round-(\d+)\.csv")


def get_round_numbers() -> List[int]:
    """
    Get all round numbers
    """
    round_numbers = sorted(
        int(match.group(1))
        for f in Path("data").iterdir()
        if f.is_file() and (match := pattern.match(f.name))
    )
    return round_numbers


def load_round_data(round_number: int) -> pd.DataFrame:
    """
    Loads the csv file for the selected round
    """
    return pd.read_csv(f"./data/rewards-events-round-{round_number}.csv")
