import requests
import json

url = "https://api.qingyunke.com/api.php?key=free&appid=0&msg="
t = True

while t:
    inp = input("User：")
    if inp == "quit" or inp == "再见":
        t = False
    else:
        rep = requests.get(url+inp)
        rep = json.loads(rep.text)
        rep = rep["content"]
        print(rep)