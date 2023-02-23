#implementaion of string matchng
def stringMatch(pat, txt):
    M = len(pat)
    N = len(txt)
    for i in range(N - M):
        for j in range(M):
            k = j + 1
            if (txt[i + j] != pat[j]):
                break
        if (k == M):
            print("Pattern found at index ", i)
txt = input("enter the text format string: ")
pat = input("enter the pattern we want to find the match: ")


stringMatch(pat, txt)