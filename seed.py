from app import app
from config import db
from models import Hero, Power, HeroPower

with app.app_context():
    db.drop_all()
    db.create_all()

    # Heroes
    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero2 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")
    hero3 = Hero(name="Doreen Green", super_name="Squirrel Girl")

    # Powers
    power1 = Power(
        name="super strength",
        description="gives the wielder super-human strengths"
    )
    power2 = Power(
        name="flight",
        description="gives the wielder the ability to fly through the skies at supersonic speed"
    )
    power3 = Power(
        name="super human senses",
        description="allows the wielder to use her senses at a super-human level"
    )

    # HeroPowers
    hp1 = HeroPower(hero=hero1, power=power2, strength="Strong")
    hp2 = HeroPower(hero=hero3, power=power1, strength="Average")

    db.session.add_all([hero1, hero2, hero3, power1, power2, power3, hp1, hp2])
    db.session.commit()
