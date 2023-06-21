import requests
import json
import random
import config
import os
from requests_toolbelt import MultipartEncoder

base_url = 'https://petstore.swagger.io/v2'

"""pet"""

# 1 POST /pet/{petId}/uploadImage  Uploads an image
# petId = 185818062023
# pet_photo = 'C:\Unit.19.3.3\images\pet\image.jpg'
#
#
# def add_pet_photo():
#     data = MultipartEncoder(fields={'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpg')})
#     print(data)
#     headers = {'accept': 'application/json', 'Content-Type': data.content_type}
#
#     print(data)
#     res = requests.post(f'{base_url}/pet/{petId}/uploadImage', headers=headers, data=data)
#
#     print(f'#3\n', res.status_code, res.json())


# 2 POST /pet  Add a new pet to the store
res = requests.post(f'{base_url}/pet',
                    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(config.new_pet))

print(f'#2\n', res.status_code, res.json())

# 3 PUT /pet  Update an existing pet
res = requests.put(f'{base_url}/pet',
                   headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                   data=json.dumps(config.update_pet))
petId = res.json()['id']

print(f'#3\n', res.status_code, res.json())

# 4 GET /pet/findByStatus  Finds Pets by status
status = 'pending'

res = requests.get(f'{base_url}/pet/findByStatus?status={status}',
                   headers={'accept': 'application/json'})

print(f'#4\n', res.status_code, res.json())

# 5 GET /pet/{petId}  Find pet by ID
res = requests.get(f'{base_url}/pet/{petId}',
                   headers={'accept': 'application/json'})

print(f'#5\n', res.status_code, res.json())

# 6 POST /pet/{petId}  Updates a pet in the store with form data
res = requests.post(f'{base_url}/pet/{petId}',
                    headers={'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'},
                    data=json.dumps(config.update_pet))

print(f'#6\n', res.status_code, res.json())

# 7 DELETE /pet/{petId}  Deletes a pet
res = requests.delete(f'{base_url}/pet/{petId}',
                      headers={'accept': 'application/json'})

"""store"""

print(f'#7\n', res.status_code, res.json())

# 8 POST /store/order  Place an order for a pet
res = requests.post(f'{base_url}/store/order',
                    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(config.order))

print(f'#8\n', res.status_code, res.json())

# 9 GET /store/order/{orderId}  Find purchase order by ID (редко статус 200)
orderId = random.randint(1, 10)
res = requests.get(f'{base_url}/store/order/{orderId}',
                   headers={'accept': 'application/json'})

print(f'#9\n', res.status_code, res.json())

# 10 DELETE /store/order/{orderId}  Delete purchase order by ID (редко статус 200)
res = requests.delete(f'{base_url}/store/order/{orderId}',
                      headers={'accept': 'application/json'})

print(f'#10\n', res.status_code, res.json())

# 11 GET /store/inventory  Returns pet inventories by status
res = requests.get(f'{base_url}/store/inventory', headers={'accept': 'application/json'})

print(f'#11\n', res.status_code, res.json())

"""user"""

# 12 POST /user/createWithArray Creates list of users with given input array
res = requests.post(f'{base_url}/user/createWithArray',
                    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(config.list_users))

print(f'#12\n', res.status_code, res.json())

# 13 POST /user/createWithList Creates list of users with given input array
res = requests.post(f'{base_url}/user/createWithList',
                    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(config.list_users))

print(f'#13\n', res.status_code, res.json())

# 14 GET /user/{username} Get user by user name
username = config.list_users[0]['username']

res = requests.get(f'{base_url}/user/{username}', headers={'accept': 'application/json'})

print(f'#14\n', res.status_code, res.json())

# 15 PUT /user/{username} Updated user
# username = list_users[1]['username']
res = requests.put(f'{base_url}/user/{username}',
                   headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                   data=json.dumps(config.updated_user))

print(f'#15\n', res.status_code, res.json())

# 16 DELETE /user/{username} Delete user
res = requests.delete(f'{base_url}/user/{username}', headers={'accept': 'application/json'})

print(f'#16\n', res.status_code, res.json())

# 17 GET /user/login  Logs user into the system
res = requests.get(f'{base_url}/user/login?login={config.username}&password={config.password}',
                   headers={'accept': 'application/json'})

print(f'#17\n', res.status_code, res.json())

# 18 GET /user/logout  Logs out current logged in user session
res = requests.get(f'{base_url}/user/logout', headers={'accept': 'application/json'})

print(f'#18\n', res.status_code, res.json())

# 19 POST /user  Create user
res = requests.post(f'{base_url}/user', headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(config.created_user))

print(f'#19\n', res.status_code, res.json())
