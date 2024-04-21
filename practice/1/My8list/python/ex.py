from black_hole_list import BlackHoleList
from list_node import BlackHoleNode

# 1. Create an empty BlackHoleList:
bh_list = BlackHoleList()
print(bh_list)

# 2. Append black holes with their types:
bh_list.append(10, "quasar")
print(bh_list)
bh_list.append(25, "blazar")
print(bh_list)
bh_list.append(15)  # Unknown type
print(bh_list)
bh_list.append(30, "quasar")
print(bh_list)

# 3. Print the list and sublists:
print("Main List:", bh_list)
print("Quasars:", bh_list.quasars)
print("Blazars:", bh_list.blazars)
print("Unknown:", bh_list.unknown)

# 4. Check length of the list and sublists:
print("Length of main list:", len(bh_list))
print("Number of quasars:", len(bh_list.quasars))

# 5. Check if a black hole exists:
if 25 in bh_list:
    print("Black hole with mass 25 exists.")

# 6. Remove a black hole:
bh_list.remove(15)
print("After removing 15:", bh_list)

# 7. Pop the last element:
last_bh = bh_list.pop()
print("Popped black hole:", last_bh)

# 8. Insert a black hole at a specific index:
bh_list.insert(1, 20, "blazar")
print("After inserting 20:", bh_list)

# 9. Reverse the list:
bh_list.reverse()
print("Reversed list:", bh_list)

# 10. Get the index of a black hole:
index = bh_list.index(30)
print("Index of black hole with mass 30:", index)
