import os
from dotenv import load_dotenv 

# Load environment variables
load_dotenv()

# Access the keys
openai_api_key = os.getenv("OPENAI_API_KEY")
tivaly_api_key = os.getenv("TIVALY_API_KEY")

# Use the keys
print(f"OpenAI API Key: {openai_api_key}")
print(f"Tivaly API Key: {tivaly_api_key}")
