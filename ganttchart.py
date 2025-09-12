import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Updated tasks and timelines
data = {
    'Task': [
        'Planning',
        'Team Formation',
        'Sponsorship Outreach',
        'Marketing & Registration',
        'Tournament Execution',
        'Wrap-up & Closing'
    ],
    'Start': [
        '2025-05-18',  # Jestha 2
        '2025-05-26',  # Jestha 10
        '2025-06-04',  # Jestha 21
        '2025-06-16',  # Asadh 2
        '2025-07-19',  # Shrawan 3
        '2025-07-22'   # Shrawan 6
    ],
    'End': [
        '2025-05-26',  # Jestha 10
        '2025-06-03',  # Jestha 20
        '2025-06-15',  # Asadh 1
        '2025-07-17',  # Shrawan 1
        '2025-07-21',  # Shrawan 5
        '2025-07-22'   # Shrawan 6
    ]
}

# DataFrame setup
df = pd.DataFrame(data)
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])
df['Duration'] = (df['End'] - df['Start']).dt.days + 1

# Gantt chart
fig, ax = plt.subplots(figsize=(10, 5))
for idx, row in df.iterrows():
    ax.barh(row['Task'], row['Duration'], left=row['Start'], color='mediumseagreen')
    ax.text(row['Start'], idx, row['Start'].strftime('%b %d'), va='center', ha='right', fontsize=8)
    ax.text(row['End'], idx, row['End'].strftime('%b %d'), va='center', ha='left', fontsize=8)

# Format
ax.set_title("Interschool Cup – Gantt Chart", fontsize=14, weight='bold')
ax.set_xlabel("Date")
ax.set_ylabel("Phases")
plt.tight_layout()
plt.grid(True, axis='x', linestyle='--', alpha=0.7)
plt.show()
