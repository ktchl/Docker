import os
import requests
import json
import time

# définition de l'adresse de l'API
api_address = 'fastapi'
# port de l'API
api_port = 8000

time.sleep(30)
# requête
r1 = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'life is beautiful'
    }
)

r2 = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'that sucks'
    }
)

r3 = requests.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'life is beautiful'
    }
)

r4 = requests.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'that sucks'
    }
)

r1_score = json.loads(r1.content.decode('utf-8')).get('score')
r2_score = json.loads(r2.content.decode('utf-8')).get('score')
r3_score = json.loads(r3.content.decode('utf-8')).get('score')
r4_score = json.loads(r4.content.decode('utf-8')).get('score')

output1 = '''
============================
    Content test
============================

request done at "/v1/sentiment"
| username="alice"
| password="wonderland"
| sentence="life is beautiful"

expected result = positif
actual restult = {r1_score}

==>  {test_status1}

'''

output2 = '''
============================
    Content test
============================

request done at "/v1/sentiment"
| username="alice"
| password="wonderland"
| sentence="that sucks"

expected result = négatif
actual restult = {r2_score}

==>  {test_status2}

'''

output3 = '''
============================
    Content test
============================

request done at "/v2/sentiment"
| username="alice"
| password="wonderland"
| sentence="life is beautiful"

expected result = positif
actual restult = {r3_score}

==>  {test_status3}

'''

output4 = '''
============================
    Content test
============================

request done at "/v2/sentiment"
| username="alice"
| password="wonderland"
| sentence="that sucks"

expected result = négatif
actual restult = {r4_score}

==>  {test_status4}

'''



if r1_score > 0:
    test_status1 = 'SUCCESS'
else:
    test_status1 = 'FAILURE'

if r2_score < 0:
    test_status2 = 'SUCCESS'
else:
    test_status2 = 'FAILURE'

if r3_score > 0:
    test_status3 = 'SUCCESS'
else:
    test_status3 = 'FAILURE'

if r4_score < 0:
    test_status4 = 'SUCCESS'
else:
    test_status4 = 'FAILURE'

if os.environ.get('LOG') == '1':
    with open('/home/app/api_test.log', 'a') as file:
        file.write(output1.format(r1_score=r1_score, test_status1=test_status1))
        file.write(output2.format(r2_score=r2_score, test_status2=test_status2))
        file.write(output3.format(r3_score=r3_score, test_status3=test_status3))
        file.write(output4.format(r4_score=r4_score, test_status4=test_status4))