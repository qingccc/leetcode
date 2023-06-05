def judgeStr(s, index, sp):
 if index + len(sp) + 1 >= len(s):
  return False
 if s[index] == s[index + len(sp) + 1] == '"' and s[index+1:index+len(sp)+1] == sp:
  return True

def trip_res(s, sp):
 return s.strip(' ').strip('"').strip(sp).strip('"')

def split_expect(s, sp):
 res = []

 before_index = 0
 flag = True
 index = 0
 while(index<len(s)):
  ch = s[index]
  if ch == '"':
   if judgeStr(s, index, sp):
    flag = not flag
    index += len(sp)+1
  if ch == ',' and flag:
   res.append(trip_res(s[before_index:index], sp))
   before_index = index + 1
  index += 1
 if flag:
  res.append(trip_res(s[before_index:index], sp))

 return res

if __name__ == '__main__':
 sp = '"'
 s = ' """sss,abc""",123,"""456,7"""'
 print(split_expect(s, sp))
 sp = 'xxx'
 s = ' "xxx"sss,abc"xxx",123,"xxx"456,7"xxx"'
 print(split_expect(s, sp))