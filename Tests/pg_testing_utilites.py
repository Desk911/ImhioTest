import psycopg2

conn = psycopg2.connect(dbname='core', user='postgres',
                        password='devpass', host='localhost', port='5433')

def get_last_record_device():
    cursor = conn.cursor()
    cursor.execute('SELECT device FROM public.t_feedback_models ORDER BY id desc LIMIT 1')
    record = cursor.fetchone()
    return record.__getitem__(0)