
# This code generates a monthly summary of deductions based on the provided gross income, pension contribution percentage, and whether the pension is a salary sacrifice.
# It then prints the summary to the console and saves it to a CSV file named 'monthly_summary.csv'. 
# The summary includes gross income, pension contribution, income tax, national insurance, student loan, total deductions, and net income.
# The values are rounded to two decimal places for better readability. 

from tools import monthly_summary, salary_range_report
from pathlib import Path
from csv import writer

pension_percentage = 0.03  # 15% pension contribution
is_sacrifice = False

salary_report = salary_range_report(
    start=24000, 
    end=44000,      
    step=2000,
    pension_contribution=pension_percentage, 
    is_sacrifice=is_sacrifice
)   
with open(Path(__file__).parent / 'monthly_summary.csv', 'w', newline='') as csvfile:
    csv_writer = writer(csvfile)    
    csv_writer.writerow([
        "Annual Gross Income", 
        "Gross Income", 
        "Pension Contribution",
        "Income Tax",
        "National Insurance",
        "Student Loan",
        "Total Deductions",
        "Net Income"
    ])
    for item in salary_report:
        csv_writer.writerow([   
            item["annual_gross_income"],
            item["gross_income"],
            item["pension"],    
            item["income_tax"],
            item["national_insurance"],
            item["student_loan"],   
            item["total_deductions"],
            item["net_income"]
        ])          
print(f"Monthly summary saved to {Path(__file__).parent / 'monthly_summary.csv'}")
