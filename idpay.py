import requests
import json


APIURL = "https://api.idpay.ir/v1.1/"
# You can get your Token from this url => https://idpay.ir/dashboard/web-services
TOKEN = "Your Token Here"
SANDBOX = str(1) # 1 or 0

Headers = {
    "Content-Type": "application/json",
    "X-SANDBOX":SANDBOX,
    "X-API-KEY":TOKEN
}

def Payment(OrderId, Amount, Callback, Name = "", Mail="", Phone = "", Description=""):

    OrderId = str(OrderId)
    Amount = int(Amount)
    Posts = {
        "order_id":OrderId,
        "amount":Amount,
        "callback":Callback,
        "name": Name,
        "mail": Mail,
        "phone": Phone,
        "desc":  Description
    }
    Posts = json.dumps(Posts)
    try:
        Response = requests.post(f"{APIURL}payment",data=Posts,headers=Headers).text
        Response = json.loads(Response)
        Response['id']
    except:
        return False 
    return Response



def Verify(Id,OrderId):

    OrderId = str(OrderId)
    Id = str(Id)
    Posts = {
        "id": Id,
        "order_id": OrderId
    }
    Posts = json.dumps(Posts)
    try:
        Response = requests.post(f"{APIURL}payment/verify",data=Posts,headers=Headers).text
        Response = json.loads(Response)
    except:
        return False
    return Response


def Inquiry(Id,OrderId):

    OrderId = str(OrderId)
    Id = str(Id)
    Posts = {
        "id": Id,
        "order_id": OrderId
    }
    Posts = json.dumps(Posts)
    try:
        Response = requests.post(f"{APIURL}payment/inquiry",data=Posts,headers=Headers).text
        Response = json.loads(Response)
    except:
        return False
    return Response
