"""
Created on  :  01 Jul, 2017  

@project    : bond-concepts
@author     : alinaved
@description: Module to calculate fraction of year based upon day count convention
"""
from abc import ABCMeta, abstractmethod, abstractproperty

from model.bond import DayCountConvention


class DayCountCalculator( object ):
    __metaclass__ = ABCMeta

    @abstractproperty
    def numerator(self): pass

    @abstractproperty
    def denominator(self):pass

    @abstractmethod
    def day_count(self):pass

    def year_fraction(self):
        return self.day_count() / self.denominator

class Thirty360DayCountCalculator( DayCountCalculator ):
    """
    A month is considered of 30 days and a year is of 360 days.
    ISDA recommended method for day count is
    360(y2-y1)+30(m2-m1-1)+max(0,30-d1)+min(30,d2)
    * Take year diff
    * Take month diff + 1 month to be adjusted by date
    * Since every month is 30 and reduce d1 from it, and take
    max with 0 in case result is negative ( days to 30 )
    * days in d2, min if more than 30
    """
    @property
    def numerator(self):
        return 30

    @property
    def denominator(self):
        return 360

    def day_count(self, start, end):
        if end <= start:
            return 0
        return 360*(end.year - start.year)\
               + 30*(end.month - start.month -1)\
               + max(0, 30 - start.day)\
               + min(30, end.day)

__CALCULATOR_MAP = (
    (DayCountConvention.THIRTY_360, Thirty360DayCountCalculator ),
)
def get_daycount_calculator_class(convention_type):
    """
    Factory method to return appropriate calculator for passed convention
    :param convention_type:
    :return:
    """
    return dict( __CALCULATOR_MAP )[ convention_type]
