# Write a program that computes the net amount of a bank account based a
# transaction log from console input. The transaction log format is shown as
# following:
#   D 100
#   W 200
# D means deposit while W means withdrawal.
# 
# Suppose the following input is supplied to the program:
#   D 300
#   D 300
#   W 200
#   D 100
# 
# Then, the output should be:
#   500

funds = 0

while True:
    transaction = input().upper()
    if not transaction:
        break
    
    try:
        operation_value = float(transaction[2:])
    except:
        continue
    
    if transaction[0] == 'D':
        funds += operation_value
    elif transaction[0] == 'W':
        funds -= operation_value
    else:
        continue
    
print(funds)
        