# Use an appropriate base image with Python and OpenCV support
# Use an NVIDIA PyTorch image compatible with CUDA and cuDNN
FROM nvcr.io/nvidia/pytorch:21.11-py3

# Update and upgrade packages
RUN apt-get update && apt-get upgrade -y

# Install necessary system packages
RUN apt-get update && apt-get install -y \
    zip \
    htop \
    screen \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip3 install --upgrade pip && \
    pip3 install numpy pandas seaborn thop

# Set the default working directory
WORKDIR /app

# Allow the container to access the X11 display and set DISPLAY environment variable
ENV DISPLAY=:0
#export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/qt5/plugins/platforms
RUN export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/qt5/plugins/platforms
# Copy your course files to the working directory if needed
# COPY . /app

# Allow the container to access the webcam (add the "--device" flag)
# You may need to use "--privileged" mode or grant specific permissions
# depending on your host environment and security settings
#CMD ["python", "-c", "import cv2; print(cv2.VideoCapture(0).isOpened())"]
CMD while true; do echo "Hello, world!"; sleep 1; done
#CMD ["python", "/app/helmet/inference.py"]
