# IP Logger

![IP Logger](https://img.shields.io/badge/IP%20Logger-v1.0-blue.svg)

Welcome to the IP Logger repository! This is a simple project that demonstrates how to log the IP addresses of visitors to a website using an `index.html` file. The logged IP addresses are sent to a Discord channel through a webhook.

## 🚀 Features

- Logs IP addresses of visitors
- Sends IP addresses to a Discord channel via webhook
- Simple and easy-to-understand code

## 🛠 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/ip-logger.git
   cd ip-logger
   ```

   **NOTE: DOWNLOAD NGROK AND VERIFY ITS AUTHTOKEN!**
# 2. Set up your Discord Webhook

**Create a new webhook in your Discord server**
**Copy the webhook URL**
**Configure the Webhook URL**

**3. Open the index.html file and replace your actual Discord webhook URL from mine.**

## **📋 Usage**
**Simply host the index.html file on your web server. When someone visits the site, their IP address will be logged and sent to the specified Discord channel via the webhook.**
```
python3 -m http.server 8000
```
```
OPTIONAL
sudo mv /path/to/ngrok /usr/local/bin/
```
```
ngrok http 8000
```

## **📂 Project Structure**
```bash
ip-logger/
│
├── index.html       # The main HTML file for logging IPs
└── README.md        # Project documentation
```
## **🤝 Contributing**
**Contributions, issues, and feature requests are welcome! Feel free to check the issues page.**

## **📧 Contact**
GitHub: itzNamanDev
Discord: naman_cy

Disclaimer: This project is for educational purposes only. Logging IP addresses without consent may be illegal or unethical. Always ensure you have proper permissions before logging any information.
