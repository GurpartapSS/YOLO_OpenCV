# YOLO_OpenCV
Implementation of state of the art image classification technique YOLO using OpenCV to detect objects in real time.

pretrained weights can be downloaded from https://pjreddie.com/darknet/yolo/

Also contains code for YOLO to do Custom Object Detection, from downloading images to creating labels and training your NN.
The structure for creating a custom object detection is inspired from https://github.com/markjay4k/YOLO-series with modifications to make the codes more robust.

you will need to install google_images_download to use the get_images module

I have added only the keywords, limit and output directory as arguments, feel free to go through https://github.com/hardikvasa/google-images-download/blob/master/google_images_download/google_images_download.py to add other arguments to the main code and see how the download works. 
