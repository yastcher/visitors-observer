import logging

import cv2
import numpy as np
from fastapi import APIRouter, Request, File, UploadFile


logger = logging.getLogger(__name__)

from_apps = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)


@from_apps.post("/check_photo")
async def api_check_photo(request: Request, file: UploadFile = File(...)):
    """
    Test photo for finding faces
    """
    try:
        contents = await file.read()
        img = np.frombuffer(contents, np.uint8)
        photo = cv2.imdecode(img, cv2.IMREAD_UNCHANGED)

        info_message = "Mock"
        status_to_create = 0

        response = {"message": info_message, "data": info_message, "status": status_to_create}
    except Exception as exc:
        logger.warning("Error check photo: %s", str(exc))
        return {
            "message": f"Error check photo: {str(exc)}",
            "status": 1,
        }
    logger.debug("Check photo: %s", str(info_message))
    return response
