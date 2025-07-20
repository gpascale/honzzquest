import pymysql.cursors

conn = pymysql.connect(
    host='s2do.local',
    user='honzzquest',
    password='honzzquest',
    database='honzzquest',
    cursorclass=pymysql.cursors.DictCursor
)

slot_map = {
    0: "Cursor",
    1: "Ear1",
    2: "Head",
    3: "Face",
    4: "Ear2",
    5: "Neck",
    6: "Shoulders",
    7: "Arms",
    8: "Back",
    9: "Wrist1",
    10: "Wrist2",
    11: "Range",
    12: "Hands",
    13: "Primary",
    14: "Secondary",
    15: "Finger1",
    16: "Finger2",
    17: "Chest",
    18: "Legs",
    19: "Feet",
    20: "Waist",
    21: "Ammo",
    22: "General1",
    23: "General2",
    23: "General3",
    24: "General4",
    25: "General5",
    26: "General6",
    27: "General7",
    28: "General8"
}

q = '''
SELECT id, name, slots FROM items
WHERE
    name LIKE 'earring of blazing energy' OR
    name LIKE 'qeynos badge of honor' OR
    name LIKE 'dire wolf-hide cloak' OR
    name LIKE 'rod of insidious glamour' OR
    name LIKE 'shardtooth''s flayed skin' OR
    name LIKE 'beguiler''s crown' OR
    name LIKE 'eyepatch of plunder' OR
    name LIKE 'spiked seahorse hide belt' OR
    name LIKE 'di''zok signet%' OR
    name LIKE 'regal band of bathezid' OR
    name LIKE 'a sandwich of foul smelling herbs' OR
    name LIKE 'coldain skin gloves' OR
    name LIKE 'neriad shawl' OR
    name LIKE 'spirit wracked cord' OR
    name LIKE 'orb of the infinite void' OR
    name LIKE 'inlaid jade hoop' OR
    name LIKE 'golden cat eye bracelet' OR
    name LIKE 'spider fur-lined boots' OR
    name LIKE 'gatorscale leggings' OR
    name LIKE 'beguiler''s sleeves'
'''

items = []
with conn:
    with conn.cursor() as cursor:
        cursor.execute(q)
        for row in cursor.fetchall():
            slots = row['slots']
            ones = [i for i in range(slots.bit_length()) if (slots >> i) & 1]
            print(f'{row["id"]} {row["name"]}')
            print('  ' + ', '.join([f'{i} {slot_map[i]}' for i in ones]))
            items.append({
                'id': row['id'],
                'name': row['name'],
                'slots': ones
            })

lines = [f'(287250, {item["id"]}, {item["slots"][0]}), -- ({item["name"]}, {slot_map[item["slots"][0]]})' for item in items]
lines_str = ",\n  ".join(lines)
ins_query = f'''
  INSERT INTO character_inventory (id, itemid, slotid) VALUES
  {lines_str}
  ON DUPLICATE KEY UPDATE
  id = VALUES(id),
  itemid = VALUES(itemid),
  slotid = VALUES(slotid)
;
'''
print(ins_query)

# bitmask = 42  # for example
# index_map = {
#     0: "read",
#     1: "write",
#     2: "execute",
#     3: "admin",
#     4: "delete",
#     5: "share",
#     6: "archive"
# }

# # Extract set bit indices
# indices = [i for i in range(bitmask.bit_length()) if (bitmask >> i) & 1]

# # Map to strings
# labels = [index_map[i] for i in indices if i in index_map]

# print(labels)