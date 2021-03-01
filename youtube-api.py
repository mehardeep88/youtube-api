api_key = 'AIzaSyAdow-Z77Q77Khs_q70_ozqE8kZp5PhhNs'
from googleapiclient.discovery import build
youtube = build('youtube','v3',developerKey=api_key)
req = youtube.channels().list(part='statistics',forUsername='schafer5')
res = req.execute()
print(res)