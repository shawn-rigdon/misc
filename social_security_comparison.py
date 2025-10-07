# Compare total payments received from early retirement vs full retirement

import numpy as np
import matplotlib.pyplot as plt

partial_payment = 2831
full_payment = 4018
compound_rate = 0.04
savings_rate = 0.20

age = np.arange(62, 100, 1.0/12, dtype=np.float32)

monthly_compound_rate = (1 + compound_rate) ** (1/12) - 1

def calculate_total_payments(age_arr, start_age, payment, per_payment_compound_rate, savings_rate):
    cumulative_interest = np.zeros_like(age, dtype=np.float32)
    cumulative_savings = np.zeros_like(age, dtype=np.float32)
    total_balance = np.zeros_like(age_arr, dtype=np.float32)
    start_index = 12 * (start_age - int(age_arr[0])) # assume age_arr starts with an integer age
    for i in range(start_index, len(age_arr)):
        if i == start_index:
            cumulative_interest[i] = 0
            cumulative_savings[i] = savings_rate * payment
            total_balance[i] = payment
            continue
        cumulative_interest[i] = cumulative_savings[i-1] * per_payment_compound_rate 
        cumulative_savings[i] = cumulative_savings[i-1] + cumulative_interest[i] + savings_rate * payment
        total_balance[i] = total_balance[i-1] + cumulative_interest[i] + payment
    return total_balance

partial_total = calculate_total_payments(age, 62, partial_payment, monthly_compound_rate, savings_rate)
full_total = calculate_total_payments(age, 67, full_payment, monthly_compound_rate, savings_rate)

plt.plot(age, partial_total, label='Early Retirement', color='blue')
plt.plot(age, full_total, label='Full Retirement', color='orange')
plt.xlabel('Age')
plt.ylabel('Total Payments ($)')
plt.title('Retirement Payments Over Time')
plt.legend()
plt.show()
