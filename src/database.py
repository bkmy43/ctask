from orator import DatabaseManager, Model, Schema
import settings as s

config = {
    'pg-docker': {
        'driver': 'postgres',
        'host': s.PG_HOST,
        'port': s.PG_PORT,
        'database': s.PG_DATABASE,
        'user': s.PG_USER,
        'password': s.PG_USER
    }
}

print(s.PG_USER, s.PG_HOST, s.PG_DATABASE, s.PG_PASSWORD, s.PG_PORT)

class TestTable(Model):
    pass

db = DatabaseManager(config)
schema = Schema(db)

Model.set_connection_resolver(db)

with schema.create('test_table') as table:
    table.increments('id')
