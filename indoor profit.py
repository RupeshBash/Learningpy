import matplotlib.pyplot as plt

# Constants
number_of_teams = 12
entry_fee_per_team = 15000
sponsorship_percentage = 0.50  # 50% of expected sponsorship
expected_sponsorship = 100000  # example value; change this based on your Canva proposal

# Calculations
total_entry_fees = number_of_teams * entry_fee_per_team
actual_sponsorship = expected_sponsorship * sponsorship_percentage
total_income = total_entry_fees + actual_sponsorship

# Example estimated expenses (replace with your actual budget breakdown)
estimated_expenses = 120000  # example value

# Profit calculation
profit = total_income - estimated_expenses

# Bar graph data
categories = ['Entry Fees', 'Sponsorship', 'Expenses', 'Profit']
values = [total_entry_fees, actual_sponsorship, estimated_expenses, profit]

# Plotting
plt.figure(figsize=(8, 6))
bars = plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'])
plt.title('Tournament Financial Summary')
plt.ylabel('Amount (in NPR)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, height, f'{int(height)}', ha='center', va='bottom')

plt.tight_layout()
plt.show()
