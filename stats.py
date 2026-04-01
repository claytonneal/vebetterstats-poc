from dataclasses import dataclass
from decimal import Decimal
from typing import cast

import pandas as pd


@dataclass
class RoundSummary:
    total_actions: int
    total_unique_users: int
    total_b3tr: Decimal


class RoundStats:
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data

    def get_round_summary(self) -> RoundSummary:
        """
        Gets the overall round summary
        - total actions
        - total unique users (wallets)
        - total b3tr rewarded
        """
        self.total_actions = len(self.data)
        self.total_unique_wallets = cast(int, self.data["receiver_address"].nunique())
        self.total_b3tr = cast(Decimal, self.data["amount"].sum())
        return RoundSummary(
            self.total_actions, self.total_unique_wallets, self.total_b3tr
        )

    def get_apps_summary(self) -> pd.DataFrame:
        """
        Computes per app summary, data frame has columns:
        - app_name
        - total_actions
        - unique_users
        - total_b3tr
        - avg_b3tr_per_action
        - avg_actions_per_user
        - percent_unique_users
        - percent_actions
        """
        # aggregate stats
        df_stats = (
            self.data.groupby("app_name")
            .agg(
                total_actions=("app_name", "size"),
                unique_users=("receiver_address", "nunique"),
                total_b3tr=("amount", "sum"),
                avg_b3tr_per_action=("amount", "mean"),
            )
            .reset_index()
            .sort_values("total_actions", ascending=False)
        )
        # avg actions per user
        df_stats["avg_actions_per_user"] = (
            df_stats["total_actions"] / df_stats["unique_users"]
        ).round(2)
        # percent unique users
        df_stats["percent_unique_users"] = (
            df_stats["unique_users"] / self.total_unique_wallets
        ).round(3)
        # percent actions
        df_stats["percent_actions"] = (
            df_stats["total_actions"] / self.total_actions
        ).round(3)
        return df_stats
