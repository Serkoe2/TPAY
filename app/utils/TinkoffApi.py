import requests
import os
from hashlib import sha256

class TinkoffApi:
    url = "https://securepay.tinkoff.ru/v2/"
    TerminalKey = "TinkoffBankTest"
    TerminalPassword = "TinkoffBankTest"
    SiteURL = os.environ.get("NOTIFY_URL") if os.environ.get("NOTIFY_URL") else "http://localhost/order/handle"

    @classmethod
    def init(cls, data):
        __method__ = "Init"
        data["TerminalKey"] =  cls.TerminalKey
        data["NotificationURL"] = cls.SiteURL + "/order/handle"
        data["SuccessURL"] = cls.SiteURL
        r = requests.post(cls.url + __method__, json=data)
        if (r.status_code != 200):
            return False
        return r.json()

    @classmethod
    def getState(cls, order) -> str:
        __method__ = "GetState"
        data = {}
        data["TerminalKey"] =  cls.TerminalKey
        data["PaymentId"] =  order.get("payment_id")
        data["Token"] = cls.getToken(data)
        r = requests.post(cls.url + __method__, json=data)
        if (r.status_code != 200):
            return False
        return r.json()

    @classmethod
    def confirm(cls, order) -> str:
        __method__ = "Confirm"
        data = {}
        data["TerminalKey"] =  cls.TerminalKey
        data["PaymentId"] =  order.get("payment_id")
        data["Token"] = cls.getToken(data)
        r = requests.post(cls.url + __method__, json=data)
        if (r.status_code != 200):
            return False
        return r.json()

    @classmethod
    def refund(cls, order) -> str:
        __method__ = "Cancel"
        data = {}
        data["TerminalKey"] =  cls.TerminalKey
        data["PaymentId"] =  order.get("payment_id")
        data["Token"] = cls.getToken(data)
        r = requests.post(cls.url + __method__, json=data)
        print(r)
        if (r.status_code != 200):
            return False
        return r.json()
    
    @property
    def terminalKey(self):
        return self.TerminalKey

    @classmethod
    def getToken(cls, data) -> str:
        data["Password"] = cls.TerminalPassword
        sort_data = dict(sorted(data.items(), key=lambda x: x[0]))
        str_data = ''.join(map(lambda x: str(x), list(sort_data.values())))
        token = sha256(str_data.encode()).hexdigest()
        return token

    @classmethod
    def compareToken(cls, data) -> bool:
        token = data.pop("Token")
        for i in ["Data","Shops", "Receipt", "DATA"]:
            if i in data:
                data.pop(i)
        data["Success"] = 'true' if data["Success"] else 'false'
        return token == cls.getToken(data)
