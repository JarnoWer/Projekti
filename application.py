#!/usr/bin/python

import gspread
import datetime
import smbus
import I2C_LCD_driver
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('PiTemps-7d01faf50d0e.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('pitemps').sheet1

#wks.delete_row(2)

#print(wks.get_all_records())

i = 0
mylcd = I2C_LCD_driver.lcd()
bus = smbus.SMBus(3)
config = [0x00, 0x00]
bus.write_i2c_block_data(0x18, 0x01, config)
bus.write_byte_data(0x18, 0x08, 0x03)
time.sleep(0.5)

mylcd.lcd_clear()
while i < 6:

	data = bus.read_i2c_block_data(0x18, 0x05, 2)


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


date = str(datetime.datetime.now().strftime('%d.%m.%Y'))
time = str(datetime.datetime.now().strftime('%H:%M:%S'))
temp = str(2.0)

wks.append_row([date, time, temp])
