import requests
import json

API_URL = "https://api.idpay.ir/v1.1/"
# You can get your Token from this url => https://idpay.ir/dashboard/web-services
TOKEN = "Your Token Here"
SANDBOX = str(1)  # 1 or 0

header = {
    "Content-Type": "application/json",
    "X-SANDBOX": SANDBOX,
    "X-API-KEY": TOKEN
}


def payment(order_id, amount, callback, name="", mail="", phone="", description=""):
    posts = {
        "order_id": str(order_id),
        "amount": int(amount),
        "callback": callback,
        "name": name,
        "mail": mail,
        "phone": phone,
        "desc": description
    }
    posts = json.dumps(posts)
    try:
        response = requests.post(f"{API_URL}payment", data=posts, headers=header).text
        response = json.loads(response)
    except Exception as e:
        return False
    return response


def verify(id, order_id):
    order_id = str(order_id)
    id = str(id)
    posts = {
        "id": id,
        "order_id": order_id
    }
    posts = json.dumps(posts)
    try:
        response = requests.post(f"{API_URL}payment/verify", data=posts, headers=header).text
        response = json.loads(response)
    except Exception as e:
        return False
    return response


def inquiry(id, order_id):
    posts = {
        "id": str(id),
        "order_id": str(order_id)
    }
    posts_json = json.dumps(posts)
    try:
        response = requests.post(f"{API_URL}payment/inquiry", data=posts_json, headers=header).text
        response = json.loads(response)
    except Exception as e:
        return False
    return response
