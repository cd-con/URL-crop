from app import dtime
import sqlalchemy as sa

class TokensModel(sa.Model):

    __tablename__ = "urls"

    """
    origin - изначальная ссылка
    token - сокращённая ссылка, не более 8 символов
    created - дата и время создания ссылки
    ow
    """
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    origin = sa.Column(sa.String(length=512), nullable=False)
    token = sa.Column(sa.String(length=8), nullable=False, unique=True, index=True)
    created = sa.Column(sa.DateTime, nullable=False, default=dtime.now())
    owner_ip = sa.Column(sa.String(length=15), index=True)
    immune = sa.Column(sa.Boolean, nullable=False, default=False, index=True)

    # Метрика
    clicks = sa.Column(sa.BIGINT, nullable=False, default=0)

    # Timestamp последнего посещения ссылки для удаления неликвидных
    last_click = sa.Column(sa.DateTime, nullable=False, default=dtime.now(), index=True)

class BlockedUsersModel(sa.Model):
    __tablename__ = "banned"
    
    """
    ip - ip пользователя
    blocked - дата и время блокировки
    cause - причина блокировки
    """
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    ip = sa.Column(sa.String(length=15), unique=True, index=True, nullable=False)
    blocked = sa.Column(sa.DateTime, nullable=False, default=dtime.now())
    cause = sa.Column(sa.String(length=127))