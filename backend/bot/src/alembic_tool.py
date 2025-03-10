from alembic import command
from alembic.config import Config


def create_new_revision(name_revision: str):
    alembic_cfg = Config("alembic.ini")
    try:
        command.revision(alembic_cfg, message=name_revision, autogenerate=True)
        print(f"Alembic revision created successfully: {name_revision}")
    except Exception as e:
        print(f"Error creating Alembic revision: {e}")


def upgrade_database():
    alembic_cfg = Config("alembic.ini")
    try:
        command.upgrade(alembic_cfg, revision="head")
        print(f"Alembic upgrade successfully")
    except Exception as e:
        print(f"Error upgrade Alembic revision: {e}")


def downgrade_database(revision: str = "-1"):
    alembic_cfg = Config("alembic.ini")
    try:
        command.downgrade(config=alembic_cfg, revision=revision)
        print(f"Alembic downgrade successfully")
    except Exception as e:
        print(f"Error downgrade Alembic revision: {e}")


if __name__ == "__main__":
    # create_new_revision(name_revision="init migration")
    upgrade_database()
    # downgrade_database()