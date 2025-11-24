goal = 5000
after_5_years = 5
money_i_need = (goal* 12 *after_5_years)

print(money_i_need)

montly_saved = [3000, 4000, 5000, 7000,10000]
for i,saved in enumerate(montly_saved,1):
    months = money_i_need // saved
    years = months // 12
    extra_months = months % 12
    print(f"{i}. I am saving {saved:,} lv  {years} year in {extra_months} months")