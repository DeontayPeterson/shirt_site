from flask_login import UserMixin
from project import db
from project import login_manager
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.is_admin}')"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


