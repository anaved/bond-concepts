from unittest import TestCase
from test.TestBase import TestBondBase
from lib.fixedincome.securities.bond import BondCalculator

class TestBondCalculator(TestCase, TestBondBase):

    def setUp(self):
        super(TestBondCalculator, self)._setUp()
        self.calculator = BondCalculator( self.govtBulletBond )

    def test_getCouponValue(self):
        self.assertEqual(self.calculator.getCouponValue(), 50)

    def test_getParValue(self):
        self.fail()

    def test_get_coupons(self):
        print self.calculator.coupon_dates

    def test_getNextCouponDate(self):
        self.fail()
