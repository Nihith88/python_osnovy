from sys import argv


script_name, prod_per_hour, tax_per_hour, bonus = argv

print("Выработка в час: ", prod_per_hour)
print("Ставка в час: ", tax_per_hour)
print("Премия: ", bonus)

print(f"Заработная плата рсотрудника: {float(prod_per_hour) * float(tax_per_hour) + float(bonus)} руб.")
