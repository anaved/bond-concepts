"""
Created on Jun 26, 2017

@author: alinaved
"""
from locale import currency

from enum import Enum
from sqlalchemy import Column, Date, Integer, String, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_enum34 import EnumType

from model.base import Base, Engine


class IssuerType( Enum ):
    GOVERNMENT = 'Government'
    CORPORATE  = 'Corporate'

class Issuer( Base ):
    __tablename__ = 'issuer'
    id   = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(EnumType(IssuerType), nullable=False)

class CouponType( Enum ):
    FIXED = 'Fixed'
    FLOATING = 'Floating'
    
class DayCountConvention( Enum ):
    ACTUAL_ACTUAL = 'Actual/Actual'
    THIRTY_360    = '30/360'
    
class CouponFrequency( Enum ):
    ANNUAL      = '12'
    SEMIANNUAL  = '6'
    QUARTERLY   = '3'
    MONTHLY     = '1'
    AT_MATURITY = '0'

class Bond(Base):
    '''
    classdocs
    '''
    __tablename__ = 'bond'
    id   = Column(Integer, primary_key=True)
    isin = Column(String)    
    par_value = Column(Numeric, nullable=False)
    coupon_rate =  Column(Numeric)
    issue_date  = Column(Date, nullable=False)
    maturity_date  = Column(Date, nullable=False)
    coupon_frequency = Column(EnumType(CouponFrequency), nullable=False)
    coupon_type = Column(EnumType(CouponType), nullable=False)
    dc_convention = Column(EnumType(DayCountConvention), nullable=False)
    issuer = Column(Integer, ForeignKey('issuer.id'))
    #TODO bondcalculator would be a hybrid method property
    # coupons would be a property returned via calculator

class Coupon( Base ):
    '''
    Coupon properties of a bond
    '''
    __tablename__ = 'coupon'
    id   = Column(Integer, primary_key=True)
    value = Column(Numeric, nullable=False)
    payment_date = Column(Date, nullable=False)
    bond = Column(Integer, ForeignKey('bond.id'))

class BondQuote( Base ):    
    __tablename__ = 'quote'
    id      = Column(Integer, primary_key=True)
    bid     = Column(Numeric, nullable=False)
    ask     = Column(Numeric, nullable=False) 
    bond_id = Column(Integer, ForeignKey('bond.id'))
    
if __name__ == '__main__':
    Base.metadata.create_all(Engine)   
