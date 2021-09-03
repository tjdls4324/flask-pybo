from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'TlKe\xbd\xe1yC\xf1\xac\xefZO\x99R\xe8'

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='dbmasteruser',
    pw='qkrtjdls',
    url='ls-00fa2416d7568d7c1eadfe3673c66ae0fe97581c.cif6jrsp3fvg.ap-northeast-2.rds.amazonaws.com',
    db='flask_pybo')