from datetime import date

from model.bond import CouponType, DayCountConvention, \
    CouponFrequency, Bond


class TestBondBase(object):
    BASE_BOND = { 'isin'        : 'TEST123',
                  'par_value'   : 1000,
                  'coupon_rate' : 5,
                  'issue_date'  : date(2015,1,1),
                  'maturity_date' : date(2020,12,31),
                  'coupon_frequency' : CouponFrequency.ANNUAL,
                  'coupon_type' : CouponType.FIXED,
                  'dc_convention' : DayCountConvention.ACTUAL_ACTUAL,
                }
    def get_govie_bullet(self):
        """
        Instantiate and return a test Govie Bond
        :return: Bond
        """
        return  Bond( ** self.BASE_BOND )

