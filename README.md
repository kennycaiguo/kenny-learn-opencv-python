# learn-opencv-python
# 学习opencv python
# Python3.10安装matplotlib的问题
## 1.python3.10需要安装3.5.3版本的matplotlib,安装低于这个版本的会报错
C:\Users\Administrator>pip install matplotlib==3.5.3
Collecting matplotlib==3.5.3
  Downloading matplotlib-3.5.3-cp310-cp310-win_amd64.whl.metadata (6.7 kB)
Requirement already satisfied: cycler>=0.10 in d:\programs\python310\lib\site-packages (from matplotlib==3.5.3) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in d:\programs\python310\lib\site-packages (from matplotlib==3.5.3) (4.53.1)
Requirement already satisfied: kiwisolver>=1.0.1 in d:\programs\python310\lib\site-packages (from matplotlib==3.5.3) (1.4.5)
Requirement already satisfied: numpy>=1.17 in d:\programs\python310\lib\site-packages (from matplotlib==3.5.3) (2.0.1)
Requirement already satisfied: packaging>=20.0 in d:\programs\python310\lib\site-packages (from matplotlib==3.5.3) (24.1)
Requirement already satisfied: pillow>=6.2.0 in d:\programs\python310\lib\site-packages (from matplotlib==3.5.3) (10.4.0)
Requirement already satisfied: pyparsing>=2.2.1 in d:\programs\python310\lib\site-packages (from matplotlib==3.5.3) (3.1.2)
Requirement already satisfied: python-dateutil>=2.7 in d:\programs\python310\lib\site-packages (from matplotlib==3.5.3) (2.9.0.post0)
Requirement already satisfied: six>=1.5 in d:\programs\python310\lib\site-packages (from python-dateutil>=2.7->matplotlib==3.5.3) (1.16.0)
Downloading matplotlib-3.5.3-cp310-cp310-win_amd64.whl (7.2 MB)
   ---------------------------------------- 7.2/7.2 MB 9.2 MB/s eta 0:00:00
Installing collected packages: matplotlib
Successfully installed matplotlib-3.5.3

## 2.MatPlotlib不支持numpy2.x,这里需要安装numpy1.26.4版本,低于这个版本会报错
C:\Users\Administrator>pip install numpy==1.26.4
Collecting numpy==1.26.4
  Downloading numpy-1.26.4-cp310-cp310-win_amd64.whl.metadata (61 kB)
Downloading numpy-1.26.4-cp310-cp310-win_amd64.whl (15.8 MB)
   ---------------------------------------- 15.8/15.8 MB 5.3 MB/s eta 0:00:00
Installing collected packages: numpy
Successfully installed numpy-1.26.4
这两点需要注意,否则可能会出现安装了matplotlib但是导入会出错的问题

# <a href="https://digi.bib.uni-mannheim.de/tesseract/">Tesseract的常用网址1</a>
# <a href="https://github.com/tesseract-ocr/tesseract">Tesseract官方网站</a>
# <a href="https://github.com/AjayAndData/Licence-plate-detection-and-recognition---using-openCV-only">opencv识别车牌，保存为图片，并且使用tessact识别为文字输出</a>
# <a href="https://github.com/rendong3/OpenCV-Notes">OpenCv 学习笔记</a>
# <a href="https://github.com/1zlab/1ZLAB_Color_Block_Finder">使用OpenCV实现色块追踪 为了方便大家入门OpenCV</a>
# <a href="https://github.com/LeBron-Jian/ComputerVisionPractice">opencv练习的代码与图片</a>
# <a href="https://blog.csdn.net/youcans/article/details/124576698">【youcans 的 OpenCV 例程200篇】173.SEEDS 超像素区域分割</a>
# <a href="https://github.com/wuxh123/my_opencv_examples">OpenCV+Qt编程</a>
# <a href="https://github.com/bashendixie/ml_toolset">机器学习案例集</a>
# <a href="https://github.com/BUPTLdy/human-detector">Human Detection using HOG-Linear SVM in Python</a>
# <a href="https://github.com/CHNicelee/HOG_SVM">使用HOG+SVM进行图像分类</a>
# <a href="https://github.com/bikz05/object-detector">Object Detection Framework using HOG as descriptor and Linear SVM as classifier.</a>
# <a href="https://github.com/makelove/OpenCV-Python-Tutorial">OpenCV教程</a>
# <a href="https://github.com/zhongqiangwu960812/OpenCVLearning">OpenCV或者数字图像处理的小项目</a>
# <a href="https://github.com/shekkizh/ImageProcessingProjects">Image processing using python and opencv</a>
# <a href="https://github.com/tinyzqh/Opencv-Computer-Vision-Practice-Python-">Opencv 计算机视觉实战——项目实战，少了car1.h5</a>
# <a href="https://github.com/ishanExtreme/RealTimeParkingSystem/blob/master/car1.7z">下载car1.h5</a>
# <a href=""></a>
# <a href=""></a>
# <a href=""></a>
# <a href=""></a>
# <a href=""></a>
# <a href=""></a>
# <a href=""></a>
