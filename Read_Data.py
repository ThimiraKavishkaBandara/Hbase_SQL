import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER
conn = hb.Connection()
table = conn.table(b'powers')

hero = table.row(b'row1', columns=[b'personal:hero'])[b'personal:hero']
power = table.row(b'row1', columns=[b'personal:power'])[b'personal:power']
name = table.row(b'row1', columns=[b'professional:name'])[b'professional:name']
xp = table.row(b'row1', columns=[b'professional:xp'])[b'professional:xp']
color = table.row(b'row1', columns=[b'custom:color'])[b'custom:color']

print('hero: {}, power: {}, name: {}, xp: {}, color: {}'.format(hero, power, name, xp, color))

hero = table.row(b'row19', columns=[b'personal:hero'])[b'personal:hero']
color = table.row(b'row19', columns=[b'custom:color'])[b'custom:color']

print('hero: {}, color: {}'.format(hero, color))

hero = table.row(b'row1', columns=[b'personal:hero'])[b'personal:hero']
name = table.row(b'row1', columns=[b'professional:name'])[b'professional:name']
color = table.row(b'row1', columns=[b'custom:color'])[b'custom:color']
print('hero: {}, name: {}, color: {}'.format(hero, name, color))