import torch
import cv2
from matplotlib import pyplot as plt

# Load YOLOv5 model (replace path if using custom weights)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt' ,force_reload= True)  # Your model path
