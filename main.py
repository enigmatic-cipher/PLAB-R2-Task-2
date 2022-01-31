"""
Given a list of size n as input. Remove all even elements from this list.
Print this new list as well as its size.
Input-> [1,7,8,9,2]
Output-> 
Size=3 
1#7#9#
"""

ls = [1,7,8,9,2]
ln = len(ls)
pt = "#"
count = 0
nw_ls = []
for i in range(0,ln):
  e = ls[i]
  if (e%2!=0):
    nw_ls = nw_ls + [e] + [pt]
    count = count + 1
print(nw_ls)
print(f"Size:{count}")
