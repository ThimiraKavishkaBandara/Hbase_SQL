import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER
conn = hb.Connection()
powers_table = conn.table(b'powers')

for key, data in powers_table.scan(include_timestamp=True):
    print('Found: {}, {}'.format(key, data))


