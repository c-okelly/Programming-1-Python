def tax(income):
    income_1 = income * 0.6
    income_2 = income * 0.4

    first_level = income_1 * 0.135
    second_level = income_2 * 0.23

    total_tax = first_level + second_level

    total = total_tax + income

    print 'Income is', income, "tax due is", total_tax
    print "The total amount of inital price plus tax is", total

tax(10000)
