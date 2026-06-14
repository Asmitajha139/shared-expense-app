"""
/backend/app/models/group.py

SQLAlchemy Database Schema Model for the 'groups' table.
Responsibility: Defines columns, keys, and metadata for shared expense containers.
Relationships omitted at this stage as per design guidelines.

Clean Architecture Layer: Domain Entities / Database Mapping
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base


class Group(Base):
    """
    Group Table Schema.
    Represents flatmate environments or trips containing distinct expenses and memberships.
    """
    __tablename__ = "groups"

    # Primary Key - Unique serial identifier with B-Tree primary index keys.
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    # Human-readable title identifying the group (e.g., 'Flat No. 4', 'Goa Trip 2026')
    name = Column(String(100), nullable=False)

    # Optional descriptive summary of the group's purpose.
    description = Column(String(255), nullable=True)

    # Foreign Key referring back to the specific administrator/creator who initiated the group.
    # Enforces database-level referential integrity against the users table.
    created_by = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Audit column record tracking when the group was registered in UTC.
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return f"<Group id={self.id}, name='{self.name}', created_by={self.created_by}>"
