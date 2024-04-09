import sqlite3

def income_tax_brackets() -> list:
    def country_id(country_name) -> int:
        connection = sqlite3.connect("mydatabase.db")
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id
            FROM countries
            WHERE name = '{}'
            """.format(country_name)
        )
        
        country_id = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return(country_id)
    
    england_id  = country_id('England')
    scotland_id = country_id('Scotland')

    return [
        # England, Wales and N. Ireland 2021
        {
            'Country ID'         : england_id,
            'Tax Year'           : 2021,
            'Name'               : 'Personal Allowance',
            'Tax Rate'           : 0,
            'Bracket Upper Bound': 12570
        },
        {
            'Country ID'         : england_id,
            'Tax Year'           : 2021,
            'Name'               : 'Basic Rate',
            'Tax Rate'           : 20,
            'Bracket Upper Bound': 50270
        },
        {
            'Country ID'         : england_id,
            'Tax Year'           : 2021,
            'Name'               : 'Higher Rate',
            'Tax Rate'           : 40,
            'Bracket Upper Bound': 162570
        },
        {
            'Country ID'         : england_id,
            'Tax Year'           : 2021,
            'Name'               : 'Additional Rate',
            'Tax Rate'           : 45,
            'Bracket Upper Bound': 1e999
        },
        # England, Wales and N. Ireland 2022
        {
            'Country ID'         : england_id,
            'Tax Year'           : 2022,
            'Name'               : 'Personal Allowance',
            'Tax Rate'           : 0,
            'Bracket Upper Bound': 12570
        },
        {
            'Country ID'         : england_id,
            'Tax Year'           : 2022,
            'Name'               : 'Basic Rate',
            'Tax Rate'           : 20,
            'Bracket Upper Bound': 50270
        },
        {
            'Country ID'         : england_id,
            'Tax Year'           : 2022,
            'Name'               : 'Higher Rate',
            'Tax Rate'           : 40,
            'Bracket Upper Bound': 162570
        },
        {
            'Country ID'         : england_id,
            'Tax Year'           : 2022,
            'Name'               : 'Additional Rate',
            'Tax Rate'           : 45,
            'Bracket Upper Bound': 1e999
        },
        # England, Wales and N. Ireland 2023
        {
            'Country ID'         : england_id,
            'Tax Year'           : 2023,
            'Name'               : 'Personal Allowance',
            'Tax Rate'           : 0,
            'Bracket Upper Bound': 12570
        },
        {
            'Country ID'         : england_id,
            'Tax Year'           : 2023,
            'Name'               : 'Basic Rate',
            'Tax Rate'           : 20,
            'Bracket Upper Bound': 50270
        },
        {
            'Country ID'         : england_id,
            'Tax Year'           : 2023,
            'Name'               : 'Higher Rate',
            'Tax Rate'           : 40,
            'Bracket Upper Bound': 137840
        },
        {
            'Country ID'         : england_id,
            'Tax Year'           : 2023,
            'Name'               : 'Additional Rate',
            'Tax Rate'           : 45,
            'Bracket Upper Bound': 1e999
        },

        # Scotland 2021
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2021,
            'Name'               : 'Personal Allowance',
            'Tax Rate'           : 0,
            'Bracket Upper Bound': 12570
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2021,
            'Name'               : 'Starter Rate',
            'Tax Rate'           : 19,
            'Bracket Upper Bound': 14667
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2021,
            'Name'               : 'Basic Rate',
            'Tax Rate'           : 20,
            'Bracket Upper Bound': 25296
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2021,
            'Name'               : 'Intermediate Rate',
            'Tax Rate'           : 21,
            'Bracket Upper Bound': 43662
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2021,
            'Name'               : 'Higher Rate',
            'Tax Rate'           : 41,
            'Bracket Upper Bound': 162570
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2021,
            'Name'               : 'Additional Rate',
            'Tax Rate'           : 46,
            'Bracket Upper Bound': 1e999
        },
        # Scotland 2022
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2022,
            'Name'               : 'Personal Allowance',
            'Tax Rate'           : 0,
            'Bracket Upper Bound': 12570
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2022,
            'Name'               : 'Starter Rate',
            'Tax Rate'           : 19,
            'Bracket Upper Bound': 14732
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2022,
            'Name'               : 'Basic Rate',
            'Tax Rate'           : 20,
            'Bracket Upper Bound': 25688
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2022,
            'Name'               : 'Intermediate Rate',
            'Tax Rate'           : 21,
            'Bracket Upper Bound': 43662
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2022,
            'Name'               : 'Higher Rate',
            'Tax Rate'           : 41,
            'Bracket Upper Bound': 162570
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2022,
            'Name'               : 'Additional Rate',
            'Tax Rate'           : 46,
            'Bracket Upper Bound': 1e999
        },
        # Scotland 2023
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2023,
            'Name'               : 'Personal Allowance',
            'Tax Rate'           : 0,
            'Bracket Upper Bound': 12570
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2023,
            'Name'               : 'Starter Rate',
            'Tax Rate'           : 19,
            'Bracket Upper Bound': 14732
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2023,
            'Name'               : 'Basic Rate',
            'Tax Rate'           : 20,
            'Bracket Upper Bound': 25688
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2023,
            'Name'               : 'Intermediate Rate',
            'Tax Rate'           : 21,
            'Bracket Upper Bound': 43662
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2023,
            'Name'               : 'Higher Rate',
            'Tax Rate'           : 42,
            'Bracket Upper Bound': 137710
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2023,
            'Name'               : 'Additional Rate',
            'Tax Rate'           : 47,
            'Bracket Upper Bound': 1e999
        },
        # Scotland 2024
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2024,
            'Name'               : 'Personal Allowance',
            'Tax Rate'           : 0,
            'Bracket Upper Bound': 12570
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2024,
            'Name'               : 'Starter Rate',
            'Tax Rate'           : 19,
            'Bracket Upper Bound': 14876
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2024,
            'Name'               : 'Basic Rate',
            'Tax Rate'           : 20,
            'Bracket Upper Bound': 26561
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2024,
            'Name'               : 'Intermediate Rate',
            'Tax Rate'           : 21,
            'Bracket Upper Bound': 43662
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2024,
            'Name'               : 'Higher Rate',
            'Tax Rate'           : 42,
            'Bracket Upper Bound': 75000
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2024,
            'Name'               : 'Higher Rate',
            'Tax Rate'           : 45,
            'Bracket Upper Bound': 137710
        },
        {
            'Country ID'         : scotland_id,
            'Tax Year'           : 2024,
            'Name'               : 'Additional Rate',
            'Tax Rate'           : 48,
            'Bracket Upper Bound': 1e999
        }
    ]

def personal_allowance_income_limit() -> list:
    return [
        {
            'Tax Year'           : 2021,
            'Income Limit'       : '100000'
        },
        {
            'Tax Year'           : 2022,
            'Income Limit'       : '100000'
        },
        {
            'Tax Year'           : 2023,
            'Income Limit'       : '100000'
        },
        {
            'Tax Year'           : 2024,
            'Income Limit'       : '100000'
        }
    ]