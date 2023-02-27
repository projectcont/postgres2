'''
python - PostgreSQL -integration script
'''

from prodcateg.product import Product
from sqlf.get_session_ import  get_session

session = get_session()


# Read product list
allprod = session.query(Product)
for prod_ in allprod:
    print('id=',prod_.id, prod_)



# Create a product
''' '''
product=Product( )
product.set_pr(ean="ean",title="Very nice", price=1200.5 )
session.add(product)
session.flush()
session.refresh(product)
session.commit()


# Update
'''
prod.title = "Some2016Film"
session.commit()
'''

prod_list_add = []
allprod = session.query(Product)

# changing product attribute by  product_id
for prod_ in allprod:
    print( getattr(prod_, 'id'))
    if (  prod_.id==5   ):
        print(prod_.title, '(changed by id)')
        prod_.title='title-id'
        #setattr(prod_, 'title', descr_)
        session.flush()
        session.refresh(prod_)
    session.commit()

# changing product attribute by  product_ean
for prod_ in allprod:
    print( getattr(prod_, 'id'))
    if (  prod_.ean=='ean2'   ):
        print(prod_.title, '(changed by ean)')
        prod_.title='title-ean'
        prod_.price = 4.2
        #setattr(prod_, 'title', descr_)
        session.flush()
        session.refresh(prod_)
    session.commit()

































