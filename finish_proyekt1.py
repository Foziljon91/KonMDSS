
import vk_api;
import requests;
import json;


token='';
data = requests.get(f'https://api.vk.com/method/friends.get?v=5.131&access_token={token}&fields=city,bdate,sex')
answer = data.json();

friend_ids = answer["response"]['items'];

sex = '';
for i in range(answer["response"]['count']):
    if (friend_ids[i]['sex'] == 1):
        sex='Ж';
    else:
        sex='М';
        
    print(i+1,')\t',sex,'\t',friend_ids[i]['first_name'], friend_ids[i]['last_name'] );


