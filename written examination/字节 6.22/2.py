n, m = map(int, input().strip().split())
s = input().strip()

key_word = [set() for _ in range(12)]
for _ in range(m):
    t = input().strip()
    key_word[len(t)].add(t)

valid_key_word_length = []
for i in range(len(key_word)):
    if len(key_word[i]) != 0:
        valid_key_word_length.append(i)

ans = 0
for key_word_len in valid_key_word_length:
    for i in range(n - key_word_len + 1):
        if s[i:i + key_word_len] in key_word[key_word_len]:
            ans += 1

print(ans)

