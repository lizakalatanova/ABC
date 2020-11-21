from Manager.DatabaseManager import DatabaseManager
from app import db
db_manager = DatabaseManager(db)
db_manager.add_interval(interval="15:25 - 17:00")
