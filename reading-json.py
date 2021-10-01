import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

data['people'].append({
    'name': 'Cristian',
    'website': 'test.com'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')

############################# NESTED JSON ###########
#"bills": [
#{
#  "url": "http:\/\/maplight.org\/us-congress\/bill\/110-hr-195\/233677",

#  "organizations": [
#    {
#      "organization_id": "22973",
#      "name": "National Health Federation",
#    },
#    {
#      "organization_id": "27059",
#      "name": "A Christian Perspective on Health Issues",
#    },
#    {
#      "organization_id": "27351",
#      "name": "Natural Health Roundtable",
#    }
#  ]
#}

for bill in data['bills']:
    for organization in bill['organizations']:
        print (organization.get('name'))

# OR

for i in data['bills']['organizations']:
    print(organization.get('name'))


