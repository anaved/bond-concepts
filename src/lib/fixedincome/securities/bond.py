'''
Created on Jun 26, 2017

@author: alinaved
'''
from dateutil.relativedelta import relativedelta
from datetime import date

class BondCalculator( object ):
    
    
    def __init__(self, bond , calculation_date = None ):
        self._calculation_date = None
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
    def coupon_dates(self):
        def _cpns( m, s, e, res):
            if m:
                s = s +  relativedelta( months = m)
                if s < e:
                    res.append( s )
                    return _cpns( m, s, e, res )
            res.append( e )
            return
                
        frequency = self.get_coupon_frequency()
        coupons = []
        _cpns( frequency, self.bond.issue_date, self.bond.maturity_date, coupons )    
        return coupons

    def get_next_coupon_date(self):
        raise NotImplementedError

    def get_coupon_frequency(self):
        '''
        Annual coupon frequency
        :return:
        '''
        return int(self.bond.coupon_frequency.value)


