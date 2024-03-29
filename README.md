# Instagram Account Registration Automation API

- This Python script uses an API built on Instagram Android API version 312.1.0.34.11 and is based on Block Response reverse engineering to automate the registration of Instagram accounts. It sends an OTP to a provided email and then uses the OTP to create a new Instagram account. This can be useful for bulk account creation or automation purposes.
### - Free Api Key
```bash 
dh6345sdsh3sdr8s98fd8
```


### Youtube Tutorial For beginner

- https://youtu.be/FexzCl-3rds


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

### Update :- 
- You can now pass your own full_name and password.
- Its optional if you want to pass your full name and password add to parameters in send otp payload
- if You Dont Want to pass these . Just Remove "full_name" and "password" From payload parameters 
```bash
{
    "full_name":'gamer',  # Optional 
    "password":'gamerrrrr',# Optional 
    "email": email,
    "proxy": proxy_path,
    "country_code": country_code
}
```


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


