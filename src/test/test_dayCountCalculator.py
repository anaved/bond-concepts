"""
Created on  :  19 Jul, 2017  

@project    : bond-concepts
@author     : alinaved
@description: No description for this module
"""

from calc.daycounter import Thirty360DayCountCalculator, Actual360DayCountCalculator, ActualActualDayCountCalculator
from datetime import date
from unittest import TestCase

class TestThirty360DayCountCalculator(TestCase):
    def setUp(self):
        self.calculator = Thirty360DayCountCalculator()

    def test_1(self):
        """
        Tests both start and end are less than 30
        :return:
        """
        end   = date(2017,1,28)
        start = date(2017,1,1)
        self.assertEqual( self.calculator.day_count(start,end), 27 )
        end   = date(2017,1,28)
        start = date(2016,1,1)
        self.assertEqual( self.calculator.day_count(start,end), 387 )

    def test_2(self):
        """
        Tests end > 30
        :return:
        """
        end   = date(2017,1,31)
        start = date(2017,1,1)
        self.assertEqual( self.calculator.day_count(start,end), 29 )
        end   = date(2017,3,31)
        start = date(2017,1,1)
        print self.calculator.day_count(start,end)
        self.assertEqual( self.calculator.day_count(start,end), 89 )

    def test_3(self):
        """
        Tests end > 30
        :return:
        """
        end   = date(2017,2,1)
        start = date(2017,1,31)
        self.assertEqual( self.calculator.day_count(start,end), 1 )
        end   = date(2017,3,31)
        start = date(2017,1,31)
        print self.calculator.day_count(start,end)
        self.assertEqual( self.calculator.day_count(start,end), 60 )


class TestActual360DayCountCalculator(TestCase):
    def setUp(self):
        self.calculator = Actual360DayCountCalculator()

    def test_1(self):
        """
        Tests both start and end are less than 30
        :return:
        """
        end   = date(2017,1,28)
        start = date(2017,1,1)
        self.assertEqual( self.calculator.day_count(start,end), 27 )
        end   = date(2017,1,28)
        start = date(2016,1,1)
        self.assertEqual( self.calculator.day_count(start,end), 387 )

    def test_2(self):
        """
        Tests end > 30
        :return:
        """
        end   = date(2017,1,31)
        start = date(2017,1,1)
        self.assertEqual( self.calculator.day_count(start,end), 29 )
        end   = date(2017,3,31)
        start = date(2017,1,1)
        print self.calculator.day_count(start,end)
        self.assertEqual( self.calculator.day_count(start,end), 89 )

    def test_3(self):
        """
        Tests end > 30
        :return:
        """
        end   = date(2017,2,1)
        start = date(2017,1,31)
        self.assertEqual( self.calculator.day_count(start,end), 1 )
        end   = date(2017,3,31)
        start = date(2017,1,31)
        print self.calculator.day_count(start,end)
        self.assertEqual( self.calculator.day_count(start,end), 60 )

class TestActualActualDayCountCalculator(TestCase):
    def setUp(self):
        self.calculator = ActualActualDayCountCalculator()

    def test_1(self):
        """
        Tests both start and end are less than 30
        :return:
        """
        end   = date(2017,1,28)
        start = date(2017,1,1)
        self.assertEqual( self.calculator.day_count(start,end), 27 )
        end   = date(2017,1,28)
        start = date(2016,1,1)
        self.assertEqual( self.calculator.day_count(start,end), 387 )

    def test_2(self):
        """
        Tests end > 30
        :return:
        """
        end   = date(2017,1,31)
        start = date(2017,1,1)
        self.assertEqual( self.calculator.day_count(start,end), 29 )
        end   = date(2017,3,31)
        start = date(2017,1,1)
        print self.calculator.day_count(start,end)
        self.assertEqual( self.calculator.day_count(start,end), 89 )

    def test_3(self):
        """
        Tests end > 30
        :return:
        """
        end   = date(2017,2,1)
        start = date(2017,1,31)
        self.assertEqual( self.calculator.day_count(start,end), 1 )
        end   = date(2017,3,31)
        start = date(2017,1,31)
        print self.calculator.day_count(start,end)
        self.assertEqual( self.calculator.day_count(start,end), 60 )