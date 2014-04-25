# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 17:14:13 2014

@author: jingsz
"""

import visa
import logging


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
        
    def MeasureVoltage(self):
    
        """ Measure output voltage """
        
        voltage = self.ask_for_values("MEAS:ARR:VOLT?")
        logging.info("Measure Voltage: %s", voltage)
        return voltage
        
if __name__ == '__main__':
    try:
        dc = DCSource("GPIB0::7")
        dc.OutputOn()
        voltage = dc.MeasureVoltage()
            
        
    except Exception, e:
        logging.error(e)

