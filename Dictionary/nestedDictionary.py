nested_dict = {
    'key1': {
        'nested_key1': 'value1',
        'nested_key2': 'value2'
    },
    'key2': {
        'nested_key3': 'Fucking',
        'nested_key4': 'value4'
    }
}
nested_dict['key1']['nested_key2'] = nested_dict['key2']['nested_key3']
print(nested_dict)

d = {}
n = 3
for i in range(n):
    d2 = {}
    for j in range(i+1):
        d2[j] = j+1
    d[i] = d2

print(d)

# using dict constructor
d3 = dict(outer_key1=dict(inner_key1="innerValue1"),outer_key2 = dict(inner_key2 = "innerValue2"))
print(d3)
