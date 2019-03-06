#!/usr/bin/python

import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('PiTemps-7d01faf50d0e.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('pitemps').sheet1

#wks.delete_row(2)

#print(wks.get_all_records())

date = str(datetime.datetime.now().strftime('%d.%m.%Y'))
time = str(datetime.datetime.now().strftime('%H:%M:%S'))
temp = str(2.0)

wks.append_row([date, time, temp])
