import happybase as hb
import csv

conn = hb.Connection()

# Create powers table
table_names = conn.tables()

#Create powers table
if b'powers' in table_names:
    powers_table = conn.table(b'powers')
    with powers_table.batch(batch_size=1000) as b:
        with open('input.csv', 'r') as f:
            for line in f:
                row_key, hero, power, name, xp, color = line.strip().split(',')
                print(row_key)
                b.put(row_key.encode(), {
                    b'personal:hero': hero.encode(),
                    b'personal:power': power.encode(),
                    b'professional:name': name.encode(),
                    b'professional:xp': xp.encode(),
                    b'custom:color': color.encode()
                })