from tax_calc import printy_Func as pf

running = True


def tax_amount(gross_income):
    p_allow = 11859
    if gross_income <= 0:
        print("Enter a valid number")
    elif gross_income <= p_allow:
        pf.printy_func(gross_income, 0)
    elif 46350 >= gross_income > p_allow:
        pf.printy_func(gross_income, 20)
    elif 150000 >= gross_income >= 46351:
        pf.printy_func(gross_income, 40)
    elif gross_income >= 150001:
        pf.printy_func(gross_income, 45)


while running:
    g_income = input("Enter your gross income: £")
    try:
        x = int(g_income)
        tax_amount(x)
    except ValueError:
        running = False


