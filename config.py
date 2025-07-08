# Global configuration variables

# Income tax bands for UK 2024/25
INCOME_TAX_BANDS = [
    {
        "band_name": "Personal Allowance",
        "lower_limit": 0,
        "upper_limit": 12570,
        "tax_rate": 0.0
    },
    {
        "band_name": "Basic Rate",
        "lower_limit": 12570,
        "upper_limit": 50270,
        "tax_rate": 0.2
    },
    {
        "band_name": "Higher Rate",
        "lower_limit": 50270,
        "upper_limit": 125140,
        "tax_rate": 0.4
    },
    {
        "band_name": "Additional Rate",
        "lower_limit": 125140,
        "upper_limit": None,  # No upper limit
        "tax_rate": 0.45
    }
]

# UK National Insurance bands for 2024/25 (Class 1, employee, not contracted out)
NI_BANDS = [
    {
        "band_name": "Below Primary Threshold",
        "lower_limit": 0,
        "upper_limit": 12570,
        "ni_rate": 0.0
    },
    {
        "band_name": "Main Rate",
        "lower_limit": 12570,
        "upper_limit": 50270,
        "ni_rate": 0.08  # 8%
    },
    {
        "band_name": "Upper Rate",
        "lower_limit": 50270,
        "upper_limit": None,  # No upper limit
        "ni_rate": 0.02  # 2%
    }
]

# Student loan plan 1 config
STUDENT_LOAN_PLAN = {
    "plan_name": "Plan 1",
    "threshold": 24275,      # Annual threshold for 2024/25
    "rate": 0.09             # 9% of income above threshold
}
