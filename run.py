def abc(p): 
    print(123)
from machine import Pin
p0 = Pin(4, Pin.IN)
p0.irq(abc, Pin.IRQ_HIGH_LEVEL)
sleep(10000)