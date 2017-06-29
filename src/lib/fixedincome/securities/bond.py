'''
Created on Jun 26, 2017

@author: alinaved
'''
from dateutil import relativedelta
from datetime import date

class BondCalculator( object ):
    def __init__(self, bond , calculation_date = None,*args, **kwargs):
        self.bond = bond
        self.calculation_date = calculation_date or date.today()

    @property
    def calculation_date(self):
        return self._calculation_date

    @calculation_date.setter
    def calculation_date(self, value):
        if not isinstance( value, date):
            raise ValueError("Need date type, %s provided"% type(value))
        self._calculation_date = value

    def get_coupon_value(self):
        return ( 100 * self.bond.interest_rate / self.bond.par_value )

    @property
    def coupons(self):
        frequency = self.get_coupon_frequency()
        coupons = []
        coupon = self.bond.maturity_date
        #atleast one coupon will be there on the maturity date
        coupons.append(coupon)
        while coupon > self.bond.issue_date:
            coupon = coupon - relativedelta( months = frequency)
            coupons.append(coupon)
        return coupons

    def get_next_coupon_date(self):
        raise NotImplementedError

    def get_coupon_frequency(self):
        '''
        Annual coupon frequency
        :return:
        '''
        return int(self.bond.coupon.frequency.value)


