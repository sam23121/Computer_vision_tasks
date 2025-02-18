# Computer Vision Tasks
This repository contains different implementations for computer vision tasks.

## Contents
- A simple notebook demonstrating image segmentation using Detectron2 
- A simple notebook showing object detection with YOLOv8
- An agentic object detection implementation for detecting peas, onions and mushrooms

## Overview
The first two notebooks focus on image segmentation and object detection using pretrained models. Both notebooks use an apples dataset from Roboflow.com, which is an excellent resource for computer vision tasks.

The third notebook implements an agentic object detection system specifically for identifying peas, onions and mushrooms in images (note: currently does not work for beans, corn, or tomatoes). This provides a more direct approach to the problem.

You can test the implementation:
- Using your own images to evaluate accuracy
- Through the web interface in app.py
- Via the hosted version at https://legumes-differentiator.streamlit.app/ (may take time to load)

## Note
While other object detection and segmentation models were considered, computational resource constraints limited exploration to these three approaches. The code serves as a demonstration of potential approaches rather than a production-ready implementation with complete end-to-end pipeline and coding standards.
