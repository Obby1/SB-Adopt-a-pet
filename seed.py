"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

Pet.query.delete()

# DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"
# createdb pets_db
# python3 seed.py
# cd SQL/SQLAlchemy/Pets/

p1 = Pet(name = "Milo", species = "Bishon", age="14", notes="very paranoid")
p2 = Pet(name = "Harper", species = "Mini Golden Doodle", age="1")
db.session.add_all([p1, p2])
db.session.commit()