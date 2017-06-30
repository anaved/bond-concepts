from model.fixedincome.securities.bond import IssuerType, Issuer,\
                                              CouponRate, DayCountConvention,\
                                              CouponFrequency, Coupon, Bond

from dateutil import relativedelta, parser
from datetime import date

class TestBondBase(object):
    BASE_BOND = { 'issuer_type' : IssuerType.GOVERNMENT,
                  'coupon_rate' : CouponRate.FIXED,
                }
    def _setUp(self):
        self.govtBulletBond = self._setupGovtBulletBond()
        

    def _setupGovtBulletBond(self):
        issuerType = IssuerType.GOVERNMENT
        issuer = Issuer( name = 'TestIssuer', type = issuerType )
        couponRateType = CouponRate.FIXED
        dayCountConvention = DayCountConvention.ACTUAL_ACTUAL
        couponFrequency = CouponFrequency.ANNUAL
        return Bond( isin = 'TEST123',
                   par_value = 1000, coupon_rate = 5,
                   issue_date=parser.parse('01/01/2000'),
                   maturity_date=parser.parse('12/31/2005'),
                   coupon_frequency=couponFrequency,
                   coupon_rate_type = couponRateType,
                   dc_convention = dayCountConvention,
                   issuer = issuer)
