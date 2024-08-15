def format_phone_number(number):
    new_number = ''.join(filter(str.isdigit, number))
    if len(new_number) == 10 :
        sdtquocte = f"{new_number[0:4]}-{new_number[4:6]}-{new_number[6:]}"
        return sdtquocte
    elif new_number[0] != 0 :
        return 'Invalid phone number'
    else:
        return 'Invalid phone number'
number = str(input('Mời bạn nhập chuối số bất kỳ : '))
print(format_phone_number(number))