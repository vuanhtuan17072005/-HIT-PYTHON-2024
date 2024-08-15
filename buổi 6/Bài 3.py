def tinh(operation,*args):
    if operation == 'add':
        return sum(args)
    elif operation == 'multiply':
        tich = 1
        for num in args:
            tich *= num
        return tich
    elif operation == 'max':
        return max(args)
    elif operation == 'min':
        return min(args)
    else:
        return 'Invalid operation'
print('Tổng tất cả các số là:',tinh('add',2,3,4,5))
print('Tích tất cả các số là:',tinh('multiply',2,3,4,5))
print('Max=',tinh('max',2,3,4,5))
print('Min=',tinh('min',2,3,4,5))
print(tinh('addddd',2,3,4,5))