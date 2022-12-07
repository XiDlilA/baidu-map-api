import pandas as pd
from utils.baiduMapAPI import BaiduMapAPI
import time
from utils.Argparse import Parser


userId = Parser().args.user
API = BaiduMapAPI(userId)
user = API.userList.currentUser.name
# 获取路段名
road_names = pd.read_excel('./data/road_exist.xlsx')
# 根据路段名查询相关数据并存储
for road_name in road_names['road_name']:
    res = API.getRoadTaffic(road_name)
    print("user:{},road:{},res:{}".format(user,road_name, res))
    API.writeWuHanTraffic(res,road_name)

API.trafficData.to_excel('./result/wuhan_traffic_'+str(time.strftime("%y%m%d_%H%M%S"))+'.xlsx')
