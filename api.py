from fastapi import FastAPI, Path, HTTPException
from tax_information import TaxInformation

app = FastAPI()

@app.get("/income-tax")
def get_income_tax(
    gross_income: float,
    country:      str,
    tax_year:     int,
):
    errors = []

    if gross_income < 0:
        errors.append("Gross income must not be negative")

    if country.capitalize() in ["England", "Northern Ireland", "Wales"]:
        tax_country = "England"
    elif country.capitalize() == "Scotland":
        tax_country = "Scotland"
    else:
        errors.append("Country not found in the UK")

    if tax_year < 2021 or tax_year > 2023:
        errors.append("Only tax years 2021-2023 inclusive are supported")

    if len(errors) > 0:
        raise HTTPException(status_code=404, detail=". ".join(errors) + ".")

    # --------------------------------------------------
    tax_information = TaxInformation(
        gross_income = gross_income,
        country      = tax_country,
        tax_year     = tax_year
    )

    return(
        tax_information.income_tax()
    )