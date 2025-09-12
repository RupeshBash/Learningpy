import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import colors

# Full dataset
data = [
    ["Jersey Front Centre", "Title Sponsor", "Fixed (High Value)"],
    ["Jersey Top Left (Chest)", "Organizer Logo", "N/A"],
    ["Jersey Top Right (Chest)", "Co-Sponsor", "Fixed"],
    ["Jersey Left Sleeve", "Independent Sponsor", "Negotiable"],
    ["Jersey Right Sleeve", "Independent Sponsor", "Negotiable"],
    ["Jersey Upper Back (Below Collar)", "Independent Sponsor", "Negotiable"],
    ["Jersey Lower Back (Above Number)", "Independent Sponsor", "Negotiable"],
    ["Cap Front Panel (Centre)", "Title Sponsor", "Fixed (High Value)"],
    ["Cap Left Side Panel", "Co-Sponsor", "Fixed"],
    ["Cap Right Side Panel", "Independent Sponsor", "Negotiable"],
    ["Cap Back Strap Area", "Independent Sponsor", "Negotiable"],
    ["Cap Bottom (Under Brim)", "Organizer Logo", "N/A"]
]

# Split data
jersey_data = [row for row in data if row[0].startswith("Jersey")]
cap_data = [row for row in data if row[0].startswith("Cap")]

# Column headers
columns = ["Position", "Sponsor Type", "Sponsorship Amount"]

def draw_colored_table(df, title, filename):
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.set_title(title, fontsize=16, weight='bold', pad=20)
    ax.axis('off')

    table = ax.table(cellText=df.values, colLabels=[f"{col}" for col in df.columns],
                     cellLoc='center', loc='center', colColours=["#40466e"]*3)

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.6)

    # Color alternating rows
    for i in range(len(df)):
        color = '#f0f0f5' if i % 2 == 0 else '#ffffff'
        for j in range(len(columns)):
            table[(i+1, j)].set_facecolor(color)

            # Highlight special cases
            if df.iloc[i, 2] in ["Fixed (High Value)", "Fixed"]:
                table[(i+1, 2)].set_facecolor('#d0f0c0')  # Light green
                table[(i+1, 2)].set_text_props(weight='bold')

            if df.iloc[i, 2] == "N/A":
                table[(i+1, 2)].set_facecolor('#ffdddd')  # Light red
                table[(i+1, 2)].set_text_props(weight='bold')

    # Bold headers
    for key, cell in table.get_celld().items():
        if key[0] == 0:
            cell.set_text_props(weight='bold', color='white')

    plt.savefig(filename, bbox_inches='tight')
    plt.show()

# Create DataFrames
jersey_df = pd.DataFrame(jersey_data, columns=columns)
cap_df = pd.DataFrame(cap_data, columns=columns)

# Draw tables
draw_colored_table(jersey_df, "Jersey Sponsorship Layout", "jersey_sponsorship_layout.png")
draw_colored_table(cap_df, "Cap Sponsorship Layout", "cap_sponsorship_layout.png")
