import openai
API_KEY = '' # INPUT YOUR OWN API SECRET KEY HERE

openai.api_key = API_KEY
print(openai.api_key)
user_prompt = input("Write your prompt for image: ")

response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)
