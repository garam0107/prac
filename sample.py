text = 'hello'

print(text.find('h'))
print(text.index('e'))
print(text.find('he'))
print(text.index('llo'))

str1 = 'APPLE'
str2 = 'apple'
str3 = 'Hello123'
str4 = '안녕하세여'
print(str1.isupper()) # T
print(str2.islower()) # T
print(str3.isalpha()) # F
print(str1.isalpha()) # T
print(str4.isalpha())

# replace
text = 'Hello, World! World World'

new_text = text.replace('World', 'Python',2)
print(new_text)

# strip
text = 'Hello,wordl!'
new_text = text.strip('H')
print(new_text)

# split 
text = 'Hello,world!'
words = text.split(',')
words2 = text.split()
print(words) #['Hello', 'world!']
print(words2) #['Hello,world']

# join (리스트를 구분자를 기준으로 문자열로 연결)
words = ['Hello', 'world']
text = '-'.join(words)
print(text) #Hello-words

text = 'heLLo, woRld!'
new_text1 = text.capitalize()
new_text2 = text.title()
new_text3 = text.upper()
new_text4 = text.swapcase()
print(new_text1) # Hello, world - 첫번째를 대문자로 바꾸고 뒤의 문자를 모두 소문자로 바꿈
print(new_text2)
print(new_text3)
print(new_text4) # HEllO, WOrLD - 대문자와 소문자를 서로 교체

new_text5 = text.swapcase().replace('l','z')
print(new_text5)


t = 'hello, world    '
new_t = t.rstrip()
print(new_t)