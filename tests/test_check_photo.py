from io import BytesIO
from unittest.mock import AsyncMock, patch

import cv2
import numpy as np


def _make_test_jpeg() -> BytesIO:
    """Minimal valid JPEG for tests."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    _, buf = cv2.imencode(".jpg", img)
    return BytesIO(buf.tobytes())


def test_check_photo_no_faces(client):
    """Photo without faces -> status 1, no detail leak."""
    with patch("api.router.mtcnn") as mock_mtcnn, patch("api.router.bot"):
        mock_mtcnn.detect.return_value = (None, None, None)

        response = client.post(
            "/api/check_photo",
            files={"file": ("test.jpg", _make_test_jpeg(), "image/jpeg")},
        )

    data = response.json()
    assert response.status_code == 200
    assert data["status"] == 1
    # No internal error details should leak
    assert "faces not found" not in data["message"]


def test_check_photo_with_faces(client):
    """Photo with face -> status 0, bot called."""
    with patch("api.router.mtcnn") as mock_mtcnn, patch("api.router.bot") as mock_bot:
        mock_mtcnn.detect.return_value = (
            np.array([[10, 10, 50, 50]]),
            np.array([0.99]),
            np.array([[[20, 20, 30, 30, 25]]]),
        )
        mock_bot.send_photo = AsyncMock()

        response = client.post(
            "/api/check_photo",
            files={"file": ("test.jpg", _make_test_jpeg(), "image/jpeg")},
        )

    data = response.json()
    assert response.status_code == 200
    assert data["status"] == 0
    assert "1 faces" in data["message"]
    mock_bot.send_photo.assert_called_once()


def test_check_photo_invalid_content_type(client):
    """Non-image file -> rejection."""
    response = client.post(
        "/api/check_photo",
        files={"file": ("test.txt", BytesIO(b"not an image"), "text/plain")},
    )
    data = response.json()
    assert data["status"] == 1
    assert "Unsupported" in data["message"]


def test_check_photo_too_large(client):
    """File > 10 MB -> rejection."""
    big = BytesIO(b"x" * (10 * 1024 * 1024 + 100))
    response = client.post(
        "/api/check_photo",
        files={"file": ("big.jpg", big, "image/jpeg")},
    )
    data = response.json()
    assert data["status"] == 1
    assert "large" in data["message"].lower()
