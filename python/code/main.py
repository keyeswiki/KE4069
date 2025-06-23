import utime
potentiometer = machine.ADC(26) #将GP26作为模拟信号采集引脚

while True:
   voltage = potentiometer.read_u16() 
   print(voltage) #打印模拟值
   utime.sleep(0.1)
   