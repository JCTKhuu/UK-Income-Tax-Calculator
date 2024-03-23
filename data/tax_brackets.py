import sqlite3

connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()

def country_id(country_name):
    cursor.execute(
        """
        SELECT id
        FROM countries
        WHERE name = '{}'
        """.format(country_name)
    )
    
    return cursor.fetchone()[0]

england_id = country_id('England')
scotland_id = country_id('Scotland')

tax_brackets = [
    {'Country ID': england_id,  'Tax Year': 2023, 'Name': 'Personal Allowance', 'Tax Rate': 0,  'Bracket Upper Bound': 12570 },
    {'Country ID': england_id,  'Tax Year': 2023, 'Name': 'Basic Rate',         'Tax Rate': 20, 'Bracket Upper Bound': 50270 },
    {'Country ID': england_id,  'Tax Year': 2023, 'Name': 'Higher Rate',        'Tax Rate': 40, 'Bracket Upper Bound': 137840},
    {'Country ID': england_id,  'Tax Year': 2023, 'Name': 'Additional Rate',    'Tax Rate': 45, 'Bracket Upper Bound': 1e999 },
    {'Country ID': scotland_id, 'Tax Year': 2023, 'Name': 'Personal Allowance', 'Tax Rate': 0,  'Bracket Upper Bound': 12570 },
    {'Country ID': scotland_id, 'Tax Year': 2023, 'Name': 'Starter Rate',       'Tax Rate': 19, 'Bracket Upper Bound': 14732 },
    {'Country ID': scotland_id, 'Tax Year': 2023, 'Name': 'Basic Rate',         'Tax Rate': 20, 'Bracket Upper Bound': 25688 },
    {'Country ID': scotland_id, 'Tax Year': 2023, 'Name': 'Intermediate Rate',  'Tax Rate': 21, 'Bracket Upper Bound': 43662 },
    {'Country ID': scotland_id, 'Tax Year': 2023, 'Name': 'Higher Rate',        'Tax Rate': 42, 'Bracket Upper Bound': 137710},
    {'Country ID': scotland_id, 'Tax Year': 2023, 'Name': 'Additional Rate',    'Tax Rate': 47, 'Bracket Upper Bound': 1e999 }
]