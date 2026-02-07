import os
import sys
from unittest.mock import MagicMock

# Set test env BEFORE any app imports
os.environ.setdefault("TELEGRAM_BOT_TOKEN", "test-token")
os.environ.setdefault("CHAT_ID", "123456")
os.environ.setdefault("INFERENCE_DEVICE", "cpu")

# Mock heavy ML dependencies BEFORE they get imported
sys.modules["torch"] = MagicMock()
sys.modules["torchvision"] = MagicMock()
sys.modules["facenet_pytorch"] = MagicMock()

pytest_plugins = [
    "tests.fixtures",
]
