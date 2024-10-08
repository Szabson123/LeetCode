


def isSubsequence(s: str, t: str):
    point_s = 0
    point_t = 0
    
    while point_s < len(s) and point_t < len(t):
        if s[point_s] == t[point_t]:
            point_s += 1
        point_t += 1
        
    return point_s == len(s)
        
    
x = isSubsequence(s = "abc", t = "ahbgdc")

print(x)