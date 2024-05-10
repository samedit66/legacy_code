def zips(i_s):
    res = []
    i = 0
    while i < len(i_s):
        if res and res[-1] == i_s[i]:
            cc = 2
            i += 1
            while i < len(i_s) and i_s[i] == res[-1]:
                cc = cc + 1
                i += 1
            res.append(str(cc))
        if i < len(i_s):
            res.append(i_s[i])
            i += 1
    return(''.join(res))
