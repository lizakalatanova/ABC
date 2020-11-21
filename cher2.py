from Manager.DatabaseManager import DatabaseManager
from app import db
db_manager = DatabaseManager(db)
db_manager.add_group(groups='БФИ1801')
