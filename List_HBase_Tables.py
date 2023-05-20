import happybase as hb

conn = hb.Connection()
table_names = conn.tables()
print(table_names)