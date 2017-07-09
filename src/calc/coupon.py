"""
Created on  :  01 07, 2017  

@project    : bond-concepts
@author     : alinaved
@description: No description for this module
"""
from abc import ABCMeta, abstractmethod
from datetime import date

from dateutil.relativedelta import relativedelta

from calc.daycounter import get_daycount_calculator_class
from model.bond import Coupon
from model.bond import CouponType


class CouponCalculator( object ):
    __metaclass__ = ABCMeta

    def __init__(self, bond , calculation_date ):
        self._calculation_date = None
        self._coupon_calculator = None
        self.bond = bond
        self.coupon_dates = self._get_coupon_dates()
        self.calculation_date = calculation_date or date.today()
        self.daycount_calculator = get_daycount_calculator_class( self.bond.dc_convention )()

    @property
    def calculation_date(self):
        return self._calculation_date

    @calculation_date.setter
    def calculation_date(self, value):
        if not isinstance(value, date):
            raise ValueError("Need date type, %s provided" % type(value))
        self._calculation_date = value

    def _get_coupon_dates(self):
        def _cpns(m, s, e, res):
            if m:
                s = s + relativedelta(months=m)
                if s < e:
                    res.append(s)
                    return _cpns(m, s, e, res)
            res.append(e)
            return

        frequency = self.coupon_frequency
        coupons = []
        _cpns(frequency, self.bond.issue_date, self.bond.maturity_date, coupons)
        return coupons

    @property
    def next_coupon_date(self):
        return next((e for e in self.coupon_dates if e > self.calculation_date), self.coupon_dates[-1])

    @property
    def prev_coupon_date(self):
        return next((e for e in self.coupon_dates[::-1] if e < self.calculation_date), self.coupon_dates[0])

    @property
    def coupon_frequency(self):
        '''
        Annual coupon frequency
        :return:
        '''
        return int(self.bond.coupon_frequency.value)

    @property
    def next_coupon( self ):
        return Coupon( value = self.get_coupon_value( self.get_next_coupon_pct()), payment_date = self.next_coupon_date )

    def get_coupon_value( self, coupon_pct ):
        return self.bond.par_value * coupon_pct /100

    @abstractmethod
    def get_next_coupon_yearfraction(self):
        """Coupon % can differ base upon day count convention.
           Which determine how much fraction of yearly % is due at this coupon
        """
        pass

    def get_next_coupon_pct(self):
        return self.bond.coupon_rate * self.get_next_coupon_yearfraction()

class FixedCouponCalculator( CouponCalculator ):
    """
    Class to Calculate Fixed coupon type
    """
    def get_next_coupon_yearfraction(self):
        return self.daycount_calculator.year_fraction( self.prev_coupon_date, self.next_coupon_date)

    def get_accrued_interest_pct(self ):
        """
        Returns accrued interest as percentage.
        This is converted into amount with respect to par value.
        :return:
        """
        if self.calculation_date in self.coupon_dates:
            return 0
        else:
            days_since_coupon = self.daycount_calculator.day_count(self.prev_coupon_date, self.calculation_date)
            days_between_coupons = self.daycount_calculator.day_count(self.prev_coupon_date, self.next_coupon_date)
            coupon_fraction  = self.bond.coupon_rate / self.coupon_frequency
            return coupon_fraction * ( days_since_coupon / days_between_coupons )

    def get_accrued_interest_amount(self):
        return self.bond.par_value * self.get_accrued_interest_pct()

class FloatingCouponCalculator( CouponCalculator ):
    """
    Class to calculate floating rate
    """
    def get_next_coupon_pct(self):
        raise NotImplementedError

__CALCULATOR_MAP = (
    (CouponType.FIXED, FixedCouponCalculator ),
    (CouponType.FLOATING, FloatingCouponCalculator),
)

def get_coupon_calculator_class( coupon_type ):
    """
    Factory method to return relevant coupon calculator
    :param coupon_type: Coupon Enum type key
    :return: class of the relevant calculator
    """
    return dict( __CALCULATOR_MAP )[ coupon_type]
