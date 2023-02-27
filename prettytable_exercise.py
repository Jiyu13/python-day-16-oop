from prettytable import PrettyTable

# x = PrettyTable()
table = PrettyTable()
# print(table)


# x.add_column(column_name, column_data_list)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# print(table)


# change table style
# print(table.align)
table.align = "l"
print(table)
