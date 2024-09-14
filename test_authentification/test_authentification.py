import os
import requests
import time 

# définition de l'adresse de l'API
api_address = 'fastapi'
# port de l'API
api_port = 8000
time.sleep(10)
# requête
r1 = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland'
    }
)

r2 = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'builder'
    }
)

r3 = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'clementine'
    }
)

status_code1 = r1.status_code
status_code2 = r2.status_code
status_code3 = r3.status_code
output1 = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="alice"
| password="wonderland"

expected result = 200
actual restult = {status_code1}

==>  {test_status1}

'''

output2 = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="bob"
| password="builder"

expected result = 200
actual restult = {status_code2}

==>  {test_status2}

'''

output3 = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="alice"
| password="clementine"

expected result = 403
actual restult = {status_code3}

==>  {test_status3}

'''




# affichage des résultats
if status_code1 == 200:
    test_status1 = 'SUCCESS'
else:
    test_status1 = 'FAILURE'

if status_code2 == 200:
    test_status2 = 'SUCCESS'
else:
    test_status2 = 'FAILURE'

if status_code3 == 403:
    test_status3 = 'SUCCESS'
else:
    test_status3 = 'FAILURE'


# impression dans un fichier
if os.environ.get('LOG') == '1':
    with open('/home/app/api_test.log', 'a') as file:
        file.write(output1.format(status_code1=status_code1, test_status1=test_status1))
        file.write(output2.format(status_code2=status_code2, test_status2=test_status2))
        file.write(output3.format(status_code3=status_code3, test_status3=test_status3))
