import urllib #importing to use its urlencode function
import urllib3 #for making http requests
import requests
import json #for decoding a JSON response
import pandas as pd
from openpyxl import *
from datetime import datetime
import pymysql as MySQLdb
import locale

keys = [
"AIzaSyCpKCUBkus7sYBH1u6w_-BIIdXq8IKX03k",
"AIzaSyBhhYCzK79eqDyAhZYB9uNuYezwrjynseE",
"AIzaSyB3uQTXQFBOE2TXf4M5xmbpm8Ic_YaMaEs",
"AIzaSyAw_nV3pQRZqmAgDHtrcdGMaE_NS3Yhj6c",
"AIzaSyDjll6VqDSp1xJel_KpVpy-_REhrHWBy2s",
"AIzaSyDkxu2_iKISHvPS-LBpyLT2Rlgzqkh9HJw",
"AIzaSyBUkGqoo6ATje9Li3TFaNtPyhe7Vz7RZEE",
"AIzaSyBx4gA9Ncj_0h3SNwd8eVt3vhWYaZMutHs",
"AIzaSyB1GfWmInAD5aZXuv0Pg-KFa9vXHiHfuok" 
  ]

key_numara = 5
API_KEY = keys[key_numara] 

db = MySQLdb.connect("safamoda.cf","yonetici","789632145xA.","youtube" )
cursor = db.cursor()

query="Select * from kanal"
df = pd.read_sql(query, con=db)
kanalID_list = df["ID"].unique()

def listele(ChannelIdentifier):
    sayac = 0
    try:
        upload_id_list=[]
        video_list=[]
        url = f"https://www.googleapis.com/youtube/v3/playlists?part=snippet&maxResults=50&channelId={ChannelIdentifier}&key={API_KEY}"
        response = urllib.request.urlopen(url)
        videos= json.load(response)
        try:
            token = videos['nextPageToken']
        except:
            token=None

        for video in videos['items']:
            ChannelPlayListID = video["id"]
            print(ChannelPlayListID)
            upload_id_list.append(ChannelPlayListID)
        
        if token!=None:
            url = f"https://www.googleapis.com/youtube/v3/playlists?part=snippet&pageToken={token}&maxResults=50&channelId={ChannelIdentifier}&key={API_KEY}"
            response = urllib.request.urlopen(url)
            videos= json.load(response)
            for video in videos['items']:
                ChannelPlayListID = video["id"]
        
        for uploadid in upload_id_list:
            url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={uploadid}&key={API_KEY}"
            response = urllib.request.urlopen(url)
            videos= json.load(response)
            for video in videos['items']:
                videoID = video["snippet"]["resourceId"]["videoId"]
                video_list.append(videoID)
                sayac += 1
                print(sayac)
            
            try:
                token = videos['nextPageToken']
                print(token)
            except:
                token=None

            while token!=None:
                url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&pageToken={token}&maxResults=50&playlistId={uploadid}&key={API_KEY}"
                response = urllib.request.urlopen(url)
                videos= json.load(response)
                for video in videos['items']:
                    videoID = video["snippet"]["resourceId"]["videoId"]
                    print(videoID)
                    video_list.append(videoID)
                    sayac += 1
                    print(sayac)
                try:
                    token = videos['nextPageToken']
                except:
                    token=None
        for x in video_list:
            try:
                query = f"insert into videoliste(videoID,kanal_ID) values ('{x}','{ChannelIdentifier}')"
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
        db.commit()

    except Exception as e:
        print(e)
        return 1

        

for ChannelIdentifier in kanalID_list:
    a = listele(ChannelIdentifier)
    if a==1:
        key_numara += 1
        if key_numara == 8:
            key_numara = 0
        API_KEY = keys[key_numara]
        listele(ChannelIdentifier)

cursor.close()
db.commit()
db.close()
