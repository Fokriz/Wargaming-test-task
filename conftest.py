import pytest
import db

@pytest.fixture(scope='session')
def db_fixture():
    f = open('warships.db', 'rb')
    data = f.read()
    f.close()

    f = open('warships_temp.db', 'wb')
    f.write(data)
    f.close()

    _db_temp = db.Database('warships_temp.db')
    _db_temp.random_update()
    _db = db.Database()
    return {'db' : _db, 'db_temp' : _db_temp}
