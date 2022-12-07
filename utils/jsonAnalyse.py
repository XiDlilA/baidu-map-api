import json
from model.traffic import Congestion,Traffic

class JsonAnalyse():
    def __init__(self, res, road_name):
        self.json = json.loads(res)
        self.traffic = self.getTraffic(road_name)
    
    def getTraffic(self,road_name):
        traffic = Traffic(road_name=road_name)
        if self.json == None:
            return traffic
        traffic.evaluation = self.getEvaluation()
        traffic.congestion = self.getCongestion()
        return traffic



    def getEvaluation(self):
        if 'evaluation'  not in self.json:
            return '失去 evaluation 字段'
        if 'status_desc' not in self.json['evaluation']:
            return '失去 status_desc 字段'
        return self.json['evaluation']['status_desc']

    def getCongestion(self):
        if 'road_traffic' not in self.json:
            return Congestion(congestion='失去 road_traffic 字段')
        if 'congestion_sections' not in self.json['road_traffic'][0]:
            return Congestion(congestion='失去 congestion_sections 字段')
        congestion = Congestion(congestion="正常")
        for section in self.json['road_traffic'][0]['congestion_sections']:
            congestion.desc += '失去 section_desc 字段 ' if 'section_desc' not in section else section['section_desc']+' '
            congestion.distance += '失去 congestion_distance 字段 ' if 'congestion_distance' not in section else str(section['congestion_distance'])+' '
            congestion.trend += '失去 congestion_trend 字段 ' if 'congestion_trend' not in section else section['congestion_trend']+' '
            congestion.speed += '失去 speed 字段 ' if 'speed' not in section else str(section['speed'])+' '
            congestion.status += '失去 status 字段 ' if 'status' not in section else self.getCongestionStatus(section['status'])+' '
            return congestion
    def getCongestionStatus(self,status):
        if status == 1:
            return '畅通'
        elif status == 2:
            return '缓行'
        elif status == 3:
            return '拥堵'
        elif status == 4:
            return '严重拥堵'
        else:
            return '未知路况'