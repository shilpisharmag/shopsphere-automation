import os
from dotenv import load_dotenv
from config.environments import ENVIRONMENTS
from pathlib import Path


# env_file = Path(__file__).resolve().parent.parent /".env"
# print("current working directory", Path.cwd())

# print("Env file direcotry",env_file)

# print("Env file exists:",env_file.exists())
#env_file,override=True
load_dotenv()

# BASE_URL = os.getenv(
#     "BASE_URL",
#     "https://www.saucedemo.com/"
# )

ENV = os.getenv("ENV","qa")
if ENV not in ENVIRONMENTS:
    raise ValueError(f"unknown environment: {ENV}")

config  = ENVIRONMENTS[ENV]
BASE_URL = config["base_url"]
# STANDARD_USERNAME = config["username"] Moving to env
# STANDARD_PASSWORD = config["password"]

STANDARD_USERNAME = os.getenv("STANDARD_USERNAME")
STANDARD_PASSWORD = os.getenv("STANDARD_PASSWORD")
