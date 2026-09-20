from comfy_sdk import Comfy
from dotenv import load_dotenv

load_dotenv(verbose=True)

client = Comfy(api_key=None)

print(client)