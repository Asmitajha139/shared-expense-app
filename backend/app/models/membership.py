"""
/backend/app/models/membership.py

SQLAlchemy Database Schema Model for the 'memberships' table.
Responsibility: Maps users to groups dynamically with strict temporal audits.
Maintains exact timestamps for when users join or leave groups, enabling
correct historical balance calculations.

Clean Architecture Layer: Domain Entities / Database Mapping
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base


class Membership(Base):
    """
    Membership Table Schema.
    Acts as a rich many-to-many bridge between Users and Groups. Supports
    historical membership records with time-bound states.
    """
    __tablename__ = "memberships"

    # Primary Key - Unique auto-incrementing serial integer index keys.
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    # Core Foreign Key linking directly to the specific user account.
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Core Foreign Key linking directly to the parent group.
    group_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"), nullable=False)

    # Timestamp marking exactly when the user joined the group (or when group created).
    # Critical for resolving expenses dated before arrival.
    joined_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Timestamp representation of when the user officially departed from the group workspace.
    # Nullable, since active members have no departure date.
    # Critical for resolving expenses dated after departure.
    left_at = Column(DateTime, nullable=True)

    # Status indicator (e.g., "active", "left", "invited"). Enforced via string flags.
    status = Column(String(20), nullable=False, default="active")

    def __repr__(self) -> str:
        return (
            f"<Membership id={self.id}, user_id={self.user_id}, "
            f"group_id={self.group_id}, status='{self.status}', "
            f"joined_at={self.joined_at}, left_at={self.left_at}>"
        )
