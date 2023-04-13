import sys
sys.path
sys.path.insert(0, 'D:\BOT\BinanceBot\Service\collector')

class Builder(object):
    def local_loader(self):
        raise NotImplementedError()
 
    def SQL_Loader(self):
        raise NotImplementedError()
 
    def Collector_WSAPI(self):
        raise NotImplementedError()
 
    def Collector_RESTAPI(self):
        raise NotImplementedError()
    
    def CreateInfra(self):
        raise NotImplementedError()
 
 
class InfrastructureBuilder(Builder):
    def local_loader(self):
        return load()
 
    def SQL_Loader(self):
        return load()
 
    def build_lamp(self):
        return Lamp()
 
    def CreateInfra(self):
        body = self.build_body()
        lamp = self.build_lamp()
        battery = self.build_battery()
        return Flashlight(body, lamp, battery)
 
 
builder = FlashlightBuilder()
flashlight = builder.create_flashlight()
flashlight.on()
print flashlight  # Flashlight [on]