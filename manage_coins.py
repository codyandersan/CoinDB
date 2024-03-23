import json
import requests

url = "https://coindb-30ac.restdb.io/rest/coins"

headers = {
    'content-type': "application/json",
    'x-apikey': "0185c745f02eea6f0d0aee3126e3d6085911d",
    'cache-control': "no-cache"
    }

def get_coins():
    response = requests.request("GET", url, headers=headers)

    return response.json()   


def add_coin(title, dateOfMinting="", remarks="", ):
    
    payload = json.dumps( {
        "title": title,
        "dateOfMinting": dateOfMinting,
        "remarks": remarks,
    } )

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.json()

def delete_coin(objectId):

    objectUrl = f"{url}/{objectId}"

    response = requests.request("DELETE", objectUrl, headers=headers)

    return response.json()


if __name__ == "__main__":
    # a = add_coin("Azadi", "sc.png", "2023", "Yo bro")
    # print(a)
    # print(get_coins())
    print(delete_coin("65fe970c89a2764b000265cf"))

