salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев
need_money += spend - salary  # сумма для первого месяца
month_0 = 0
while month_0 <= 8:
    month_0 += 1
    spend += increase * spend  # траты
    need_money += spend - salary
print(round(need_money))
