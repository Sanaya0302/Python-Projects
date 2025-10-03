def tip(bill_amount,total_tip):
    total=bill_amount*(1+0.01*total_tip)
    total=round(total,2)
    print(f"please pay ${total}")
tip(120,20)