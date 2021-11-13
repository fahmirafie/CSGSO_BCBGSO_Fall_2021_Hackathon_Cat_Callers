# file for testing constant sending of hello world and receiving ping back to print
# argument 0 is /dev/video0 for camera input
import jetson.inference
import jetson.utils
import random
import serial
import time

arduino = serial.Serial(
port = 'dev/ttyACM10',
baudrate = 9600,
bytesize = serial.EIGHTBITS, 
parity = serial.PARITY_NONE,
stopbits = serial.STOPBITS_ONE,
timeout = 5,
xonxoff = False,
rtscts = False,
dsrdtr = False,
writeTimeout = 2)

while True:
    try:
        arduino.write("command from jetson")
        data = arduino.readline()
        if data:
            print(data)
        time.sleep(1)
    except Exception as e:
        print(e)
        arduino.close()

# # create video output object
# output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv+is_headless)
#
# # load the object detection network
# net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)
#
# # create video sources
# input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)
#
# SERIAL_OUTPUT = '/dev/ttyACM0'
# with serial.Serial(SERIAL_OUTPUT) as port:
#     time.sleep(1.6)
#     while True:
#     	img = input.Capture() # capture the next image
#     	detections = net.Detect(img, overlay=opt.overlay) # detect objects in the image (with overlay)
#
#     	port.write("hello world")
#         port.flush()
#         response = port.readline()
#         print(response)
#         time.sleep(.1)
#
#     	for detection in detections:
#     		print(detection)
#         if detection.ClassID == 17:
#           center = detection.Center
#
#     	# render the image
#     	output.Render(img)
#
#     	# print out performance info
#     	net.PrintProfilerTimes()
#
#     	# exit on input/output EOS
#     	if not input.IsStreaming() or not output.IsStreaming():
#     		break
