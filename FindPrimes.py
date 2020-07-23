n_ls = []
p_ls = []
search_range = 1500
for i in range(search_range):
    n_ls += [i+2]
for i in (n_ls):
    for f in range(search_range):
        rational = f / i+2
        if rational == int(rational):
            pass
        elif (f/3) == int(f/3) and f != 3:
            pass
        elif (f/5) == int(f/5) and f != 5:
            pass
        elif (f/7) == int(f/7) and f != 7:
            pass
        elif (f/5) == int(f/5) and f != 9:
            pass
        elif (f/11) == int(f/11) and f != 11:
            pass
        elif (f/13) == int(f/13) and f != 13:
            pass
        elif (f/17) == int(f/17) and f != 17:
            pass
        elif (f/19) == int(f/19) and f != 19:
            pass
        elif (f/23) == int(f/23) and f != 23:
            pass
        elif (f/29) == int(f/29) and f != 29:
            pass
        elif (f/31) == int(f/31) and f != 31:
            pass
        elif (f/37) == int(f/37) and f != 37:
            pass
        else:
            p_ls += [f]
p_ls[0] += 1
p_ls = p_ls[0:167]
print(p_ls)