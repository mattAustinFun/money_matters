from config import INCOME_TAX_BANDS, NI_BANDS, STUDENT_LOAN_PLAN


def income_tax(gross_income: float) -> float:
    """
    Calculate total income tax deduction for a given gross annual income.
    """
    tax_due = 0.0
    for band in INCOME_TAX_BANDS:
        lower = band["lower_limit"]
        upper = band["upper_limit"] if band["upper_limit"] is not None else gross_income
        if gross_income > lower:
            taxable = min(gross_income, upper) - lower
            tax_due += taxable * band["tax_rate"]
        if band["upper_limit"] is not None and gross_income < band["upper_limit"]:
            break
    return tax_due


def national_insurance(gross_income: float) -> float:
    """
    Calculate total UK National Insurance deduction for a given gross annual income.
    """
    ni_due = 0.0
    for band in NI_BANDS:
        lower = band["lower_limit"]
        upper = band["upper_limit"] if band["upper_limit"] is not None else gross_income
        if gross_income > lower:
            taxable = min(gross_income, upper) - lower
            ni_due += taxable * band["ni_rate"]
        if band["upper_limit"] is not None and gross_income < band["upper_limit"]:
            break
    return ni_due


def student_loan(gross_income: float) -> float:
    """
    Calculate annual UK Student Loan repayment for Plan 1.
    """
    threshold = STUDENT_LOAN_PLAN["threshold"]
    rate = STUDENT_LOAN_PLAN["rate"]
    if gross_income > threshold:
        return (gross_income - threshold) * rate
    return 0.0


def pension_contribution(gross_income: float, pension_percentage: float) -> float:
    """
    Calculate annual pension contribution based on gross income and a given percentage.
    """
    return gross_income * pension_percentage


def deduction_items(
    gross_income: float,
    pension_percentage: float,
    is_sacrifice: bool
) -> dict:
    """
    Generate a summary of deductions for a given gross income.
    """
    pension_contribution_due = pension_contribution(
        gross_income, pension_percentage)
    
    if is_sacrifice:
        adjusted_gross_income = gross_income - pension_contribution_due
    else:
        adjusted_gross_income = gross_income

    items = {"pension": pension_contribution_due,
             "income_tax": income_tax(adjusted_gross_income),
             "national_insurance": national_insurance(adjusted_gross_income),
             "student_loan": student_loan(adjusted_gross_income)}
    return items


def deduction_total(deductions: dict) -> float:
    """
    Calculate the total deductions from a dictionary of deductions.
    """
    return sum(deductions.values())
