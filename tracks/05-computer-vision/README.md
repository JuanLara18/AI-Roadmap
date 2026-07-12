# Computer Vision

> Teaching machines to see — from image classification to multimodal visual understanding.

**Prerequisites:** [Deep Learning](../03-deep-learning/README.md) — especially CNNs and the transformer architecture.

---

## Core Concepts

### Image Classification

The foundational CV task — identifying what's in an image.

| Approach | Description |
|---|---|
| CNNs (ResNet, EfficientNet, ConvNeXt) | Classic deep learning approach, still strong |
| Vision Transformers (ViT) | Applying transformer architecture to images |
| Transfer Learning | Using pretrained models on custom datasets |
| Data Augmentation | Random crops, flips, color jitter, Mixup, CutMix |
| Knowledge Distillation | Training small models to mimic large ones |

### Object Detection

Locating and classifying multiple objects in an image.

| Model | Approach |
|---|---|
| **YOLO (v8, v9, v10, v11)** | Real-time single-shot detection |
| **RT-DETR** | Transformer-based real-time detection |
| **Faster R-CNN** | Two-stage detection, high accuracy |
| **DINO / Grounding DINO** | Open-vocabulary detection with language |
| **Florence-2** | Unified vision-language model for detection |

### Segmentation

Pixel-level understanding of images.

| Type | Description | Key Models |
|---|---|---|
| Semantic Segmentation | Label every pixel by class | DeepLab, SegFormer |
| Instance Segmentation | Separate individual objects | Mask R-CNN, YOLACT |
| Panoptic Segmentation | Combine semantic + instance | Panoptic FPN |
| **Segment Anything (SAM / SAM 2)** | Foundation model for universal segmentation | Zero-shot, promptable |

### Video Understanding

Extending vision to temporal data.

| Task | Description |
|---|---|
| Action Recognition | Classifying activities in video |
| Object Tracking | Following objects across frames |
| Video Transformers | TimeSformer, VideoMAE |
| Optical Flow | Estimating motion between frames |

### Vision-Language Models

Bridging vision and language — the frontier of multimodal AI.

| Model | Capability |
|---|---|
| **CLIP** | Zero-shot image classification via text |
| **LLaVA / LLaVA-Next** | Open-source visual question answering, image reasoning |
| **GPT-4o / o1** | Frontier multimodal understanding and complex reasoning |
| **Claude 3.5 Sonnet** | Advanced image reasoning, document analysis, and visual coding |
| **Gemini 1.5 Pro / 2.0 Flash** | Native multimodal with long-context video and image processing |
| **Llama 3.2 Vision** | Open-source multimodal model with native image understanding |
| **Florence-2** | Microsoft's unified visual understanding model (VLM) for object detection, segmentation |
| **PaliGemma / PaliGemma 2** | Google's open vision-language model for transfer learning |

---

## Recommended Resources

### Courses
- [Stanford CS231n — CNNs for Visual Recognition](http://cs231n.stanford.edu/) (free)
- [Michigan EECS 498 — Deep Learning for Computer Vision](https://web.eecs.umich.edu/~justlnch/eecs498/) (free)
- [Hugging Face Computer Vision Course](https://huggingface.co/learn/computer-vision-course) (free)

### Books
- *Computer Vision: Algorithms and Applications* — Richard Szeliski ([free online](https://szeliski.org/Book/))
- *Deep Learning for Vision Systems* — Mohamed Elgendy
- *Programming Computer Vision with Python* — Jan Erik Solem

### Key Papers
- [ResNet — Deep Residual Learning](https://arxiv.org/abs/1512.03385)
- [Vision Transformer (ViT)](https://arxiv.org/abs/2010.11929)
- [YOLO — You Only Look Once](https://arxiv.org/abs/1506.02640)
- [CLIP](https://arxiv.org/abs/2103.00020) — Learning visual concepts from language
- [Segment Anything (SAM)](https://arxiv.org/abs/2304.02643)

### Key Libraries
- [OpenCV](https://opencv.org/) — classic computer vision
- [torchvision](https://pytorch.org/vision/) — PyTorch vision utilities
- [Ultralytics](https://github.com/ultralytics/ultralytics) — YOLO family
- [Detectron2](https://github.com/facebookresearch/detectron2) — Meta's detection framework
- [Albumentations](https://albumentations.ai/) — fast image augmentations
- [Roboflow](https://roboflow.com/) — dataset management and annotation

---

## Project Ideas

| Project | Difficulty | Description |
|---|---|---|
| **Image Classification System** | Beginner | Train a CNN or ViT to classify images with transfer learning |
| **Real-Time Face Recognition** | Intermediate | Detect and recognize faces using OpenCV and deep learning |
| **Object Detection on Custom Data** | Intermediate | Train YOLO on your own annotated dataset |
| **Visual Search Engine** | Advanced | Build image similarity search with CLIP embeddings |
| **Video Action Recognition** | Advanced | Classify actions in video using video transformers |
| **Zero-Shot Classifier** | Intermediate | Use CLIP for classifying images without training data |

---

## What's Next?

Explore **[Generative AI](../06-generative-ai/README.md)** for image generation, or **[MLOps](../08-mlops-production/README.md)** to deploy your vision models.

[Back to Roadmap](../../README.md)
