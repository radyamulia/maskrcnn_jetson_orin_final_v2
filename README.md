# Mask R-CNN + MobileNetV3-FPN for Pothole Detection on Jetson Orin Nano

This final package contains an end-to-end pipeline for:

1. Training Mask R-CNN + MobileNetV3-FPN on a laptop/PC.
2. Evaluating test-set metrics and COCO mAP.
3. Profiling model size, latency, and FPS.
4. Exporting the trained PyTorch model to ONNX.
5. Validating ONNX Runtime inference.
6. Preparing Jetson Orin Nano deployment files.
7. Creating TensorRT FP16 conversion scripts.
8. Running ONNX vs TensorRT benchmark.
9. Generating a final deployment report.

## Main files

```text
configs/config_maskrcnn_mobilenetv3_fpn.yaml
notebooks/maskrcnn_mobilenetv3_fpn_jetson_orin_end_to_end_v2.ipynb
docs/Manual_Book_MaskRCNN_Jetson_Orin_Nano_End_to_End_v2.pdf
```

## Dataset structure

```text
data/images/train/
data/images/val/
data/images/test/
data/annotations/train.json
data/annotations/val.json
data/annotations/test.json
data/videos/pothole_test.mp4
```

## Run on laptop

```bash
conda create -n pothole_maskrcnn python=3.10 -y
conda activate pothole_maskrcnn
pip install -r requirements.txt
jupyter notebook
```

Open:

```text
notebooks/maskrcnn_mobilenetv3_fpn_jetson_orin_end_to_end_v2.ipynb
```

## Jetson Orin Nano note

TensorRT engine files must be built directly on Jetson Orin Nano, not on the laptop.
