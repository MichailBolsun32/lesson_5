immutable_var = (10, 11, 'abc', 'def')
print(f'immutable tuple: {immutable_var}')

mutable_list =[10, 11, 'abc', 'def']
mutable_list[0] += 1
print(f'mutable_list list modified: {mutable_list}')