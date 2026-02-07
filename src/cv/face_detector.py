from facenet_pytorch import MTCNN

from src.config import settings

mtcnn = MTCNN(keep_all=True, device=settings.inference_device)
