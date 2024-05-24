import mysql.connector
class Database:
    def __init__(self, host, user, port, passwd, database):
        self._conn = mysql.connector.connect(
            host=host,
            user=user,
            port=port,
            passwd=passwd,
            database=database,
            auth_plugin='mysql_native_password'
        )
        self._cursor = self._conn.cursor()

    def query(self, sql):
        self._cursor.execute(sql)
        return self._cursor.fetchall()

    def insert(self, table, fields, values):
        sql = f"INSERT INTO {table} ({','.join(fields)}) VALUES ({','.join(['%s']*len(values))})"
        self._cursor.execute(sql, values)
        self._conn.commit()
        return self._cursor.lastrowid

    def update(self, table, fields, values, condition):
        set_clause = ','.join([f"{field}=%s" for field in fields])
        sql = f"UPDATE {table} SET {set_clause} WHERE {condition}"
        self._cursor.execute(sql, values)
        self._conn.commit()
        return self._cursor.rowcount

    def delete(self, table, condition):
        sql = f"DELETE FROM {table} WHERE {condition}"
        self._cursor.execute(sql)
        self._conn.commit()
        return self._cursor.rowcount

    def __del__(self):
        self._cursor.close()
        self._conn.close()