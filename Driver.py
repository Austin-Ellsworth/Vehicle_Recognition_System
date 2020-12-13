import car_make_model_classifier_yolo3
import Main
import argparse
import cv2
import csv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-y", "--yolo", default='yolo-coco',
	help="base path to YOLO directory")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
ap.add_argument("-t", "--threshold", type=float, default=0.3,
	help="threshold when applying non-maxima suppression")
args = vars(ap.parse_args())

car_make_model_classifier_yolo3.classify(args["image"])

makeAndModel = car_make_model_classifier_yolo3.getMakeAndModel()
plate = Main.getLicensePlate()

print("Result: \nMake: " + makeAndModel[0] + ", Model: " + makeAndModel[1] + ", plate: " + plate)

makeFlag = False
modelFlag = False
plateFlag = False 

with open("CarList.csv", 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		if makeAndModel[0] == row[0]:
			makeFlag = True
		if makeAndModel[1] == row[1]:
			modelFlag = True
		if plate == row[2]:
			plateFlag = True

if makeFlag & modelFlag & plateFlag:
	print("\n***Access Granted!***\nGate Opening...")
else:
	print("\n***Access Denied.***\nCall Gate Security For Access")