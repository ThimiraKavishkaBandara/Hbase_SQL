import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER
connection = hb.Connection()
table = connection.table('powers')

for key, data in table.scan():
    color = data[b'custom:color'].decode()
    name = data[b'professional:name'].decode()
    power = data[b'personal:power'].decode()


    for key1,data1 in table.scan():
        color1 = data1[b'custom:color'].decode()
        name1 = data1[b'professional:name'].decode()
        power1 = data1[b'personal:power'].decode()

        if color == color1 and name != name1:
            print('b\'{}\', b\'{}\', b\'{}\', b\'{}\', b\'{}\''.format(name, power, name1, power1, color))



