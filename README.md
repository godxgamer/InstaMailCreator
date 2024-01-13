# Instagram Account Registration Automation API

This Python script uses an API to automate the registration of Instagram accounts. It sends an OTP to a provided email and then uses the OTP to create a new Instagram account. This can be useful for bulk account creation or automation purposes.

## Prerequisites

Before using this script, make sure you have the following:

- Python installed on your machine
- Necessary dependencies installed (`requests` library)

```bash
pip install requests
```

# Usage
1- Clone the repository:
git clone https://github.com/your-username/instagram-automation-api.git


## API Documentation
# 1. Send OTP to Email
- Endpoint: /api/insta/android/email/send
- Method: POST
- Request Payload:
```bash
{
    "email": "your-email@example.com",
    "proxy": "username:password@host:port",
    "country_code": "IN"
}
```

# 2. Verify OTP and Create Account
- Endpoint: /api/insta/android/email/create
- Method: POST
- Request Payload:
```bash
{
    "otp": "123456",
    "proxy": "username:password@host:port",
    "client_data": {}  // Response from the first API call
}
```

# Contact
- For bulk account creation or any queries, contact the developer on Telegram: @god_x_gamer.

# Disclaimer
- Use this script responsibly and in accordance with Instagram's terms of service. The developer is not responsible for any misuse or consequences.


