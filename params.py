import pyb 
import vt100


MAX_HEIGHT = 20
MAX_WIDTH = 80

def convert_value(high, low):
	value = (high << 8) | low
	if value & (1 << 15):
		value = value - (1 << 16)
	
	return value
	
def get_axis(uart, address):
	result = 0

	value = [0, 0]

	CS.low()
	spi.send(0x80 | address+1)
	value[0] = spi.recv(1)[0]
	CS.high()

	CS.low()
	spi.send(0x80 | address)
	value[1] = spi.recv(1)[0]
	CS.high()

	result = convert_value(value[0], value[1])

	result /= 16384

	return result

    
uart = pyb.UART(2)
uart.init(115200, bits=8, parity=None, stop=1)

CS = pyb.Pin("PE3", pyb.Pin.OUT_PP)
spi = pyb.SPI(1, pyb.SPI.MASTER, baudrate=50000, polarity=0, phase=0)
value = 0
CS.low()
spi.send(0x8f)
values = spi.recv(1)
CS.high()
uart.write(str(values[0]) + "\r\n")

CS.low()
spi.send(0x00 | 0x20)
spi.send(0x77)
CS.high()


leds = [pyb.LED(1), pyb.LED(2), pyb.LED(3), pyb.LED(4)]

vt100.clear_screen(uart)

position = [40, 17]