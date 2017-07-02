from unittest import TestCase
from test.TestBase import TestBondBase
from calc.fixedincome.securities.bond import BondCalculator


class TestBondCalculator(TestCase, TestBondBase):
    def setUp(self):
        self.bond = self.get_govie_bullet()
        self.bond_calculator = BondCalculator(self.bond)

    def test_getCouponValue(self):
        self.assertEqual(self.calculator.getCouponValue(), 50)

    def test_getParValue(self):
        self.fail()

    def test_get_coupons(self):
        self.assertEqual(len(self.calculator.coupon_dates), 6)

    def test_getNextCouponDate(self):
        print self.bond_calculator.coupon_calculator.coupon_dates
        print self.bond_calculator.coupon_calculator.next_coupon

    def test_calculation_date(self):
        self.fail()
