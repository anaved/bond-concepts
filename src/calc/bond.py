'''
Created on Jun 26, 2017

@author: alinaved
'''
from datetime import date

from calc.coupon import get_coupon_calculator_class


class BondCalculator( object ):

    
    def __init__(self, bond , calculation_date = None):
        self.bond = bond
        self.calculation_date = calculation_date or date.today()
        cc =  get_coupon_calculator_class( self.bond.coupon_type )
        self.coupon_calculator = cc(self.bond, self.calculation_date)

