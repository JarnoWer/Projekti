#!/usr/bin/python3

import gspread
import datetime
import time
import smbus
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Desktop/Projekti/pitemps-key.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('pitemps').sheet1

#wks.delete_row(2)

#print(wks.get_all_records())

bus = smbus.SMBus(3)
config = [0x00, 0x00]
bus.write_i2c_block_data(0x18, 0x01, config)
bus.write_byte_data(0x18, 0x08, 0x03)
time.sleep(0.5)

data = bus.read_i2c_block_data(0x18, 0x05, 2)


ctemp = ((data[0] & 0x1F) * 256) + data[1]
if ctemp > 4095 :
	ctemp -= 8192
ctemp = ctemp * 0.0625

date = str(datetime.datetime.now().strftime('%d.%m.%Y %H:%M'))
#time = str(datetime.datetime.now().strftime('%H:%M:%S'))


wks.append_row([date, ("%.2f" % ctemp)])
