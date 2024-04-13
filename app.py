import requests as re
import json
import pandas as pd







guest_token = input("Enter guest token (from DevTools)")
client_transaction = input("Enter client_transaction (from DevTools)")

headers_xhr = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",    
    "sec-ch-ua": '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Linux",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",        
    "x-twitter-active-user": "yes",
    "x-twitter-client-language": "en",
	"referrer": "https://twitter.com/",
	"x-client-transaction-id": client_transaction,
    "x-guest-token": guest_token,
	"referrerPolicy": "strict-origin-when-cross-origin",		
	"mode": "cors",
	"credentials": "include"
}


def find_all_key_values(data, key):
    results = []
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                results.append(v)
            elif isinstance(v, (dict, list)):
                results.extend(find_all_key_values(v, key))
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                results.extend(find_all_key_values(item, key))
    return results


url = input("Enter API-URL: ")
tweets = re.get(url, headers=headers_xhr)
print(tweets)
print(tweets.status_code)


with open('tweets2.json', 'wb') as f:
	f.write(tweets.content)
	

with open('./tweets2.json') as file:
    data = json.load(file)
    
data = data['data']['user']['result']['timeline_v2']['timeline']['instructions']

key = 'full_text'

values = find_all_key_values(data, key)

df = pd.DataFrame(values)
f_name = input("Enter File name: ")
df.to_csv(f"./{f_name}.csv", index=True)
