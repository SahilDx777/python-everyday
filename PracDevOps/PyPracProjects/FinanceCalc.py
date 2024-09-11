def calculate_finance(monthly_income, tax_rate, currency, approx_monthly_expenses) -> None:
    monthly_tax = monthly_income * (tax_rate / 100)
    monthly_net_income = monthly_income - monthly_tax
    yearly_salary = monthly_income * 12
    yearly_tax = monthly_tax * 12
    yearly_net_income = yearly_salary - yearly_tax
    approx_savings = monthly_net_income - approx_monthly_expenses

    print("--------------------------")
    print(f"Monthly Income: {currency}{monthly_income:,.2f}")
    print(f"Tax Rate: {tax_rate:,.2f}")
    print(f"Monthly Tax: {currency}{monthly_tax:,.2f}")
    print(f"Monthly Net Income: {currency}{monthly_net_income:,.2f}")
    print(f"Yearly Salary: {currency}{yearly_salary:,.2f}")
    print(f"Yearly Tax Paid: {currency}{yearly_tax:,.2f}")
    print(f"Yearly Net income: {currency}{yearly_net_income:,.2f}")
    print(f"Total monthly Savings After Expenses: {approx_savings}")
    print("---------------------------")


def main() -> None:
    monthly_income = float(input("Enter Your Monthly Salary In Numbers: "))
    tax_rate = float(input("Enter Your Tax Rate(%) In Numbers: "))
    approx_monthly_expenses = float(input("Enter Your Approximate Monthly Expenses In Numbers: "))

    calculate_finance(monthly_income, tax_rate, "Rs", approx_monthly_expenses)


if __name__ == "__main__":
    main()
