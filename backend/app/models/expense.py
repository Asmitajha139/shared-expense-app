"""
/backend/app/models/expense.py

SQLAlchemy Database Schema Model for the 'expenses' table.
Responsibility: Defines columns, foreign keys, and constraints representing expense records.
Supports precise Decimal amount limits and custom timestamps. No relationships yet.

Clean Architecture Layer: Domain Entities / Database Mapping
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey
from app.database import Base


class Expense(Base):
    """
    Expense Table Schema.
    Represents financial expenses incurred by a group member. Stores details, precise amount,
    and references to the related user and group.
    """
    __tablename__ = "expenses"

    # Primary Key - Unique serial identifier with B-Tree indices.
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    # Referential link to the group context in which this expense was incurred.
    group_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"), nullable=False)

    # Referential link to the specific user who paid for the expense upfront.
    paid_by = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Short naming tag of the expense transaction (e.g. 'Airport cab', 'March Rent')
    title = Column(String(255), nullable=False)

    # Supporting details or remarks summarizing the purchase.
    description = Column(String(500), nullable=True)

    # Financial amount containing up to 10 total digits and 2 decimal places.
    # Maps natively to decimal.Decimal to guarantee precise calculations without float rounding anomalies.
    amount = Column(Numeric(10, 2), nullable=False)

    # Timeline date when the actual event or transaction occurred (e.g., matching the CSV date).
    expense_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Timestamp tracking when the entry was officially stored in the database.
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return (
            f"<Expense id={self.id}, title='{self.title}', amount={self.amount}, "
            f"group_id={self.group_id}, paid_by={self.paid_by}>"
        )
