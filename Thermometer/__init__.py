import machine
import time

u = "f"

screen.font = font.ignore
screen.pen = color.rgb(255, 255, 255)

sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)
conversion_factor = 3.3 / (65535)

while True:
    
    if badge.pressed(BUTTON_A):
        u = "f"
    elif badge.pressed(BUTTON_B):
        u = "c"
    
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    
    if u == "f":
        temperature = (temperature*1.8 + 32)
    print(temperature)
    time.sleep(0.1)
    
    screen.pen = color.rgb(0,0,0)
    screen.clear()
    
    screen.pen = color.rgb(255,255,255)
    screen.text(str(temperature), 10, 40)
    
    badge.update()
