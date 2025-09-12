import matplotlib.pyplot as plt

# Expense categories and their respective costs
categories = [
    "Venue (32 hrs)", 
    "Umpire (3 days)", 
    "Scorer (3 days)",
    "Refreshments",  
    "Jersey (120 pcs)",
    "Winner + Runner-up", 
    "Miscellaneous",
    "Trophies & Medals"
]

costs = [
    38400,  # Venue
    3000,  # Umpire
    3000,   # Scorer
    30000,  # Refreshments
    40000,  #jersey
    35000,  # Prizes
    20000,  #miscellaneous
    15000   # Trophies & Medals
]

# Create horizontal bar graph
plt.figure(figsize=(12, 7))
bars = plt.barh(categories, costs, color='skyblue')
plt.xlabel("Cost (NPR)")
plt.title("VibeX Indoor Interschool Cup - Expense Budget Breakdown")

# Add labels to each bar
for bar in bars:
    width = bar.get_width()
    plt.text(width + 1000, bar.get_y() + bar.get_height() / 2,
             f"NPR {width:,}", va='center', fontsize=9)

# Styling
plt.tight_layout()
plt.gca().invert_yaxis()  # Highest cost appears on top
plt.grid(axis='x', linestyle='--', alpha=0.6)

# Show plot
plt.show()
