import requests

headers={
    "Content-Type": "application/json",
}

proc = str(input("Enter Your Proxy -> "))  # "username:password@host:port"  (without http:// or https:// )
num = str(input("Enter Your Number -> "))  #919988998877

def creator():
    data={
        "api-key":"gamer",
        "number": num,
        "proxy":proc
    }

    r=requests.post("http://128.140.99.16:6969/api/send-sms",json=data,headers=headers,timeout=100)
    if "securetoken" in r.text:
        print(r.text)
        r=r.json()
        securetoken=r['message']['securetoken']
        otp=str(input("otp : "))
        data={
        "api-key":"gamer",
        "securetoken": securetoken,
        "proxy":proc,
        "otp":otp
        }

        r=requests.post("http://128.140.99.16:6969/api/create-acc",json=data,headers=headers,timeout=100)
        print(r.text)

    elif "IndexError" in r.text:
        print("indexerror restarting")
        creator()

    elif "ReadTimeout" in r.text:
        print("ReadTimeout restarting")
        creator()
    else:
        print(r.text)

creator()
