"""
/backend/app/models/settlement.py

SQLAlchemy Database Schema Model for the 'settlements' table.
Responsibility: Defines columns, foreign keys, and constraints representing settlement/payback entries.
Supports precise Decimal amount limits. No relationships/backrefs yet.

Clean Architecture Layer: Domain Entities / Database Mapping
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey
from app.database import Base


class Settlement(Base):
    """
    Settlement Table Schema.
    Represents direct payback transactions from a debtor (payer) to a creditor (receiver) inside a group.
    """
    __tablename__ = "settlements"

    # Primary Key - Unique serial identifier with B-Tree auto-indexing.
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    # Core relationship link to the specific group container context.
    group_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"), nullable=False)

    # The user who is paying back money (making the settlement payment).
    payer_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # The user who is receiving the payback money (the outstanding creditor).
    receiver_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Financial settlement amount containing up to 10 total digits and 2 decimal places.
    # Maps natively to decimal.Decimal to safeguard against precision rounding errors.
    amount = Column(Numeric(10, 2), nullable=False)

    # Timeline date when the actual payment transaction took place or was initiated.
    settlement_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Optional descriptive remark (e.g., 'GPay reimbursement for Goa villa').
    note = Column(String(255), nullable=True)

    # Audit column recording when the settlement details were officially stored.
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return (
            f"<Settlement id={self.id}, group_id={self.group_id}, "
            f"payer_id={self.payer_id}, receiver_id={self.receiver_id}, amount={self.amount}>"
        )
