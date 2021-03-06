#!/usr/bin/python3
# -*- coding: ascii -*-
#Importing currencies will demonstrate the effects of currency
import click
import json
from api import currency_converter
#added a "greet" statement to prompt the user on inputs
greet = input("Hello!, what currency would you like to translate")
print(greet)
type = ('USD','EUR','GBP','JPY','CHF','CAD','ZAR')
if greet == type:
    print('Are you sure this is the type you want?')
@click.command()
@click.option('--amount', nargs=1, type=float)
@click.option('--input_currency', nargs=1)
@click.option('--output_currency')
def main(amount, input_currency, output_currency):
    resp = currency_converter(amount, input_currency, output_currency)
    print(json.dumps(resp if isinstance(resp, dict) else resp[0], indent=4))

#an if statement to compare the function and variable
if __name__ == "__main__":
    main()
#call the main function of the program 
