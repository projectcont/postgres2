from sqlalchemy import MetaData
from sqlalchemy.orm import mapper, relationship, sessionmaker
from sqlf.engine import get_engine
from prodcateg.product import Product
from prodcateg.productb import get_productb


def get_session():

    #BASE_DIR = Path(__file__).resolve().parent
    #print('BASE_DIR= ',BASE_DIR)

    metadata = MetaData()

    productb = get_productb(metadata)
    mapper(Product, productb)



    try:
        engine = get_engine()
        print(f"Engine created successfully.")

        # metadata.create_all(engine)
        # print(f"Table created successfully.")

        DBSession = sessionmaker(bind=engine, autoflush=True)
        print(f"sessionmaker successfully.")

        session = DBSession()
        print(f"DBSession successfully.")

        return session

    except Exception as ex:
        print("ОШИБКА SQL: \n", ex)

