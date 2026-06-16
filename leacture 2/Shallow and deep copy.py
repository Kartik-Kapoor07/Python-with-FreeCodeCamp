import copy
# *Assignment → same everything (one object, two names)
a = [[1, 2], [3, 4]]
b = a                    # same object, two names

b.append([5, 6])         # affects both
b[0].append(99)          # affects both

print(a)  # [[1, 2, 99], [3, 4], [5, 6]]
print(b)  # [[1, 2, 99], [3, 4], [5, 6]]  ← identical
print(id(a) == id(b))  # True — same object in memory


# *Shallow copy → outer list is new, inner objects are shared
c = [[1, 2], [3, 4]]
d = a.copy()             # new outer list, shared inner lists

c.append([5, 6])         # only affects d (outer list is separate)
d[0].append(99)          # affects BOTH (inner list is shared)

print(c)  # [[1, 2, 99], [3, 4]]          ← got 99 but not [5,6]
print(d)  # [[1, 2, 99], [3, 4], [5, 6]]  ← has both

print(id(c) == id(d))    # False — different outer list
print(id(c[0]) == id(d[0]))  # True — same inner list


# *Deep copy → outer list is new, inner objects are also new — fully independent
e = [[1, 2], [3, 4]]
f = copy.deepcopy(a)     # new outer list AND new inner lists

f.append([5, 6])         # only affects f
f[0].append(99)          # only affects f — e is untouched

print(e)  # [[1, 2], [3, 4]]              ← completely unchanged
print(f)  # [[1, 2, 99], [3, 4], [5, 6]]

print(id(e) == id(f))        # False — different outer list
print(id(e[0]) == id(f[0]))  # False — different inner list too