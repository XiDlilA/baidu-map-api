from model.user import UserList
from utils.jsonAnalyse import JsonAnalyse
import pandas as pd
from urllib import parse
import hashlib
import requests
from datetime import datetime

class BaiduMapAPI:
    def __init__(self, userId):
        self.baseURL = "https://api.map.baidu.com"
        self.city = "武汉市"
        self.userList = UserList(userId)
        self.trafficData = None
    
    # 计算 SN
    def getBaiduSN(self,queryStr):
        encodedStr = parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
        rawStr = encodedStr + self.userList.currentUser.sk
        sn = (hashlib.md5(parse.quote_plus(rawStr).encode("utf8")).hexdigest())
        return sn

    # 获取 指定道路 路况
    def getRoadTaffic(self,road):
        queryStr = "/traffic/v1/road?road_name={}&city={}&ak={}".format(road,self.city,self.userList.currentUser.ak)
        sn = self.getBaiduSN(queryStr)
        url = parse.quote(self.baseURL + queryStr + "&sn=" + sn, safe="/:=&?#+!$,;'@()*[]")
        res = requests.get(url).text
        return res

    def createWuHanTraffic(self):
        self.trafficData = pd.DataFrame(columns=['road_name','current_time','evaluation','congestion','congestion_distance','congestion_trend','speed','congestion_status','congestion_desc'])

    def writeWuHanTraffic(self, res, road_name):
        trafficInfo = JsonAnalyse(res, road_name).traffic
        if self.trafficData is None:
            self.createWuHanTraffic()
        self.trafficData = pd.concat([self.trafficData, pd.DataFrame(
                    {
                        'road_name':trafficInfo.road_name,
                        'current_time':str(datetime.now()),
                        'evaluation':trafficInfo.evaluation,
                        'congestion':trafficInfo.congestion.congestion,
                        'congestion_distance':trafficInfo.congestion.distance,
                        'congestion_trend':trafficInfo.congestion.trend,
                        'speed':trafficInfo.congestion.speed,
                        'congestion_status':trafficInfo.congestion.status,
                        'congestion_desc':trafficInfo.congestion.desc
                    }
                    ,index=[0])], 
                    ignore_index=True)
