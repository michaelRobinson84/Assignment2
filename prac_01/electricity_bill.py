TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff_choice = int(input("Which tariff? 11 or 31: "))

daily_use = float(input("Enter daily use in kWh: "))

number_of_days = int(input("Enter number of billing days: "))

if tariff_choice == 11:
    estimated_bill = TARIFF_11 * daily_use * number_of_days
elif tariff_choice == 31:
    estimated_bill = TARIFF_31 * daily_use * number_of_days

print(f"Estimated bill: ${estimated_bill:.2f}")