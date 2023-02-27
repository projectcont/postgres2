from configuration import dbconf
from sqlalchemy import create_engine
from configuration import showdebug

# PYTHON FUNCTION TO CONNECT TO THE POSTGRESQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_engine (
        user=dbconf['user'],
        password=dbconf['password'],
        host=dbconf['host'],
        port=dbconf['port'],
        database=dbconf['database']):


    engine = create_engine( f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}" )
    return engine





