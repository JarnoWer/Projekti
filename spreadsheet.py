import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('PiTemps-7d01faf50d0e.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('pitemps').sheet1

#wks.delete_row(2)

print(wks.get_all_records())

#wks.append_row(['column1', 'column2', 'column3'])
