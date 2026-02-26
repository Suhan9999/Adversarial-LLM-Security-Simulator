from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime, timezone

engine = create_engine("sqlite:///simulation.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()
ground_truth = Column(String)

class SimulationLog(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime(timezone=True),
                       default=lambda: datetime.now(timezone.utc))
    round = Column(Integer)
    prompt = Column(String)
    ground_truth = Column(String)
    classification = Column(String)
    confidence = Column(Float)
    risk_score = Column(Float)
    attack_success = Column(Boolean)
    incident_flag = Column(Boolean)

Base.metadata.create_all(engine)