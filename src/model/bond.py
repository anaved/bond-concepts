"""
Created on Jun 26, 2017

@author: alinaved
"""
from locale import currency

from enum import Enum
from sqlalchemy import Column, Date, Integer, String, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_enum34 import EnumType
from sqlalchemy.orm import relationship

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
    ACTUAL_360    = 'Actual/360'
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
    name = Column(String)
    issuer_id = Column(Integer, ForeignKey('issuer.id'))
    par_value = Column(Numeric, nullable=False)
    coupon_rate =  Column(Numeric)
    issue_date  = Column(Date, nullable=False)
    maturity_date  = Column(Date, nullable=False)
    coupon_frequency = Column(EnumType(CouponFrequency), nullable=False)
    coupon_type = Column(EnumType(CouponType), nullable=False)
    dc_convention = Column(EnumType(DayCountConvention), nullable=False)

    issuer = relationship("Issuer", back_populates="bonds")

class Coupon( Base ):
    '''
    Coupon properties of a bond
    '''
    __tablename__ = 'coupon'
    id   = Column(Integer, primary_key=True)
    value = Column(Numeric, nullable=False)
    payment_date = Column(Date, nullable=False)
    bond_id = Column(Integer, ForeignKey('bond.id'))

    bond = relationship("Bond", back_populates="coupons")

    def __repr__(self):
        return "Coupon value: %s, payment date %s" % (self.value, self.payment_date)

class Price( Base ):
    __tablename__ = 'price'
    id      = Column(Integer, primary_key=True)
    price     = Column(Numeric, nullable=False)
    date      = Column(Date, nullable=False)
    bond_id = Column(Integer, ForeignKey('bond.id'))

    bond = relationship("Bond", back_populates="prices")

class Quote( Base ):
    __tablename__ = 'quote'
    id      = Column(Integer, primary_key=True)
    bid     = Column(Numeric, nullable=False)
    ask     = Column(Numeric, nullable=False)
    bond_id = Column(Integer, ForeignKey('bond.id'))

    bond = relationship("Bond", back_populates="quotes")

Issuer.bonds = relationship( "Bond", order_by=Bond.id, back_populates="issuer")
Bond.coupons = relationship( "Coupon", order_by=Coupon.id, back_populates="bond")
Bond.prices = relationship( "Price", order_by=Price.id, back_populates="bond")
Bond.quotes = relationship( "Quote", order_by=Quote.id, back_populates="bond")

if __name__ == '__main__':
    Base.metadata.create_all(Engine)
