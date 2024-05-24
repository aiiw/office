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

    # def __del__(self):
    #     if hasattr(self, '_cursor') and self._cursor is not None:
    #         self._cursor.close()
    #     self._conn.close()
    def close(self):
        self._cursor.close()
        self._conn.close()

# db = Database(
#     host="192.168.0.7",
#     user="root",
#     port="3306",
#     passwd="123456",
#     database="dj3"
# )

# # 查询数据
# result = db.query("SELECT * FROM wk")
# print(result)
# db.close()
# # 关闭游标和数据库连接


# # 新增数据
# fields = ['name', 'age']
# values = ('John', 30)
# last_id = db.insert('some_table', fields, values)
# print(last_id)

# # 更新数据
# fields = ['name', 'age']
# values = ('Bob', 25)
# condition = "id=1"
# affected_rows = db.update('some_table', fields, values, condition)
# print(affected_rows)

# # 删除数据
# condition = "id=2"
# affected_rows = db.delete('some_table', condition)
# print(affected_rows)