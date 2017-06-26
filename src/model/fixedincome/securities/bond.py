'''
Created on Jun 26, 2017

@author: alinaved
'''
from enum import Enum
from model.base import Base
from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy_enum34 import EnumType

class CouponType( Enum ):
    FIXED = 'Fixed'
    VARIABLE = 'Variable'
    ZERO_COUPON = 'Zero Coupon'
    
class DayCountConvention( Enum ):
    ACTUAL_ACTUAL = 'Actual/Actual'
    THIRTY_360    = '30/360'
    
class CouponFrequency( Enum ):    
    SEMIANNUAL  = 'Semi-annual'
    QUARTERLY   = 'Quarterly'
    MONTHLY     = 'Monthly'
    AT_MATURITY = 'At Maturity'
        
class Coupon( Base ):
    '''
    Coupon properties of a bond
    '''
    __tablename__ = 'coupon'
    id   = Column(Integer, primary_key=True)
    start_date  = Column(Date, nullable=False)
    end_data    = Column(Date, nullable=False)
    frequency   = Column(Date, nullable=False)
    type = Column(EnumType(CouponType), nullable=False)
    dc_convention = Column(EnumType(DayCountConvention), nullable=False)
    
    
class Bond(object):
    '''
    classdocs
    '''
    __tablename__ = 'bond'
    id   = Column(Integer, primary_key=True)
    isin = Column(String)
    coupon_id = Column(Integer, ForeignKey('coupon.id'))


        