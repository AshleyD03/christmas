from sense_hat import SenseHat
import time 

sense = SenseHat()

image = ["candycane_1.png", "candycane_2.png", "penguin_1.png", "penguin_2.png",
	"present_1.png", "present_2.png"]

while True:
	for i in range (0,len(image)):
		sense.load_image(image[i])
		time.sleep(1)


