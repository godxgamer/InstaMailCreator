import requests

headers={
    "Content-Type": "application/json",
    "X-API-Key":"None",
}

baseurl='http://128.140.99.16:5622' # Base Url Of Api


emal='cekkukofyi@gufum.com'  # Note Always Use least Flagged Domains for email like gmail,outlook,hotmail
#Instagram Is Very Strict With Email Account Registratin They Block or susspend Account Registered With Temp Mails

proxy_path='username:password@host:port' # username of your paid proxy " : " password of Your proxy " @ " Host of proxy " : " Port of proxy  " example =   smartuser:ERvccvRRTgfd@gate.smartptoxy.com:7777
# You Ca Also Use Free Proxy Of Any Country " Only Proxy Should Be alive

country_Code='IN' # "India"   This Is A Advance Feature Of This Api This Will Make Country Info Spoofing To Reduce Bot Detection By Instagram
" Example If You Are Using Indian Proxy Location Then Country Code should be IN"


data={
    "email":emal,
    "proxy":proxy_path,
    "country_code":country_Code
}

sendsms=requests.post(url=f'{baseurl}/api/insta/android/email/send',json=data,headers=headers,timeout=200)  # This Request Will Send An Sms containig otp To Yor email
if 'user_agent' in sendsms.text: # an if else condition To check the given keyword is in response or not
    print('otp sent ')  # Otp sent sucessfull To your email.......
    otp=str(input("enter otp "))
    data={
        "otp":otp,
        "proxy":proxy_path,
        "client_data":sendsms.json(), #  This will take response from first api ("sendsms")  and pass into the next api  .
    }
    create=requests.post(url=f'{baseurl}/api/insta/android/email/create',json=data,headers=headers,timeout=200).json()  # At Last Create Api .This Will Take otp,proxy and sendsms data to verify and create account using email
    print(create)

else:
    print(sendsms.text)  # in case otp not sent sucessfull



"""

You Can Use This Api According To You In Any Language (py,php,js,Go,java) and Make Your Own Automation Of account registragtion


Contact For Bulk Account Creation 
Join @gxbytes For updates and new upcoming freatures like ( Post Upload api, Get followers and following list api ,follow api , like api, ............. and all features of instagram of api ) 
If You Have Any query About This Api You Can Contact me on telegram . my username = '@god_x_gamer'
"""
