import os

def ensure_directories():
    os.makedirs("data/logs", exist_ok=True)
    os.makedirs("data/historical", exist_ok=True)
