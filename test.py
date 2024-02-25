import requests

#Location of an API where the server is running, find this in the VScode terminal
BASE = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "Joe", "views": 1000}, 
        {"likes": 19, "name": "How to make Rest APIS", "views": 10000},
        {"likes": 21, "name": "First API ", "views": 10900},
        {"likes": 15, "name": "Python Demo", "views": 10100}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
print(response.json())



input()
response = requests.get(BASE + "video/6")
print(response.json())