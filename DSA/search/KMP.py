str1 = "abcxabsabcxabmnabcxabmnabckm"
str2 = "abcxabmnabck"
# str2 = "sabcxab"

def get_lps_arr() -> list:
    length = 0
    i = 1
    str2_len = len(str2)
    lps = [0] * str2_len
    while i < str2_len:
        if str2[i] == str2[length]:
            lps[i] = length+1
            i += 1
            length += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            i += 1
            length = 0

    return lps


def str_match() -> bool:
    lps_arr = get_lps_arr()
    m = len(str2)
    n = len(str1)
    j = 0
    i = 0
    while i < n:
        if str1[i] == str2[j]:
            i += 1
            j += 1
        elif j > 0:
            j = lps_arr[j-1]
        else:
            i += 1

        if j == m:
            return True

    return False


print(str_match())

