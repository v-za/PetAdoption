from flask import make_response, abort
from userAccount_config import userDB
from models import User, UserSchema

def read_all():
	user = User.query.order_by(User.userFirst).all()
	user_schema = UserSchema(many=True)
	data = user_schema.dump(user)
	return data

def read_one(userID):

    user = User.query.filter(User.userID == userID).one_or_none()

    if user is not None:

        user_schema = UserSchema()
        data = user_schema.dump(user).data
        return data
    else:
        abort(
            404,
            "User not found for ID: {userID}".format(userID=userID),
        )

def create(user):

    userName = USER.get("userName")
    userFirst = USER.get("userFirst")
    userLast = USER.get("userLast")
    userPhone = USER.get("userPhone")
    userEmail = USER.get("userEmail")
    userAddress = USER.get("userAddress")
    userAddress2 = USER.get("userAddress2")
    userState = USER.get("userState")
    userZip = USER.get("userZip")


    existing_user = (
        User.query.filter(User.userName == userName)
        .filter(User.userFirst == userFirst)
        .filter(User.userLast == userLast)
        .filter(User.userPhone == userPhone)
        .filter(User.userEmail == userEmail)
        .filter(User.userAddress == userAddress)
        .filter(User.userAddress2 == userAddress2)
        .filter(User.userState == userState)
        .filter(User.userZip == userZip)
        .one_or_none()
    )

    if existing_user is None:

        schema = UserSchema()
        new_user = schema.load(user, session=db.session).data

        db.session.add(new_user)
        db.session.commit()

        data = schema.dump(new_user).data

        return data, 201

    else:
        abort(
            409,
            "{UserName} already exists".format(
                UserName=userName
            ),
        )

def update(userID, userName):

    update_users = User.query.filter(
        User.userID == userID
    ).one_or_none()

    if update_users is not None:

        schema = UserSchema()
        update = schema.load(userName, session=db.session).data

        update.userID = update_users.userID

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_users).data

        return data, 200

    else:
        abort(
            404,
            "User not found for ID: {userID}".format(userID=userID),
        )

def delete(userID):
    user = User.query.filter(User.userID == userID).one_or_none()

    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return make_response(
            "User {userID} is deleted".format(userID=userID), 200
        )
    else:
        abort(
            404,
            "User not found for ID: {userID}".format(userID=userID),
)
