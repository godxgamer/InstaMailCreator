# Instagram Account Registration Automation API

- This Python script uses an API built on Instagram Android API version 312.1.0.34.11 and is based on Block Response reverse engineering to automate the registration of Instagram accounts. It sends an OTP to a provided email and then uses the OTP to create a new Instagram account. This can be useful for bulk account creation or automation purposes.
- ## Free Api 


## Prerequisites

Before using this script, make sure you have the following:

- Python installed on your machine
- Necessary dependencies installed (`requests` library)

```bash
pip install requests
```

# Usage
1- Clone the repository:
git clone https://github.com/godxgamer/InstaMailCreator.git


## API Documentation
# 1. Send OTP to Email
- Endpoint: /api/insta/android/email/send
- Method: POST
- Request Payload:
```bash
headers={
    "Content-Type": "application/json",
    "X-API-Key":"None",
}

{
    "email": "your-email@example.com",
    "proxy": "username:password@host:port",
    "country_code": "IN"
}
```
- cURL Example:
```bash
curl -X POST \
  http://128.140.99.16:5622/api/insta/android/email/send \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: Your-API-Key' \
  -d '{
    "email": "your-email@example.com",
    "proxy": "username:password@host:port",
    "country_code": "IN"
  }'
```

# 2. Verify OTP and Create Account
- Endpoint: /api/insta/android/email/create
- Method: POST
- Request Payload:
```bash
headers={
    "Content-Type": "application/json",
    "X-API-Key":"None",
}

{
    "otp": "123456",
    "proxy": "username:password@host:port",
    "client_data": {}  // Response from the first API call
}
```
- cURL Example:
```bash
curl -X POST \
  http://128.140.99.16:5622/api/insta/android/email/create \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: Your-API-Key' \
  -d '{
    "otp": "123456",
    "proxy": "username:password@host:port",
    "client_data": {}
  }'
```

# Contact
- For bulk account creation or any queries, contact the developer on Telegram: [@god_x_gamer](https://telegram.me/god_x_gamer).
- Join [@gxbytes](https://telegram.me/gxbytes) for latest updates 

# Disclaimer
- Use this script responsibly and in accordance with Instagram's terms of service. The developer is not responsible for any misuse or consequences.

  ## Hashtags

# Instagram #Automation #Python #API #InstagramAPI #AccountCreation #InstagramAutomation #Developer #Coding #Programming #OpenSource #WebDev #Tech #GitHub #CodingCommunity #Bot #Scraping #ReverseEngineering #PythonBot #InstaBot #RequestsLibrary #InstagramBot #AccountCreationBot #AutomaticAccountCreation #CreateInstagramAccount #MakeAccount #MultipleAccounts #PythonAutomation #InstagramRequest #InstagramAPIAutomation #PythonDevelopment #HTTPAutomation #AndroidAutomation #CodingCommunity #InstagramDevelopment #IGDev #Instagram #InstagramScraper #InstagramAPI #Insta #InstagramDownloader #InstagramPrivateAPI #CreateInstagramAccount #InstaBot #InstagramAccountCreator #InstaReger #InstagramRegistration #InstaCreate #InstaRegerAPI #InstagramGenerator #InstagramSignUp #InstagramSignUpAPI #InstagramBusinessAccount #InstagramPython #InstagramBulkAccount #CodingCommunity
