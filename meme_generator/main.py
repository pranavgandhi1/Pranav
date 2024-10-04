import requests

# Function to get meme templates from Imgflip API
def get_meme_templates():
    url = "https://api.imgflip.com/get_memes"
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the JSON response to get meme templates
        memes = response.json()['data']['memes']
        print(f"Found {len(memes)} meme templates!")
        for meme in memes[:5]:  # Show top 5 memes
            print(f"Name: {meme['name']}, ID: {meme['id']}, URL: {meme['url']}")
        return memes
    else:
        print("Failed to retrieve memes from Imgflip API.")
        return None

# Function to generate a custom meme using Imgflip API
def generate_meme(template_id, top_text, bottom_text, username, password):
    url = "https://api.imgflip.com/caption_image"
    params = {
        "template_id": template_id,
        "username": username,
        "password": password,
        "text0": top_text,
        "text1": bottom_text
    }

    response = requests.post(url, params=params)
    if response.status_code == 200:
        result = response.json()
        if result['success']:
            print(f"Generated Meme URL: {result['data']['url']}")
            return result['data']['url']
        else:
            print(f"Failed to create meme: {result['error_message']}")
    else:
        print("Failed to connect to Imgflip API.")
    return None

# Main function to test the program
if __name__ == "__main__":
    # Step 1: Get meme templates
    templates = get_meme_templates()

    # Step 2: Use the first template for generating a meme
    if templates:
        username = input("Enter your Imgflip username: ")
        password = input("Enter your Imgflip password: ")
        
        # Choose the first template from the list
        template_id = templates[0]['id']
        top_text = input("Enter top text for the meme: ")
        bottom_text = input("Enter bottom text for the meme: ")

        # Step 3: Generate meme
        meme_url = generate_meme(template_id, top_text, bottom_text, username, password)
        print(f"Your generated meme is available here: {meme_url}")
