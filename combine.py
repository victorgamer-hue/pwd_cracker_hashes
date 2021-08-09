words = open("combinations.txt").readlines()
tmpWord = ""
index = len(words) - 1

while len(tmpWord) < 20: 
  tmpWord = words[index]
  index += 1
  for ch in range(32, 127):
    words.append(tmpWord + chr(ch))
    open('combinations.txt', 'a').write(tmpWord + chr(ch) + '\n')
    print(tmpWord + chr(ch))
  
  
def chr(ch):
  return str(unichr(ch))
