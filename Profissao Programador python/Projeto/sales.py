from dbfread import DBF

from validator import sale_validator

# Mostrando na tela o que esta acontecendo. Mostrando nossa base de dados
# for record in DBF("sales.dbf"):
#     print(record)


def load_valid_sales():
    sales = DBF("sales.dbf")

    valid_sales = []

    for sale in sales:
        if sale_validator(sale):
            valid_sales.append(sale)

    return valid_sales


sales = load_valid_sales()

for sale in sales:
    print(sale["FULL_NAME"])
