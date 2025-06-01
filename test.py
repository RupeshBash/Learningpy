import matplotlib.pyplot as plt

# Budget categories and their estimated costs in NPR
categories = [
    "Venue (14 days)",
    "Team Logistics",
    "Marketing & Media",
    "Umpires (27 matches)",
    "Match Awards (27 matches)",
    "Best Batter & Bowler",
    "Operations/Admin",
    "Winner Prize",
    "Runner-up Prize"
]

costs = [
    15000 * 14,           # Venue cost
    180000,               # Team logistics
    100000,               # Marketing & Media
    5000 * 27,            # Umpires
    3000 * 27,            # Match awards
    10000 * 2,            # Best Batter & Bowler
    120000,               # Operations/Admin
    120000,               # Winner Prize
    50000                 # Runner-up Prize
]

# Plotting the bar graph
plt.figure(figsize=(12, 7))
bars = plt.barh(categories, costs, color='skyblue')
plt.xlabel("Cost in NPR")
plt.title("Estimated Budget Breakdown for Vibex T20 Tournament")

# Annotate each bar with cost
for bar, cost in zip(bars, costs):
    plt.text(cost + 1000, bar.get_y() + bar.get_height()/2, f"Rs. {cost:,}", va='center')

plt.tight_layout()
plt.gca().invert_yaxis()  # Highest cost at top
plt.show()
