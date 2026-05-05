import sys, platform
print('Python:', sys.version)
print('Platform:', platform.platform())
try:
 import onnxruntime as ort; print('ONNX Runtime providers:', ort.get_available_providers())
except Exception as e: print('ONNX Runtime check failed:', e)
try:
 import tensorrt as trt; print('TensorRT:', trt.__version__)
except Exception as e: print('TensorRT check failed:', e)
