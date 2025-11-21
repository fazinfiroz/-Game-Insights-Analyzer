# Game Insights Analyzer 🎮

A small analytics project built in **Python** using **Pandas** and **Matplotlib** to explore gameplay behavior,
player engagement, and retention patterns.

This project (dataset and code) was created by **Fazin Firoz** as part of my data analysis portfolio.

## 🔧 Tech Stack
- Python
- Pandas
- Matplotlib

## 📊 Dataset
File: `gameplay_sessions.csv`  
Columns include:
- `player_id`
- `session_id`
- `session_length_min`
- `levels_completed`
- `in_game_purchases`
- `retained_next_day` (0/1)

## ▶️ Example Usage
```bash
python analyze.py
```

The script loads the dataset and generates simple visualizations like:
- Average session length by player
- Retention vs. average session length
