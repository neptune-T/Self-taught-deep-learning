## Self-taught deep learning, train models and understand the underlying mathematics



## 学习资源

- 视频课程：[**stanford cs229  -  andrew ng**](https://www.youtube.com/watch?v=jGwO_UgTS7I&list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU)
- 全程指导代码书 : [**d2l-zh**](https://zh-v1.d2l.ai/)
- 深入了解深度学习背后的数学原理：**PRML**






## 所需要的配置

#### [**anaconda**](https://www.anaconda.com/)

Check installation

```
conda --version
```

Add system path

```
export PATH="/path/to/anaconda3/bin:$PATH"
```

Initialize Anaconda

```
source ~/anaconda3/bin/activate
conda init
```

Create an Anaconda environment

```
conda create -n xxx python=3.x(Change these values as needed with x)
```

Activate the Anaconda environment

```
conda activate xxx
```





#### **install  CUDA (12.0)**

```
# install CUDA 12.0
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget http://developer.download.nvidia.com/compute/cuda/12.0.0/local_installers/cuda-repo-ubuntu1804-12-0-local_12.0.0-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804-12-0-local_12.0.0-1_amd64.deb
sudo apt-key add /var/cuda-repo-ubuntu1804-12-0-local/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda
```



#### **install PyTorch（GPU 11.0**)

You need to choose a version that is adapted to CUDA 11.0, because PyTorch is usually distinguished by CUDA version.

```
# conda install PyTorch
conda install pytorch torchvision torchaudio cudatoolkit=11.0 -c pytorch

# or use pip
pip install torch torchvision torchaudio
```

#### **install MXNet（cu112 version）**

```
pip install mxnet-cu112
```

#### **install Keras (2.6)**

```
pip install keras==2.6
```



#### **install opencv**

OpenCV is a computer vision library that is open-source and free for use. It is widely used for a variety of applications, such as facial recognition, object tracking, and motion detection. OpenCV was developed by Intel and is written in C++, with interfaces available for Python, Java, and other programming languages.

```
sudo apt install libopencv-dev python3-opencv
```

The most current version of the OpenCV library may be obtained by compiling it from its source code. You’ll have full say over how the build is tailored to your machine’s specifications. This method is recommended for setting up OpenCV. To install the most recent OpenCV version directly from the source, follow these instructions:

Make backups of OpenCV and all its source code repositories：

```
mkdir ~/opencv_build && cd ~/opencv_build
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
```

Make a temporary directory to construct in, and then go to it after the download is complete:

```
cd ~/opencv_build/opencv
mkdir -p build && cd build
```

To make OpenCV, only need to setup CMake:

```
cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PINEFIX=/usr/local/ \
	-D INSTALL_C_EXAMPLES=ON \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D OPENCV_GENERATE_PKGCONFIG=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_build/opencv_contrib/modules \
	-D BUILD_EXAMPLES=ON ..
```

need to start the compilation process using:

```
make -j8
```

Modify the -j option to suit your CPU. The time required to create is system-specific, so if you’re not sure how many cores your CPU has, run nproc into the terminal to find out.

The next step is to Set up the OpenCV you can do this using the below command:

```
sudo make install
```

 Type the following steps to see the OpenCV version to ensure proper installation.

```
 pkg-config --modversion opencv4
 python3 -c "import cv2; print(cv2.__version__)"
```

