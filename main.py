from sense_hat import SenseHat
import time 

sense = SenseHat()

image = ["santa_1.png","santa_2.png","santa_3.png","santa_4.png","santa_5.png","santa_6.png","santa_7.png","santa_8.png"]

while True:
	for i in range (0,len(image)):
		sense.load_image(image[i])
		time.sleep(1)


