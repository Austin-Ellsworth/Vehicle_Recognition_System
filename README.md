# Vehicle_Recognition_System

IMPORTANT: Before this program will run, weights must be downloaded from https://pjreddie.com/darknet/yolo/.

A vehicle recognition system.

Usage image: 

Use --help to see usage of car_make_model_classifier_yolo3.py:

$ python car_make_model_classifier_yolo3.py --image cars.jpg

Usage video: 

Use --help to see usage of car_make_model_classifier_yolo3_video.py:

$ python car_make_model_classifier_yolo3_video.py --input video.avi --output output.avi
$ python car_make_model_classifier_yolo3_video.py [-h] [--yolo MODEL_PATH] [--confidence CONFIDENCE] [--threshold THRESHOLD] [--input] [--output]

required arguments:
  -i, --input              path to input video
  -o, --output             path to output video

optional arguments:
  -h, --help               show this help message and exit
  --yolo MODEL_PATH        path to YOLO model weight file, default yolo-coco
  --confidence CONFIDENCE  minimum probability to filter weak detections, default 0.5
  --threshold THRESHOLD    threshold when applying non-maxima suppression, default 0.3


Requirements
python
numpy
tensorflow
opencv
yolov3.weights must be downloaded from https://pjreddie.com/media/files/yolov3.weights and saved in folder yolo-coco









Open Sources Used:

Licensed under the MIT License

Stanford car dataset: 

https://ai.stanford.edu/~jkrause/cars/car_dataset.html
