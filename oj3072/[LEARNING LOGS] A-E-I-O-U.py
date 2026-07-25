"""[LEARNING LOGS] A-E-I-O-U"""

text = input().lower()
a_count = text.count("a")
e_count = text.count("e")
i_count = text.count("i")
o_count = text.count("o")
u_count = text.count("u")

if a_count:
    print(f"a : {a_count}")
if e_count:
    print(f"e : {e_count}")
if i_count:
    print(f"i : {i_count}")
if o_count:
    print(f"o : {o_count}")
if u_count:
    print(f"u : {u_count}")
