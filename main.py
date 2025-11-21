"""Game Insights Analyzer
Created by: Fazin Firoz
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("gameplay_sessions.csv")

    # Average session length per player
    avg_session = df.groupby("player_id")["session_length_min"].mean()
    print("Average Session Length (min) per Player:")
    print(avg_session)

    avg_session.plot(kind="bar")
    plt.xlabel("Player ID")
    plt.ylabel("Avg Session Length (min)")
    plt.title("Average Session Length per Player")
    plt.tight_layout()
    plt.savefig("avg_session_length.png")
    plt.close()

    # Retention vs session length
    retention = df.groupby("retained_next_day")["session_length_min"].mean()
    print("\nAvg Session Length by Next-Day Retention:")
    print(retention)

if __name__ == "__main__":
    main()
