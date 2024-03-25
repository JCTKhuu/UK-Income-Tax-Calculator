from math import inf
import sqlite3
import data.tax_information as tax_information
import data.create_tables as create_tables
import data.populate_tables as populate_tables
import os

class TaxBracket:
    def __init__(self, rate: float, lower_bound: float, upper_bound: float) -> None:
        self.rate        = float(rate)
        self.lower_bound = float(lower_bound)
        self.upper_bound = float(upper_bound)

    def __str__(self) -> str:
        return(
            str({
                'Rate': self.rate,
                'Lower bound': self.lower_bound,
                'Upper bound': self.upper_bound
                }
            )
        )

class TaxInformation:
    def __init__(
        self,
        net_income: float,
        country   : str,
        tax_year  : int,
        database  : str = 'mydatabase.db'
    ) -> None:
        def load_personal_allowance_income_limit(self) -> None:
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT income_limit
                FROM personal_allowance_income_limit
                WHERE tax_year = {}
                ;
                """.format(self.tax_year)
            )

            self.personal_allowance_income_limit = cursor.fetchone()[0]

            cursor.close()
            connection.close()

        def load_and_calc_income_tax_brackets(self) -> None:
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    tax_brackets.name,
                    tax_brackets.rate,
                    tax_brackets.bracket_upper_bound
                FROM tax_brackets
                JOIN countries ON countries.id = tax_brackets.country_id
                WHERE   countries.name = '{}'
                    AND tax_brackets.tax_year = {}
                ORDER BY tax_brackets.bracket_upper_bound ASC
                ;
                """.format(self.country, self.tax_year)
            )

            tax_bracket_list = cursor.fetchall()

            bracket_lower_bound = 0
            for tax_bracket in tax_bracket_list:
                # Determine personal allowance based on income
                if (    tax_bracket[0] == 'Personal Allowance'
                    and self.net_income > self.personal_allowance_income_limit):
                    self.income_tax_brackets.append(
                        TaxBracket(
                            rate        = tax_bracket[1],
                            lower_bound = bracket_lower_bound,
                            upper_bound = max(tax_bracket[2] - (self.net_income - self.personal_allowance_income_limit) / 2, 0)
                        )
                    )
                else:
                    self.income_tax_brackets.append(
                        TaxBracket(
                            rate        = tax_bracket[1],
                            lower_bound = bracket_lower_bound,
                            upper_bound = tax_bracket[2]
                        )
                    )

                bracket_lower_bound = self.income_tax_brackets[-1].upper_bound

            connection.close()
        
        # --------------------------------------------------
        self.net_income                      = net_income
        self.country                         = country
        self.tax_year                        = tax_year
        self.database                        = database
        self.personal_allowance_income_limit = 0
        self.income_tax_brackets             = []

        load_personal_allowance_income_limit(self)
        load_and_calc_income_tax_brackets(self)

    def __str__(self) -> str:
        tax_bracket_list = []

        for tax_bracket in self.income_tax_brackets:
            tax_bracket_list.append(str(tax_bracket))

        return(
            str(tax_bracket_list)
        )

def income_tax(tax_information: TaxInformation) -> float:
    net_income = tax_information.net_income
    income_tax = 0

    for tax_bracket in tax_information.income_tax_brackets:
        # If income is not relevant to (less than) this tax bracket, skip to next tax bracket
        if net_income < tax_bracket.lower_bound:
            continue

        # If income is above this tax bracket, tax full amount from this bracket
        if net_income > tax_bracket.upper_bound:
            income_tax += (tax_bracket.upper_bound - tax_bracket.lower_bound) * tax_bracket.rate / 100
        # If income is in this tax bracket, only tax up to income
        elif net_income <= tax_bracket.upper_bound:
            income_tax += (net_income - tax_bracket.lower_bound) * tax_bracket.rate / 100

    return(income_tax)

if __name__ == '__main__':
    create_tables.create_tables()
    populate_tables.populate_tables()

    test_tax_info_1 = TaxInformation(
        net_income   = 200000,
        country  = 'England',
        tax_year = 2023
    )
    print(test_tax_info_1)
    print(income_tax(test_tax_info_1))

