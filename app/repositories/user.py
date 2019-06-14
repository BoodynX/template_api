from typing import Union

from app.entities.user import User
from app.framework.database import db
from app.models.user import UserModel


class UserRepository:
    _model = UserModel

    @classmethod
    def create(cls, user: User) -> None:
        user_model = cls._model(username=user.username, password=user.password)
        db.session.add(user_model)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username: str) -> Union[User, None]:
        user = cls._model.query.filter_by(username=username).first()
        return cls._make_entity(user)

    @classmethod
    def find_by_id(cls, _id: int) -> Union[User, None]:
        user = cls._model.query.filter_by(id=_id).first()
        return cls._make_entity(user)

    @classmethod
    def _make_entity(cls, user: UserModel) -> Union[User, None]:
        if not user:
            return None
        return User(id_=user.id, username=user.username, password=user.password)
