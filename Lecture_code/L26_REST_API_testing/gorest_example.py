import requests

# url = 'https://gorest.co.in/public/v2/users'
# header_with_authorization = {"Accept": "application/json",
#                              "Content-Type": "application/json",
#                              "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"}
#
# response = requests.get(url, headers=header_with_authorization)
# print(response)
# print(response.status_code)
# print(response.json())
# print(response.json()[0]['id'])
# print(response.text)
# print(response.content)
# print(response.cookies)

# url = 'https://account.104.ua/ua'
# response = requests.get(url)
# print(response)
# print(response.status_code)
# #print(response.json())
# #print(response.text)
# #print(response.conten



# url = 'https://gorest.co.in/public/v2/users?page=3&per_page=20'
# header_with_authorization = {"Accept": "application/json",
#                              "Content-Type": "application/json",
#                              "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"}
#
# response = requests.get(url, headers=header_with_authorization)
# print(response)
# print(response.status_code)
# print(response.json())
# print(response.headers)
# print(len(response.json()))


# url = 'https://gorest.co.in/public/v2/users/217414'
# header_with_authorization = {"Accept": "application/json",
#                              "Content-Type": "application/json",
#                              "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"}
#
# response = requests.get(url, headers=header_with_authorization)
# print(response)
# print(response.status_code)
# print(response.json())
# print(response.headers)
# print(len(response.json()))


# url = 'https://gorest.co.in/public/v2/users?id=217414&gender=female'
# header_with_authorization = {"Accept": "application/json",
#                              "Content-Type": "application/json",
#                              "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"}
#
# response = requests.get(url, headers=header_with_authorization)
# print(response)
# print(response.status_code)
# print(response.json())
# print(response.headers)
# print(len(response.json()))


# url = 'https://gorest.co.in/public/v2/users.xml?id=217414&gender=female'
# header_with_authorization = {"Accept": "application/json",
#                              "Content-Type": "application/json",
#                              "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"}
#
# response = requests.get(url, headers=header_with_authorization)
# print(response)
# print(response.status_code)
# print(response.text)
# print(response.headers)



# url = 'https://gorest.co.in/public/v2/users.xml?id=217414&gender=female'
# header_with_authorization = {"Accept": "application/json",
#                              "Content-Type": "application/json",
#                              "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"}
#
#
# user_data = {"name": "Anna Ivanova", "gender": "female", "email": "anna.ivanova@test.com", "status": "active"}
#

# response = requests.post(url, json=user_data, headers=header_with_authorization)
# print(response)
# print(response.status_code)
# print(response.text)
# print(response.headers)

# url = 'https://gorest.co.in/public/v2/users?email=anna.ivanova@test.com'
# response = requests.get(url, headers=header_with_authorization)
# print(response)
# print(response.status_code)
# print(response.text)
# print(response.headers)
#
# url = 'https://gorest.co.in/public/v2/users/218345'
# response = requests.patch(url, json={'name': 'Oksana Volkova'}, headers=header_with_authorization)
# print(response)
# print(response.status_code)
# print(response.text)
# print(response.headers)
#
# url = 'https://gorest.co.in/public/v2/users?email=anna.ivanova@test.com'
# response = requests.get(url, headers=header_with_authorization)
# print(response)
# print(response.status_code)
# print(response.text)
# print(response.headers)

# url = 'https://gorest.co.in/public/v2/users/218345'
# response = requests.delete(url, headers=header_with_authorization)
# print(response)
# print(response.status_code)
# print(response.text)
# print(response.headers)
#
# url = 'https://gorest.co.in/public/v2/users?email=anna.ivanova@test.com'
# response = requests.get(url, headers=header_with_authorization)
# print(response)
# print(response.status_code)
# print(response.text)
# print(response.headers)

# response = requests.post(url, json=user_data, headers=header_with_authorization)
# print(response)
# print(response.status_code)
# print(response.text)
# print(response.headers)
#
# response = requests.post(url, json=user_data, headers=header_with_authorization)
# print(response)
# print(response.status_code)
# print(response.text)
# print(response.headers)


# header_for_options = {"Accept": "application/json",
#                              "Content-Type": "application/json",
#                              "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c",
#                       'Origin': 'https://gorest.co.in'}
#
#
# url = 'https://gorest.co.in/public/v2/users'
# response = requests.options(url, headers=header_for_options)
# print(response)
# print(response.status_code)
# print(response.text)
# print(response.headers)
