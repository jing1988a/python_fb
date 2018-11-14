# Ceasar Cipher 简单说就是 abc + 2 --> cde, xyz + 2 --> zab 不是字母不变 区分大小写
# 要求编译通过运行。


class Problem:
    def cipher(self, a, shift):
        ans = []
        for c in a:
            ans.append(chr((ord(c) - 97 + shift) % 26 + 97))
        return ''.join(ans)


a = 'xyz'
print(ord('a'))
test = Problem()
print(test.cipher(a, 26))
