D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
D['food']
D['quantity'] += 10

dic = {}
print("Input name: ", end="")
dic['name'] = input()
print("Input age: ", end="")
dic['age'] = input()
for key in dic:
    print(key + " - " + dic[key])

# Вложенность хранения данных
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
       'job': ['dev', 'mgr'],
       'age': 18}
print(rec['name'], rec['name']['firstname'], rec['job'])
rec['job'].append('janitor')
for key, value in rec.items():
    print(f"{key} - {value}")