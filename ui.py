import pandas as pd
import streamlit as st


def render_app_cards(df_stats: pd.DataFrame, cols_per_row: int = 2) -> None:
    st.html("""
    <style>
    .app-card {
        background: linear-gradient(180deg, #18212f 0%, #111827 100%);
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 18px;
        padding: 16px;
        box-shadow: 0 10px 24px rgba(0,0,0,0.22);
        color: #e5e7eb;
        min-height: 320px;
        margin-bottom: 12px;
    }

    .app-card-title {
        font-size: 1.2rem;
        font-weight: 800;
        color: #f8fafc;
        margin-bottom: 12px;
        padding-bottom: 8px;
        border-bottom: 1px solid rgba(148, 163, 184, 0.15);
    }

    .metric-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
    }

    .metric-box {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(148, 163, 184, 0.12);
        border-radius: 12px;
        padding: 10px 12px;
    }

    .metric-box.full {
        grid-column: span 2;
        background: linear-gradient(90deg, rgba(59,130,246,0.12), rgba(168,85,247,0.12));
        border: 1px solid rgba(96,165,250,0.25);
    }

    .metric-label {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #94a3b8;
        margin-bottom: 6px;
        font-weight: 700;
    }

    .metric-value {
        font-size: 1.25rem;
        font-weight: 800;
        color: #f8fafc;
        line-height: 1.1;
    }

    .metric-value.accent {
        color: #60a5fa;
    }
    </style>
    """)

    for i in range(0, len(df_stats), cols_per_row):
        cols = st.columns(cols_per_row)

        for j, col in enumerate(cols):
            if i + j >= len(df_stats):
                continue

            row = df_stats.iloc[i + j]

            with col:
                st.html(f"""
                <div class="app-card">
                    <div class="app-card-title">{row["app_name"]}</div>

                    <div class="metric-grid">
                        <div class="metric-box">
                            <div class="metric-label">Actions</div>
                            <div class="metric-value">{int(row["total_actions"]):,}</div>
                        </div>

                        <div class="metric-box">
                            <div class="metric-label">Unique Users</div>
                            <div class="metric-value">{int(row["unique_users"]):,}</div>
                        </div>

                        <div class="metric-box">
                            <div class="metric-label">Total B3TR</div>
                            <div class="metric-value">{float(row["total_b3tr"]):,.2f}</div>
                        </div>

                        <div class="metric-box">
                            <div class="metric-label">Avg B3TR / Action</div>
                            <div class="metric-value">{float(row["avg_b3tr_per_action"]):,.2f}</div>
                        </div>

                        <div class="metric-box">
                            <div class="metric-label">Avg Actions / User</div>
                            <div class="metric-value">{float(row["avg_actions_per_user"]):,.2f}</div>
                        </div>

                        <div class="metric-box">
                            <div class="metric-label">% Overall Users</div>
                            <div class="metric-value">{float(row["percent_unique_users"]):.1%}</div>
                        </div>

                        <div class="metric-box full">
                            <div class="metric-label">% Overall Actions</div>
                            <div class="metric-value accent">{float(row["percent_actions"]):.1%}</div>
                        </div>
                    </div>
                </div>
                """)
