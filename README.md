# YOLOv9

Implementation of paper - [YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information](https://arxiv.org/abs/2402.13616)

[![arxiv.org](http://img.shields.io/badge/cs.CV-arXiv%3A2402.13616-B31B1B.svg)](https://arxiv.org/abs/2402.13616)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/kadirnar/Yolov9)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/merve/yolov9)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov9-object-detection-on-custom-dataset.ipynb)
[![OpenCV](https://img.shields.io/badge/OpenCV-BlogPost-black?logo=opencv&labelColor=blue&color=black)](https://learnopencv.com/yolov9-advancing-the-yolo-legacy/)

<div align="center">
    <a href="./">
        <img src="./figure/performance.png" width="79%"/>
    </a>
</div>


## Performance 

MS COCO

| Model | Test Size | AP<sup>val</sup> | AP<sub>50</sub><sup>val</sup> | AP<sub>75</sub><sup>val</sup> | Param. | FLOPs |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: |
| [**YOLOv9-T**]() | 640 | **38.3%** | **53.1%** | **41.3%** | **2.0M** | **7.7G** |
| [**YOLOv9-S**]() | 640 | **46.8%** | **63.4%** | **50.7%** | **7.1M** | **26.4G** |
| [**YOLOv9-M**]() | 640 | **51.4%** | **68.1%** | **56.1%** | **20.0M** | **76.3G** |
| [**YOLOv9-C**](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c-converted.pt) | 640 | **53.0%** | **70.2%** | **57.8%** | **25.3M** | **102.1G** |
| [**YOLOv9-E**](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-e-converted.pt) | 640 | **55.6%** | **72.8%** | **60.6%** | **57.3M** | **189.0G** |
<!-- | [**YOLOv9 (ReLU)**]() | 640 | **51.9%** | **69.1%** | **56.5%** | **25.3M** | **102.1G** | -->

<!-- tiny, small, and medium models will be released after the paper be accepted and published. -->


# Docker Setup for Model Training

This guide provides instructions on how to build and run a Docker container for model training purposes. This setup encapsulates the training environment, ensuring consistency across different machines.

## Prerequisites

Ensure you have Docker and Docker Compose installed on your machine. These tools are required to build and manage the containers. For installation instructions, please visit:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

### Build the Docker Image
Tested on Ubuntu 20.04
Use the following command to build the Docker image and run it. This process may take a few minutes as it sets up the environment and dependencies:

```bash
sudo docker-compose up --build
```
This command executes the Docker Compose file, docker-compose.yml, which should be configured to build the Docker image based on the provided Dockerfile and run the container.
### Accessing the Docker Container

Once the container is running, you can access its bash shell to interact with the training environment directly:
```bash
sudo docker exec -it [docker_image_name] bash
```
Replace [docker_image_name] with the actual name of your Docker image. You can find the image name by running docker images if you are unsure of the name.

Using the Container

Inside the container, you can execute commands and scripts to start training models or perform any required tasks. The environment is isolated, which helps in maintaining consistency regardless of the underlying host system.


## Model Training Setup with Docker container

This guide provides detailed instructions on setting up Docker for model training, modifying model parameters through a configuration file, and managing dataset specifications for successful training.

## Configuration and Dataset

### Configuring the Model

The model's parameters can be adjusted by editing the `config.yaml` file. This file contains various settings that can be customized to fit specific training needs, including learning rates, batch sizes, and other model-specific parameters. It's essential to review and modify this file to ensure the model trains correctly according to your requirements.

### Preparing the Data

Data for training is located in the `data/fashion` directory. The dataset's details and format are described in the `data.yaml` file. Notably, due to a current limitation with the YOLO model format, you must include a placeholder class (`NA`) as the first class in your dataset. This is because YOLO indexes classes from `0` to `nc-1`, and the absence of any images for the first class (`0`) is presently treated as a bug.

This workaround is temporary, and a planned future update to the `cocotoyolo.py` script will resolve this issue by adjusting how classes are handled.

## Training the Model

To start training the model with the specified configurations and prepared data, run the following command from the root directory of your project:

```bash
python segment/train_with_config.py
```


