from dbfread import DBF

from auto_forms import fill_form
from validator import sale_validator


def load_valid_sales():
    sales = DBF("sales.dbf")

    valid_sales = []

    for sale in sales:
        if sale_validator(sale):
            valid_sales.append(sale)

    return valid_sales


sales = load_valid_sales()

for sale in sales:
    print("Preenchendo o Formulário de", sale["FULL_NAME"])
    fill_form(sale)

print("Finalizado")
input()


