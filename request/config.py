# Имя пользователя для входа
username = 'Test'

# Пароль пользователя для входа
password = 'abcd1234'

# Данные для добавления нового питомца в магазин
new_pet = {
  "id": 185818062023,
  "category": {
    "id": 0,
    "name": "Собакен"
  },
  "name": "Бобр",
  "photoUrls": [
    "None"
  ],
  "tags": [
    {
      "id": 0,
      "name": "Tags"
    }
  ],
  "status": "available"
}

# Данные для обновления питомца
update_pet = {
  "id": 185818062023,
  "category": {
    "id": 0,
    "name": "Собакен"
  },
  "name": "Бобр",
  "photoUrls": [
    "None"
  ],
  "tags": [
    {
      "id": 0,
      "name": "Tags"
    }
  ],
  "status": "sold"
}


# Данные для создания заказа на покупку
order = {
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2023-06-18T18:58:31.704Z",
  "status": "placed",
  "complete": True
}


# Данные для создания пользователей списком
list_users = [
  {
    "id": 111,
    "username": "AAAA",
    "firstName": "BBBB",
    "lastName": "CCCC",
    "email": "cccC@gmal.com",
    "password": "abcd",
    "phone": "+76543875426",
    "userStatus": 0
  },
  {
    "id": 222,
    "username": "HHHH",
    "firstName": "OOOO",
    "lastName": "KKKK",
    "email": "kkkk@gmail.com",
    "password": "koh",
    "phone": "+78521532745",
    "userStatus": 0
  }
]


# Данные для создания нового user
created_user = {
  "id": 0,
  "username": "GGGG",
  "firstName": "CCCC",
  "lastName": "DDDD",
  "email": "dddD@gmail.com",
  "password": "god",
  "phone": "+79839614265",
  "userStatus": 0
}

# Данные для обновления user
updated_user = {
  "id": 0,
  "username": "GGG1",
  "firstName": "CCC1",
  "lastName": "DDD1",
  "email": "ddd@gmail.com",
  "password": "123",
  "phone": "+79839614265",
  "userStatus": 0
}
