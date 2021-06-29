import sys

def calculator(num):
    shouldpay = num - 5000 - num * 0.165
    if shouldpay <= 0:
        tax = 0
        salsry = income - tax - num * 0.165
        return(salsry)
    elif 0 < shouldpay <= 3000:
        tax = shouldpay * 0.03
        salsry = income - tax - num * 0.165
        return(salsry)
    elif 3000 < shouldpay <= 12000:
        tax = shouldpay * 0.1 - 210
        salsry = income - tax - num * 0.165
        return(salsry)
    elif 12000 < shouldpay <= 25000:
        tax = shouldpay * 0.2 - 1410
        salsry = income - tax - num * 0.165
        return(salsry)
    elif 25000 < shouldpay <= 35000:
        tax = shouldpay * 0.25 - 2660
        salsry = income - tax - num * 0.165
        return(salsry)
    elif 35000 < shouldpay <= 55000:
        tax = shouldpay * 0.3 - 4410
        salsry = income - tax - num * 0.165
        return(salsry)
    elif 55000 < shouldpay <= 80000:
        tax = shouldpay * 0.35 - 7160
        salsry = income - tax - num * 0.165
        return(salsry)
    else:
        tax = shouldpay * 0.45 - 15160
        salsry = income - tax - num * 0.165
        return(salsry)

for i in sys.argv[1:]:
    id,income = i.split(':')
    income = int(income)
    salsry = 0
    shouldpay = 0
    tax = 0
    print('{}:{:.2f}'.format(id,calculator(income)))

