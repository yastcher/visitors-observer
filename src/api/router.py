import logging
from io import BytesIO

import cv2
import numpy as np
from fastapi import APIRouter, File, Request, UploadFile

from src.config import settings
from src.cv.face_detector import mtcnn
from src.tbot.command import bot

logger = logging.getLogger(__name__)

from_apps = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)


@from_apps.post("/check_photo")
async def api_check_photo(request: Request, file: UploadFile = File(...)):  # noqa: B008
    """
    Test photo for finding faces
    """
    if file.content_type not in ("image/jpeg", "image/png", "image/webp"):
        return {"message": "Unsupported file type", "status": 1}

    try:
        MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
        contents = await file.read(MAX_FILE_SIZE + 1)
        if len(contents) > MAX_FILE_SIZE:
            return {"message": "File too large (max 10MB)", "status": 1}
        if contents is None:
            raise Exception("UploadFileException = contents is None")
        img = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(img, cv2.IMREAD_UNCHANGED)
        im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        boxes, _probs, _landmarks_all = mtcnn.detect(im_rgb, landmarks=True)
        if boxes is None:
            raise Exception("faces not found")

        info_message = f"{len(boxes)} faces founded"
        status_to_create = 0

        photo_file = BytesIO(contents)
        await bot.send_photo(chat_id=settings.chat_id, photo=photo_file)

        response = {"message": info_message, "data": info_message, "status": status_to_create}
    except Exception as exc:
        logger.warning("Error check photo: %s", str(exc))
        return {
            "message": "Error processing photo",
            "status": 1,
        }
    logger.debug("Check photo: %s", str(info_message))
    return response
