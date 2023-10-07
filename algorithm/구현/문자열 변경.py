spell = '353'
print(type(spell))

a = int(spell)
print(type(a))


destroy_str = 'hidoctor'

# 문자열은 변경 불가. list로 변환.
s = list(destroy_str)
s[2] = 'F'
s[3] = 'K'

print(''.join(s))


s = "Ninja"
new_s = s[:2]+'K'+s[3:]
print(new_s)

# 문자열 자르기
new_s = new_s[:-1]
print(new_s)
