from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from backend import db
from sqlalchemy.orm import relationship



class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    date_posted = Column(DateTime, nullable=False, default=datetime.utcnow)
    content = Column(String(1000), nullable=False)
    user_id = Column(Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
