import urllib #importing to use its urlencode function
import urllib3 #for making http requests
import requests
import json #for decoding a JSON response
import pandas as pd
from openpyxl import *
from datetime import datetime
import pymysql as MySQLdb
import locale


keys = []


key_numara = 0
API_KEY = keys[key_numara] 

db = MySQLdb.connect("ip","user","password","db_names" )
cursor = db.cursor()


query="SELECT * FROM kanal"
cursor.execute(query)

kanallar = cursor.fetchall()

kanal_list=[]
for i in kanallar:
    kanal_list.append(i[0])

 
def listele(ChannelIdentifier):
    try:
        url = "https://www.googleapis.com/youtube/v3/channels?id="+ChannelIdentifier+"&key="+API_KEY+"&part=contentDetails"
        response = urllib.request.urlopen(url)
        videos= json.load(response)

        for video in videos['items']:
            ChannelUploadId = video["contentDetails"]["relatedPlaylists"]["uploads"]

        print(ChannelUploadId)



        url = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId="+ ChannelUploadId +"&key="+API_KEY+"&part=snippet&maxResults=50"
        response = urllib.request.urlopen(url) #makes the call to YouTube
        videos = json.load(response)
        deneme = videos
        i=0
        videolist = []
        for video in videos['items']:
            metadata = video["snippet"]["resourceId"]["videoId"]
            videolist.append(metadata)
            try:
                query = f"insert into videoliste(videoID,kanal_ID) values ('{metadata}','{ChannelIdentifier}')"
                cursor.execute(query)
                db.commit()
            except:
                continue
            i += 1
            print(i)

        TokenCode = deneme["nextPageToken"]
        url = "https://www.googleapis.com/youtube/v3/playlists?part=snippet,contentDetails&channelId="+ChannelIdentifier+"&maxResults=50&key="+API_KEY+"&pageToken="+TokenCode
        response = urllib.request.urlopen(url) #makes the call to YouTube
        videos = json.load(response)
        TokenCode2 = videos["prevPageToken"]
        #print(TokenCode2)
        url = "https://www.googleapis.com/youtube/v3/playlists?part=snippet,contentDetails&channelId="+ChannelIdentifier+"&maxResults=50&key="+API_KEY+"&pageToken="+TokenCode2
        response = urllib.request.urlopen(url) #makes the call to YouTube
        videos = json.load(response)
        for video in videos["items"]:
            listeId = video["id"]
            url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails&maxResults=50&playlistId="+listeId+"&key="+API_KEY
            response = urllib.request.urlopen(url) #makes the call to YouTube
            videos2 = json.load(response)
            for video in videos2['items']:
                metadata = video["snippet"]["resourceId"]["videoId"]
                videolist.append(metadata)
                i += 1
                #sheet.cell(row=i,column=1,value=metadata)
                print(i)
                print(ChannelIdentifier)
        for x in videolist:
            try:
                query = f"insert into videoliste(videoID,kanal_ID) values ('{x}','{ChannelIdentifier}')"
                cursor.execute(query)
            except:
                continue

    except Exception as e:
        return 1

for ChannelIdentifier in kanal_list:
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


        


