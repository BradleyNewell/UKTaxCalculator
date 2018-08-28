def printy_func(gross_income, percentage):
    print("Your Tax Rate is " + str(percentage) + '%')
    perc_amount = (gross_income / 100) * percentage
    net_wage = gross_income - perc_amount
    print("Your Gross income is: £" + str("{0:.2f}".format(gross_income)))
    print('You must pay: £' + str("{0:.2f}".format(perc_amount) + ' in taxes this year.'))
    print("You will effectively earn: £" + str("{0:.2f}".format(net_wage)))