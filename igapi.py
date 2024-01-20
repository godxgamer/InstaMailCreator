import requests

# API headers
headers = {
    "Content-Type": "application/json",
    "X-API-Key": "None",  # Replace with your actual API key
}

# Base URL of the API
base_url = 'http://128.140.99.16:5622'

# Email for Instagram registration
email = 'cekkukofyi@gufum.com'  # Note Always Use least Flagged Domains for email like gmail,outlook,hotmailInstagram Is Very Strict With Email Account Registratin They Block or susspend Account Registered With Temp Mails


# Proxy details for making requests
proxy_path = f'proxy-username:proxy-password@proxy-host:proxy-port'  # Replace with your actual proxy details. username of your paid proxy " : " password of Your proxy " @ " Host of proxy " : " Port of proxy  " example =   smartuser:ERvccvRRTgfd@gate.smartptoxy.com:7777 You Can Also Use Free Proxy Of Any Country " Only Proxy Should Be alive

# Country code for advanced features Of This Api This Will Make Country Info Spoofing To Reduce Bot Detection By Instagram
country_code = 'US'

# Data payload for the API request
data = {
    "email": email,
    "proxy": proxy_path,
    "country_code": country_code
}

#Guys If Want to pass Your Username And Password
# add two parameters data =
"""{
    "full_name":'gamer', 
    "password":'gamerrrrr',
    "email": email,
    "proxy": proxy_path,
    "country_code": country_code
}
"""

# Sending an SMS containing OTP to the provided email
sendsms = requests.post(
    url=f'{base_url}/api/insta/android/email/send',
    json=data,
    headers=headers,
    timeout=200
)

# Checking if 'user_agent' is in the response text
if 'user_agent' in sendsms.text:
    print('OTP sent successfully to your email...')
    otp = str(input("Enter OTP: "))

    # Data for the second API request, including the response from the first API
    data = {
        "otp": otp,
        "proxy": proxy_path,
        "client_data": sendsms.json()
    }

    # Verifying OTP and creating an account using email
    create = requests.post(
        url=f'{base_url}/api/insta/android/email/create',
        json=data,
        headers=headers,
        timeout=200
    ).json()

    print(create)
else:
    print(sendsms.text)

"""
You can use this API in any language (py, php, js, Go, java) to create your own account registration automation.

For bulk account creation or any queries, join @gxbytes for updates and upcoming features. 
If you have any queries about this API, you can contact me on Telegram. My username is '@god_x_gamer'.
"""
