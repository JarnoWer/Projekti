import smbus
import time
import I2C_LCD_driver


# Get I2C bus

i = 0
mylcd = I2C_LCD_driver.lcd()
bus = smbus.SMBus(3)
# MCP9808 address, 0x18(24)
# Select configuration register, 0x01(1)
#0x0000(00)	Continuous conversion mode, Power-up default
config = [0x00, 0x00]
bus.write_i2c_block_data(0x18, 0x01, config)
# MCP9808 address, 0x18(24)
# Select resolution rgister, 0x08(8)
#0x03(03)	Resolution = +0.0625 / C
bus.write_byte_data(0x18, 0x08, 0x03)
time.sleep(0.5)

mylcd.lcd_clear()
while i < 6:
	# MCP9808 address, 0x18(24)
	# Read data back from 0x05(5), 2 bytes
	# Temp MSB, TEMP LSB
	data = bus.read_i2c_block_data(0x18, 0x05, 2)

	# Convert the data to 13-bits
	ctemp = ((data[0] & 0x1F) * 256) + data[1]
	if ctemp > 4095 :
		ctemp -= 8192
	ctemp = ctemp * 0.0625
	ftemp = ctemp * 1.8 + 32
	string_value = str("%.2f" % ctemp)
	mylcd.lcd_display_string(string_value, 1)

	mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 2)
	time.sleep(5)
	mylcd.lcd_clear()
	
	i += 1


