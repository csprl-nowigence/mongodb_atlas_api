import os

from dotenv import load_dotenv

load_dotenv()

ATLAS_API_PUBLIC_KEY = os.getenv("ATLAS_API_PUBLIC_KEY")
ATLAS_API_PRIVATE_KEY = os.getenv("ATLAS_API_PRIVATE_KEY")
ATLAS_GROUP_ID = os.getenv("ATLAS_GROUP_ID")
