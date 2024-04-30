"""
Test to see if 2 strings are anagrams.
"""


def is_anagram(s1, s2) -> bool:
    s1_map = {}
    s2_map = {}
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] in s1_map:
            s1_map[s1[i]] += 1
        else:
            s1_map[s1[i]] = 1

        if s2[i] in s2_map:
            s2_map[s2[i]] += 1
        else:
            s2_map[s2[i]] = 1

    for key, item in s1_map.items():
        if key not in s2_map:
            return False
        elif s1_map[key] != s2_map[key]:
            return False

    return True


def main():
    print(is_anagram("nameless", "salesmen"))
    print(is_anagram("mike", "john"))
    print(is_anagram("igloo", "oilgo"))
    print(is_anagram("nameless", "salesman"))


if __name__ == "__main__":
    main()
