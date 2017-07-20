"""
Created on  :  01 Jul, 2017  

@project    : bond-concepts
@author     : alinaved
@description: Module to calculate fraction of year based upon day count convention.
"""
from abc import ABCMeta, abstractmethod, abstractproperty
from model.bond import DayCountConvention
import calendar
from datetime import date

class DayCountCalculator( object ):
    __metaclass__ = ABCMeta

    @abstractproperty
    def denominator(self):pass

    @abstractmethod
    def _get_day_count(self, start, end):pass

    def day_count(self, start, end):
        if start == end :
            return 0
        elif start > end:
            return - self._get_day_count(end, start)
        else:
            return self._get_day_count(start, end)

    def year_fraction(self, start, end):
        return self.day_count(start, end) / self.denominator

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
    def denominator(self):
        return 360

    def _get_day_count(self, start, end):

        return 360*(end.year - start.year)\
               + 30*(end.month - start.month -1)\
               + max(0, 30 - start.day)\
               + min(30, end.day)

class Actual360DayCountCalculator( DayCountCalculator ):
    """
    Actual difference between dates is calculated, but year is considered
    to be of 360 days.
    This convention is used mostly for sub year calculation
    """

    @property
    def denominator(self):
        return 360

    def _get_day_count(self, start, end):
        return ( end - start ).days


class ActualActualDayCountCalculator( DayCountCalculator ):
    """
    Actual difference between dates is calculated, also the difference in year.
    Used in US treasury bonds
    """

    @property
    def denominator(self):
        #Not actual value
        return 365

    def _get_day_count(self, start, end):
        return ( end - start ).days

    def year_fraction(self, start, end):
        year_days = lambda x: 366 if calendar.isleap(x) else 365
        if start.year == end.year:
            return self.day_count(start, end) / year_days( start.year )
        else:
            return (date(start.year,12,31) - start ).days/year_days(start.year) + (end - date(end.year,1,1) ).days/year_days(end.year)

__CALCULATOR_MAP = (
    (DayCountConvention.THIRTY_360, Thirty360DayCountCalculator ),
    (DayCountConvention.ACTUAL_360, Actual360DayCountCalculator ),
    (DayCountConvention.ACTUAL_ACTUAL, ActualActualDayCountCalculator ),

)
def get_daycount_calculator_class(convention_type):
    """
    Factory method to return appropriate calculator for passed convention
    :param convention_type:
    :return:
    """
    return dict( __CALCULATOR_MAP )[ convention_type]
