import params

def myship():

	while True:	
					
		vt100.move(uart, 0, 0)
		result = [0, 0 ,0]
		
		result = [get_axis(uart, 0x28), get_axis(uart, 0x2A), get_axis(uart, 0x2C)]

		if result[0] >= 1:
			vt100.clear_screen(uart)

		if result[0] >= 0.3:
			leds[0].on()
			leds[1].off()
			position[0] -= 1
		elif result[0] <= -0.3:
			leds[0].off()
			leds[1].on()
			position[0] += 1
		else:
			leds[0].off()
			leds[1].off()

		if result[1] >= 0.3:
			leds[2].on()
			leds[3].off()
			position[1] -= 1
		elif result[1] <= -0.3:
			leds[2].off()
			leds[3].on()
			position[1] += 1
		else:
			leds[2].off()
			leds[3].off()

		vt100.move(uart, position[0], position[1])
		uart.write("0^^0")
		pyb.delay(200)