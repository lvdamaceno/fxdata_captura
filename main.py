import json
import requests
import variables


def auth(username, password):
    headers = {'content-type': 'application/json', }
    data = '{"username": "%s", "password": "%s"}' % (username, password)
    response = requests.post('https://api.login.fxdata.com.br/api/authenticate', headers=headers, data=data)
    json_data = json.loads(response.text)
    return json_data


def token():
    return auth(variables.USERNAME, variables.PASSWORD)['token']


def entrace_flow(company, branch):
    url = 'https://api.login.fxdata.com.br/api/data'
    headers = {'content-type': 'application/json', 'authorization': 'Token ' + token(), }
    data = '{"company": "%s", ' \
           ' "filter" : ["%s"], ' \
           ' "queries" : [{"alias": "entrace_flow", "metric": "entrace_flow", "by_establishment": true, ' \
           '"by_device": false, "period": {"from": "2019-01-01 00:00:00",  "to": "2019-12-31 23:59:59"}, ' \
           '"granularity": "day"}]}' % (company, branch)
    response = requests.post(url=url, headers=headers, data=data, )
    json_data = json.loads(response.text)
    return json_data


entrace = entrace_flow(variables.COMPANY, variables.PMIRANDA)
flow = entrace['data']['entrace_flow']['data'][0]['data']

for f in flow:
    print('5, ' + f['key'][:10] + ', ' + str(f['value']))