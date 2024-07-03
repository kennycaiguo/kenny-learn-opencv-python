"""
查看所有被支持的鼠标事件：
"""
import cv2 as cv
events = [i for i in dir(cv) if 'EVENT' in i]
print( events )