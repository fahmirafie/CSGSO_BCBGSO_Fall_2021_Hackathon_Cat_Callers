# file for testing constant sending of hello world and receiving ping back to print
# argument 0 is /dev/video0 for camera input
import jetson.inference
import jetson.utils
import random
import serial
import time

import argparse
import sys

# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.",
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use")

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

SERIAL_OUTPUT = '/dev/ttyACM0'
with serial.Serial(SERIAL_OUTPUT) as port:
    time.sleep(1.6)
    while True:
    	img = input.Capture() # capture the next image
    	detections = net.Detect(img, overlay=opt.overlay) # detect objects in the image (with overlay)

    	port.write("hello world")
        port.flush()
        response = port.readline()
        print(response)
        time.sleep(.1)

    	for detection in detections:
    		print(detection)
        if detection.ClassID == 17:
          center = detection.Center

    	# render the image
    	output.Render(img)

    	# print out performance info
    	net.PrintProfilerTimes()

    	# exit on input/output EOS
    	if not input.IsStreaming() or not output.IsStreaming():
    		break
