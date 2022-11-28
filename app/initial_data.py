#!/usr/bin/env python3
from getpass import getpass

from app.db.session import db_session
from app.db.crud.user import create_user
from app.db.schemas.user import UserCreate


def init() -> None:
    email = input("Super Administrator Account Email: ")
    if not email or "@" not in email:
        print(" Malformed email address!")
        return
    password = getpass("Password: ")
    if len(password) < 8:
        print("Password length must be at least 8 characters!")
        return
    repeated_password = getpass("Repeat password: ")
    if password != repeated_password:
        print("Passwords do not match!")
        return

    with db_session() as db:
        create_user(
            db,
            UserCreate(
                email=email,
                password=password,
                is_active=True,
                is_superuser=True,
            ),
        )


if __name__ == "__main__":
    print("Creating superuser")
    init()
    print("Superuser created")
