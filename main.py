import db

def main(drop = True):
    _db = db.Database()
    if drop:
        _db.drop_tables()
    _db.create_tables()
    _db.random_insert()
    del _db

if __name__ == '__main__':
    main()
