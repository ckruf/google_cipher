import unittest

def solution(cipher: str) -> str:
    """
    Given ciphertext as a string, return the decoded plaintext.
    The cipher used takes every lower case letter [a...z] and replaces it with the corresponding one in [z...a].
    """
    plain = list(cipher)
    for i in range(len(cipher)):
        if plain[i].islower() and plain[i].isalpha():
            if ord(plain[i]) < 110:
                distance = 109 - ord(plain[i])
                plain[i] = chr(110 + distance)
            else:
                distance = ord(plain[i]) - 110
                plain[i] = chr(109 - distance)
    return "".join(plain)


def main() -> None:
    print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
    print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"), "did you see last night's episode?")


    def test2(self):
        self.assertEqual(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"), 
        "Yeah! I can't believe Lance lost his job at the colony!!")

if __name__ == '__main__':
    main()
    # unittest.main()
    