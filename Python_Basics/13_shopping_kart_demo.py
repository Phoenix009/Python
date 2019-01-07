data = {"nike": {"running shoes": {"price": 3995, "size": {"6": 3, "7": 0, "8": 1, "9": 3}},
                 "casual shoes": {"price": 5295, "size": {"6": 1, "7": 3, "8": 0, "9": 4}}},
        "adidas": {"cricket shoes": {"price": 4595, "size": {"6": 1, "7": 3, "8": 5, "9": 0}},
                   "football shoes": {"price": 2759, "size": {"6": 0, "7": 2, "8": 4, "9": 0}}}}


coupons = {"50OFF": 0.5, "80OFF": 0.8, "20OFF": 0.2}

total_bill = 0
shop_flag = True
while shop_flag:
    brand = input("What brand do you want to buy :").lower()
    if brand not in data:
        print("Sorry, Yhe requested brand is currently unavailable")
        print()
    else:
        kind = input("Enter the type of shoes you want to buy :").lower()
        foot_size = input("Enter the foot length :").lower()
        print()
        if kind not in data[brand]:
            print("Sorry, The type of shoes are not available")
            print()
        else:
            if data[brand][kind]["size"][foot_size] == 0:
                print("Sorry, The foot length is not available")
                print()
            else:
                print("Price :", data[brand][kind]["price"])
                print("Stock available :", data[brand][kind]["size"][foot_size])
                print()
                buy_flag = input("Do YOu want to buy (Y/N) :").upper()
                if buy_flag == "Y":
                    total_bill += data[brand][kind]["price"]
                    print("Adding to oyur cart...")
                    print()
    shop_flag = input("Do you want to continue shopping(Y/N) :").upper()
    if shop_flag == "N":
        break

print("Your Total Bill is :", total_bill)
coupon_flag = input("Do You want to apply any coupon :").upper()
if coupon_flag == "Y":
    user_coupon = input("Enter the coupon :")
    if user_coupon not in coupons:
        print("Invalid Coupon")
    else:
        print("The Coupon is applied")
        total_bill -= total_bill*coupons[user_coupon]

print()
print("Your Bill :", total_bill)
print("Thank You")


