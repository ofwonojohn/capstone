from app import db


class Participant(db.Model):
    __tablename__ = "participants"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    affiliation = db.Column(db.String(100), nullable=True)  # CS, SE, etc.
    specialization = db.Column(db.String(100), nullable=True)  # Software, Hardware, etc.
    cross_skill_trained = db.Column(db.Boolean, default=False)
    institution = db.Column(db.String(100), nullable=True)  # SCIT, CEDAT, etc.

    # Relationships
    projects = db.relationship("ProjectParticipant", back_populates="participant")

    def __repr__(self):
        return f"<Participant {self.full_name}>"