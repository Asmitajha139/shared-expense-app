"""
/backend/app/models/user.py

SQLAlchemy Database Schema Model for the 'users' table.
Responsibility: Defines the database columns, indices, and constraints for user accounts.
Relationships omitted at this stage as per design guidelines.

Clean Architecture Layer: Domain Entities / Database Mapping
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base


class User(Base):
    """
    User Table Schema.
    Represents system participants. Enforces system identity constraints at the database level.
    """
    __tablename__ = "users"

    # Primary Key - Unique serial identifier for quick primary key index keys.
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Human display name of the flatmate (e.g., 'Aisha', 'Rohan')
    name = Column(String(100), nullable=False)

    # Unique email address used for secure logins.
    # index=True generates a B-Tree index structure enabling O(log N) lookup queries.
    email = Column(String(255), nullable=False, unique=True, index=True)

    # Secure salted bcrypt hash of the user's password. Stored in fixed-length string space block.
    password_hash = Column(String(255), nullable=False)

    # Automatic UTC auditing timestamp marking when the user registered in the system.
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return f"<User id={self.id}, name='{self.name}', email='{self.email}'>"
