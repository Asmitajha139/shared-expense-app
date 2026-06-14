"""
/backend/app/models/expense_share.py

SQLAlchemy Database Schema Model for the 'expense_shares' table.
Responsibility: Maps individual split balances owed by debtors for each expense.
Supports highly precise Decimal valuations. No relationships/backrefs yet.

Clean Architecture Layer: Domain Entities / Database Mapping
"""

from sqlalchemy import Column, Integer, Numeric, ForeignKey
from app.database import Base


class ExpenseShare(Base):
    """
    ExpenseShare Table Schema.
    Represents a specific user's share of responsibility for a given expense.
    """
    __tablename__ = "expense_shares"

    # Primary Key - Unique serial identifier with local index keys.
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    # Core relationship link to the parent expense transaction.
    expense_id = Column(Integer, ForeignKey("expenses.id", ondelete="CASCADE"), nullable=False)

    # Core relationship link to the specific user/debtor responsible for this portion.
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Owed share amount (calculated from split logic).
    # Uses Numeric(10, 2) to match precise Decimal standards, avoiding float errors.
    share_amount = Column(Numeric(10, 2), nullable=False)

    def __repr__(self) -> str:
        return (
            f"<ExpenseShare id={self.id}, expense_id={self.expense_id}, "
            f"user_id={self.user_id}, share_amount={self.share_amount}>"
        )
