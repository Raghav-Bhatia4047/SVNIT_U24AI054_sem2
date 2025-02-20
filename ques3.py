class converter:
    meter={"inches":39.37,"feet":3.28,"yards":1.093,"miles":0.00062,"kilometers":0.001,"meters":1,"centimeters":100,"millimeters":1000}
    def _init_(self,length,unit):
        self.unit=unit.lower()
        self.length=length
    def convert_to_meter(self):
        return self.length/converter.meter[self.unit]
    #def convert(self,unit1):
    #   a=self.convert_to_meter()
    #   return a*converter.meter[unit1]
    def meters(self):
        return self.convert_to_meter()*converter.meter["meters"]
    def feet(self):
        return self.convert_to_meter()*converter.meter["feet"]
    def inches(self):
        return self.convert_to_meter()*converter.meter["inches"]
    def miles(self):
        return self.convert_to_meter()*converter.meter["miles"]
    def centimeters(self):
        return self.convert_to_meter()*converter.meter["centimeters"]
    def millimeters(self):
        return self.convert_to_meter()*converter.meter["millimeters"]
    def kilometers(self):
        return self.convert_to_meter()*converter.meter["kilometers"]
a=converter(12,"inches")
print(round(a.meters(),2))        
print(round(a.feet(),2))          
print(round(a.inches(),2))        
print(round(a.miles(),4))         
print(round(a.centimeters(),2))   
print(round(a.millimeters(),2))
print(round(a.kilometers(),4))