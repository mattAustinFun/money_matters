from deductions import deduction_items, deduction_total


def annual_to_monthly(annual: dict) -> dict:
    """
    Convert annual deduction values to monthly values.
    Returns a new dictionary with the same keys and monthly values (rounded to 2 decimals).
    """
    monthly = {}
    for key, value in annual.items():
        monthly[key] = round(value / 12, 2)
    return monthly


def annual_summary(gross_income: float, pension_contribution: float, is_sacrifice: bool) -> dict:
    """
    Generate an annual summary of deductions for a given gross income.
    """
    annual_summary = deduction_items(
        gross_income, pension_contribution, is_sacrifice)
    annual_summary["total_deductions"] = deduction_total(annual_summary)
    annual_summary["net_income"] = gross_income - \
        annual_summary["total_deductions"]
    return annual_summary


def monthly_summary(gross_income: float, pension_contribution: float, is_sacrifice: bool) -> dict:
    """
    Generate a monthly summary of deductions for a given gross income.
    """
    monthly_summary_data = {"gross_income": round(gross_income / 12, 2)}
    monthly_summary_data.update(annual_to_monthly(
        annual_summary(gross_income, pension_contribution, is_sacrifice)))

    return monthly_summary_data


def salary_range_report(
    start: float, end: float, step: float, pension_contribution: float, is_sacrifice: bool
) -> list:
    """
    Generate a report of monthly summaries for a range of gross incomes.
    Returns a list of dictionaries, each containing the monthly summary for a specific gross income.
    """
    report = []
    report_line = {}
    for gross_income in range(int(start), int(end) + 1, int(step)):
        monthly_summary_data = monthly_summary(
            gross_income, pension_contribution, is_sacrifice)
        report_line = {"annual_gross_income": gross_income,
                       "gross_income": monthly_summary_data["gross_income"],
                       "pension": monthly_summary_data["pension"],
                       "income_tax": monthly_summary_data["income_tax"],
                       "national_insurance": monthly_summary_data["national_insurance"],
                       "student_loan": monthly_summary_data["student_loan"],
                       "total_deductions": monthly_summary_data["total_deductions"],
                       "net_income": monthly_summary_data["net_income"],
                       }
        report.append(report_line)
    return report


