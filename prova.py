import Adafruit_DHT
import RPi.GPIO as gp
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
HYG_PIN = 8
RES_PIN = 11
BLUE_PIN= 15
RED_PIN = 16

gp.setwarnings(False)

gp.setmode(gp.BOARD)


gp.setup(HYG_PIN, gp.IN)
gp.setup(RED_PIN, gp.OUT)
gp.setup(BLUE_PIN, gp.OUT)

gp.output(RED_PIN, False)
gp.output(BLUE_PIN, False)

while True:


    #RESISTOR TURNS OUTPUT MODE
    gp.setup(RES_PIN, gp.OUT)
    gp.output(RES_PIN, gp.LOW)
    
    time.sleep(0.1)
    
    #RESISTOR TURNS INPUT MODE
    gp.setup(RES_PIN, gp.IN)
    currentTime = time.time()
    diff = 0
    
    while(gp.input(RES_PIN) == gp.LOW):
        diff = time.time() - currentTime
        
    print("Light param= {0:0.3f}".format(diff*1000))
    
    #DHT11 CONTROL
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
    
        if temperature < 20 or temperature > 27:
            gp.output(RED_PIN, True)
        else:
            gp.output(RED_PIN, False)
        
            
        print("Temperature: "+str(temperature)+"C\nHumidity: "+str(humidity)+"%")
    else:
        print("DHT failure")
    
    #HYGROMETER CONTROL
    if gp.input(HYG_PIN) is not None:
        water = not gp.input(HYG_PIN)
        if not water:
            gp.output(BLUE_PIN, True)
        else:
            gp.output(BLUE_PIN, False)
            
        print(water)
    else:
        print("Hygrometer failure")
    
    #BED TIME
    time.sleep(60)
