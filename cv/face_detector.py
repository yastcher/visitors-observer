from facenet_pytorch import MTCNN

import config

mtcnn = MTCNN(keep_all=True, device=config.INFERENCE_DEVICE)
