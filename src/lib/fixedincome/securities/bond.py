'''
Created on Jun 26, 2017

@author: alinaved
'''
class BondCalculator( object ):
    def __init__(self, bond ,*args, **kwargs):
        self.bond = bond
        object.__init__(self, *args, **kwargs)
        
    def getCouponValue(self):
        return ( 100 * self.bond.interest_rate / self.bond.par_value )
    
    def getParValue(self):
        return self.bond.par_value
    
    def getNextCouponDate(self):
        raise NotImplementedError