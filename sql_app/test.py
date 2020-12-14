from sql_app.database2 import SessionLocal

def get_db():
    print('0')
    db = 'yi'
    print('1')
    try:
        print('2')
        yield db
        print('3')
    finally:
        print('5')

i = get_db()
print(next(i))