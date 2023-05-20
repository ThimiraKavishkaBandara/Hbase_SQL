import happybase as hb


# Connect to HBase
conn = hb.Connection()
table_names = conn.tables()

#Create powers table
if b'powers' in table_names:
    conn.disable_table('powers')
    conn.delete_table('powers')
else:
    conn.create_table(
        'powers',
        {
            'personal': dict(),
            'professional': dict(),
            'custom': dict(),
        }
    )

#Create food table
if b'food' in table_names:
    conn.disable_table('food')
    conn.delete_table('food')
else:
    conn.create_table(
        'food',
        {
            'nutrition': dict(),
            'taste': dict(),
        }
    )