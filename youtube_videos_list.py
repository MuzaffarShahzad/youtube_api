import os
import json
import requests
from apiclient.discovery import build
import requests


youtube_api = "paste-your-youtube-api-here"

def get_api_data(API_KEY, Region):
    videos = []
    next_page_token = None
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    while 1:
        res = youtube.videos().list(part='snippet, recordingDetails, statistics',
        regionCode=Region, chart='mostPopular', maxResults=50, pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        if next_page_token is None:
            break
    return videos


api_data = get_api_data(youtube_api, 'US')

i = 0
for video in api_data:

    video_id = video['id']
    count = i = i+1
    print("Video No: " + str(count))
    print("Video URL: " + f"https://www.youtube.com/watch?v={video_id}")
    print("Video Title: " + video['snippet']['title'])
    v = video['statistics']
    print("Total Views: " + v['viewCount'])
    print("Total Likes: " + v['likeCount'])
    print("Total DisLikes: " + v['dislikeCount'])
    # print("Total Comments: " + v['commentCount'])
    print('_'*70)
