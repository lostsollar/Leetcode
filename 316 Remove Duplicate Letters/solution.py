# -*— coding:utf-8 -*-


def remove_duplication_letters1(s):
    # https://www.hrwhisper.me/leetcode-remove-duplicate-letters/
    vis = [False] * 26
    cnt = [0] * 26
    res = []
    for c in s:
        cnt[ord(c) - 97] += 1
    for c in s:
        index = ord(c) - 97
        cnt[index] -= 1
        if vis[index]:
            continue
        while res and ord(c) < ord(res[-1]) and cnt[ord(res[-1]) - 97]:
            vis[ord(res.pop()) - 97] = False
        res.append(c)
        vis[ord(c) - 97] = True
    return "".join(res)


def remove_duplication_letters2(s):
    """
    每次找最小值，如果遇到 cnt 为0的字符则停止(意味着该字符后面不会再出现了)
    然后将最小值放入结果中，该最小值为截止到后面不会再出现的字符前的最小字符,
    然后从该最小值后面的子字符串作为新字符串重新开始循环, 时间复杂度为 O(n2)
    :param s:
    :return result:
    """
    res = ''
    while s:
        cnt = {}
        for c in s:
            cnt[c] = cnt.get(c, 0) + 1
        min_index, min_value = 0, s[0]
        for i, c in enumerate(s):
            if c < min_value:
                min_index, min_value = i, c
            cnt[c] -= 1
            if cnt[c] == 0:
                break
        res += min_value
        s = s[min_index + 1:].replace(min_value, '')
    return res


def check_solution(func, test_set, index=None):
    if index is not None:
        print test_set[index]
        print func(test_set[index])
        print
    else:
        for test in test_set:
            print test
            print func(test)
            print


if __name__ == "__main__":
    test1 = "bcaaaaabdabc"
    test2 = "bcabc"
    test3 = "cbacdcbc"
    tests = [test1, test2, test3]

    # check_solution(remove_duplication_letters1, tests)
    check_solution(remove_duplication_letters2, tests, -1)
