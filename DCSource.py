# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 17:14:13 2014

@author: jingsz
"""

import visa
import logging
import time


logging.basicConfig(level=logging.DEBUG)

class DCSource(visa.GpibInstrument):

    """ This class exists to handle the requirements of the
        Agilent 6633B System DC power supply 
        
   """
   
    def __init__(self, gpib_identifier, **keyw):
        super(DCSource, self).__init__(gpib_identifier, **keyw)
        self.Reset()
        self.clear()
        
    def Reset(self):
    
        """ Reset """
        
        self.write("*RST")
        logging.info("Reset succeed")
        
    def OutputOn(self):
    
        """ Enable the output """
        
        self.write("OUTPut ON")
        logging.info("Output On")
        
    def OutputOff(self):
    
        """ Disable the output """
        
        self.write("OUTPut OFF")
        logging.info("Output Off")


    def SetVoltage(self, voltage):
    
        """ Measure output voltage """
        
        self.write("VOLTage %s" % voltage)
        logging.info("Set Voltage to %s succeed", voltage)

    def MeasureVoltage(self):
    
        """ Measure output voltage """
        
        voltage = self.ask_for_values("MEASure:VOLTage?")
#         self.write("MEASure:VOLTage?")
#         voltage = self.read_values()
        logging.info("MEASure:VOLTage: %s", voltage)
        return voltage
       
    def SetCurrent(self, current):
    
        """ Measure output current """
        
        self.write("CURRent %s" % current)
        logging.info("Set current to %s succeed", current)

    def MeasureCurrent(self):
    
        """ Measure output current """
        
        current = self.ask_for_values("MEASure:CURRent?")
#         self.write("MEASure:CURRent?")
#         current = self.read_values()
        logging.info("MEASure:current: %s", current)
        return current

if __name__ == '__main__':
    try:
        dc = DCSource("GPIB0::7")
        dc.OutputOn()
#         dc.SetVoltage(1)
# #        time.sleep(10)
#         voltage = dc.MeasureVoltage()
        dc.SetCurrent(1)
        dc.MeasureCurrent()     
        
    except Exception, e:
        logging.error(e)

