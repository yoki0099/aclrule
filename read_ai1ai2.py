
dict_map = {}
with open('./Clash/openai1.list', 'r') as file:
    for line in file:
        if line.startswith('DOMAIN-'):
            #print(line.strip())
            items = line.split(',')
            if(dict_map.get(items[1]) == None):
                dict_map[items[1]] = items[0]
            else:
                print(items[1])

with open('./Clash/openai2.list', 'r') as file:
    for line in file:
        if line.startswith('DOMAIN-'):
            #print(line.strip())
            items = line.split(',')
            if(dict_map.get(items[1]) == None):
                dict_map[items[1]] = items[0]
            else:
                print(items[1])