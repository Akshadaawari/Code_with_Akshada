format_numeric=lambda num: f"{num:e}" if isinstance (num,int) else f"{num:,.2f}"
print("int Formatting :",format_numeric(10000000))