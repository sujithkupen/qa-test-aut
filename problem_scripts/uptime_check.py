import requests
import time
from datetime import datetime

APP_URL = "https://www.sujith.dev"  
CHECK_INTERVAL = 0

def check_application_status(url):
    try:
        response = requests.get(url)
        if 200 <= response.status_code < 300:
            return "up"
        else:
            return f"down: {response.status_code})"
    except requests.exceptions.RequestException as e:
        return f"DOWN (Error: {str(e)})"

if __name__ == "__main__":

    while True:
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = check_application_status(APP_URL)
        print(f"{timestamp} : Application Status: {status}")
        time.sleep(CHECK_INTERVAL)  
