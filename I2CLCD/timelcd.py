#!/usr/bin/python
import smbus
import I2C_LCD_driver
import time
mylcd = I2C_LCD_driver.lcd()

bus = smbus.SMBus(3)
config = [0x00, 0x00]
bus.write_i2c_block_data(0x18, 0x01, config)
bus.write_byte_data(0x18, 0x08, 0x03)


x = 0;
while True:

	data = bus.read_i2c_block_data(0x18, 0x05, 2)
	ctemp = ((data[0] & 0x1F) * 256) + data[1]
	if ctemp > 4095 :
		ctemp -= 8192
	ctemp = ctemp * 0.0625
	string_value = str("%.2f" % ctemp + " C")

	mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 1)
	x = x + 1
	time.sleep(1)
	if x == 10:
		x = 0
		mylcd.lcd_display_string("Temp: " + string_value, 2)
	

