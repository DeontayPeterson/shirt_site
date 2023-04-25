from project import db, app
from project.user import User

# Script to create an admin account. 
def create_admin(username: str, password: str) -> None:
    admin = User(username=username, password=password, is_admin=True)
    admin.set_password(password)
    db.session.add(admin) 
    db.session.commit()

    print(f"Admin created: {username}")


if __name__ == "__main__":
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    with app.app_context():
        create_admin(username=username, password=password)