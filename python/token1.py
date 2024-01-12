import requests
# response = requests.post('http://192.168.0.7:8075/token/', data={'username': '11608', 'password': '!@12qwaszx'})
# # access_token = response.json()['access']
# print(response.json().get('access'))
# access_token = response.json().get('access')


# headers = {'Authorization': f'Bearer {access_token}'}
# response = requests.post('http://192.168.0.7:8075/a/', headers=headers,data={'username': '11608', 'password': '!@12qwaszx'})
# print(response.json())

requests.get('http://192.168.0.7:8075/b/')
# # # Use JWT access token for API requests
# headers = {'Authorization': f'Bearer {access_token}'}
# response = requests.get('http://192.168.0.7:8075/token/', headers=headers)
# print(response.json())



