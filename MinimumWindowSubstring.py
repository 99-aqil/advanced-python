
def minimumWindowSubstring(s, t):
    if t == "":
        return ""
    countT, window = {}, {}

    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    have, need = 0, len(countT)
    result, resLen = [-1, -1], float("infinity")
    left = 0

    for right in range(len(s)):
        c = s[right]
        window[c] = 1 + window.get(c, 0)

        if c in countT and window[c] == countT[c]:
            have += 1
        while have == need:
            # update our result
            if (right-left+1) < resLen:
                result = [left, right]
                resLen = (right-left+1)
            # pop from the left our window
            window[s[left]] -= 1
            if s[left] in countT and window[s[left]] < countT[s[left]]:
                have -= 1
            left += 1

    left, right = result
    if resLen != float("infinity"):
        return s[left:right + 1]
    else:
        return ""


if __name__ == '__main__':
    print('1) Output of "Minimum Window Substring":', minimumWindowSubstring("ADOBECODEBANC", "ABC"))
