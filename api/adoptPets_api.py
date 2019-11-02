from flask import make_response, abort
from config import adoptDB
from models import Adopt, AdoptSchema

def read_all():
        adopt = Adopt.query.order_by(Adopt.adoptName).all()
        adopt_schema = AdoptSchema(many=True)
        data = adopt_schema.dump(adopt).data
        return data


def read_one(adoptID):

    adopt = Adopt.query.filter(Adopt.adoptID == adoptID).one_or_none()

    if adopt is not None:

        adopt_schema = AdoptSchema()
        data = adopt_schema.dump(adopt).data
        return data
    else:
            abort(
            404,
            "Pet not found for id: {adoptID}".format(adoptID=adoptID),
        )

def create(adopt):

    adoptName = ADOPT.get("adoptName")
    adoptType = ADOPT.get("adoptType")
    adoptBreed = ADOPT.get("adoptBreed")
    adoptDesc = ADOPT.get("adoptDesc")
    adoptAppearance = ADOPT.get("adoptAppearance")
    adoptGender = ADOPT.get("adoptGender")
    adoptSize = ADOPT.get("adoptSize")

    existing_pet = (
        Adopt.query.filter(Adopt.adoptName == adoptName)
        .filter(Adopt.adoptType == adoptType)
        .filter(Adopt.adoptBreed == adoptBreed)
        .filter(Adopt.adoptDesc == adoptDesc)
        .filter(Adopt.adoptAppearance == adoptAppearance)
        .filter(Adopt.adoptGender == adoptGender)
        .filter(Adopt.adoptSize == adoptSize)
        .one_or_none()
    )

    if existing_pet is None:

        schema = AdoptSchema()
        new_pet = schema.load(adopt, session=db.session).data

        db.session.add(new_pet)
        db.session.commit()

        data = schema.dump(new_pet).data

        return data, 201

    else:
        abort(
            409,
            "{adoptName} already exists".format(
                adoptName=adoptName
            ),
        )

def update(adoptID, adoptName):

    update_pet = Adopt.query.filter(
        Adopt.adoptID == adoptID
    ).one_or_none()

    if update_pet is not None:

        schema = AdoptSchema()
        update = schema.load(adoptName, session=db.session).data

        update.adoptID = update_pet.adoptID

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_pet).data

        return data, 200

    else:
        abort(
            404,
            "Pet not found for ID: {adoptID}".format(adoptID=adoptID),
        )

def delete(adoptID):
    adopt = Adopt.query.filter(Adopt.adoptID == adoptID).one_or_none()

    if adopt is not None:
        db.session.delete(adopt)
        db.session.commit()
        return make_response(
            "Pet {adoptID} is deleted".format(adoptID=adoptID), 200
        )
    else:
        abort(
            404,
            "Pet not found for ID: {adoptID}".format(adoptID=adoptID),
)
