#!/usr/bin/python3

from os import X_OK
import jetson.inference
import jetson.utils
import random
import serial

import argparse
import sys

# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.",
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

parser.add_argument("input_URI", type=str, default="",
                    nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="",
                    nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2",
                    help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf",
                    help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5,
                    help="minimum detection threshold to use")

is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)

# create video output object
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv+is_headless)

# load the object detection network
net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)

# create video sources
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)

# Center coordinates in degrees
point_x = 41
point_y = 21

# THe coordinates that we want to move to
x = 0
y = 0

# How much to move in degrees
move_x = 0
move_y = 0

def gen_randx():
	return random.randrange(0, 82)

def gen_randy():
	return random.randrange(0, 52)

def rand_xy(top, bottom, right, left):
	x = gen_randx()
	y = gen_randy()
	while (left < x < right):
		x = gen_randx()

	while (top < y < bottom):
		y = gen_randy()

with serial.Serial('/dev/ttyUSB0',9600,timeout=3.) as port:
	# process frames until the user exits
	while True:
		# capture the next image
		img = input.Capture()

		# detect objects in the image (with overlay)
		detections = net.Detect(img, overlay=opt.overlay)

		# print the detections
		print("detected {:d} objects in image".format(len(detections)))

		catDetected = False

		for detection in detections:
			if detection.ClassID == 1:
				print(detection)
				rand_xy(detection.Top, detection.Right, detection.Bottom, detection.Left)

				if (x < point_x):
					move_x = x - point_x
				else:
					move_x = point_x - x

				if (y < point_y):
					move_y = y - point_y
				else:
					move_y = point_y - y

				## Send command to move by how many degrees in x and y axis
				catDetected = True

		if catDetected:
#			moveCommand(move_x, move_y)
			port.write(4)
			port.write(5)
    	port.flush()
		else:
			port.write(0)
			port.flust()

		# render the image
		output.Render(img)

		# update the title bar
		output.SetStatus("{:s} | Network {:.0f} FPS".format(opt.network, net.GetNetworkFPS()))

		# print out performance info
		net.PrintProfilerTimes()

		# exit on input/output EOS
		if not input.IsStreaming() or not output.IsStreaming():
			break
