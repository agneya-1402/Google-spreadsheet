import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope=["https://www.googleapis.com/auth/drive"]
creds=ServiceAccountCredentials.from_json_keyfile_name('spreadsheet_api.json',scope)
gc=gspread.authorize(creds)
sh=gc.open_by_url('https://docs.google.com/spreadsheets/d/1z3e4xs8Wf7-0cJZ2n7CfB8rGpIw355_sgAHUuyJY7xA/edit#gid=0').sheet1
data=sh.get_all_records()
print(data)