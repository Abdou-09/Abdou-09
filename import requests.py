import requests
import socket
def backup_webpage():
    # Step 1: Ask the user for the full URL of the webpage
    url = input("Please enter the full URL of the webpage: ")
    
    try:
        # Step 2: Send an HTTP GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            print(f"Successfully fetched the webpage: {url}")
            
            # Step 3: Create a filename based on the URL (or use a static filename)
            filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
            
            # Step 4: Write the content to a file
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"Webpage saved successfully as '{filename}'")
        else:
            print(f"Failed to fetch the webpage. HTTP Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to fetch the webpage: {e}")

# Call the function
backup_webpage()
