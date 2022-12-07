class Congestion:
    def __init__(self,congestion='',distance='',trend='',speed='',status='',desc=''):
        self.congestion = congestion
        self.distance = distance
        self.trend = trend
        self.speed = speed
        self.status = status
        self.desc = desc


class Traffic:
    def __init__(self,road_name='',evaluation='',congestion=Congestion()):
        self.road_name = road_name
        self.evaluation = evaluation
        self.congestion = congestion

