import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.table as tbl

# Data for the table
data = {
    "Sponsorship Tier": ["Title Sponsor", "Co-Sponsor", "Category Sponsor", "In-Kind Partner"],
    "Booth Stall at Venue": ["✅ Yes (Premium)", "✅ Yes", "⚠️ Negotiable", "⚠️ Negotiable"],
    "Booth Availability Notes": [
        "Guaranteed premium booth space",
        "Guaranteed booth space",
        "Possible with added discussion",
        "Depends on contribution value"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting the table
fig, ax = plt.subplots(figsize=(12, 3))
ax.axis('off')
table = tbl.table(ax, cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')

# Style the table
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1, 2)

# Bold headers
for (row, col), cell in table.get_celld().items():
    if row == 0:
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor('#40466e')
    else:
        cell.set_facecolor('#f1f1f2')

plt.tight_layout()
plt.show()
