python正则表达式
1.python中提供了正则表达式的匹配，可以使用re
import re
2.re.findall(rule,content)通过rule的规则匹配得到列表 ,如果没有符合的就返回一个空列表

import re
s='123abc456eabc789'
re.findall(r'abc',s)
['abc', 'abc']
pattern = '[1-9]'
pat = re.compile(pattern)
re.findall(pat,s)
['1', '2', '3', '4', '5', '6', '7', '8', '9']

r'...'字符串的使用（raw字符串）？由于正则表达式的规则也是一个由一个字符串定义的，而在正则表达式中大量使用转义字符‘\’,如果不用raw串，
则在需要些一个'\'的地方，必须的写成‘\\’，那么在要从目标字符串中匹配一个'\\'，就这写成'\\\\'，很麻烦。一般用r''来定义规则字符串。当然
在某些情况下可能不用raw字符串较好。
3.
功能符号'.','*','+','|','?','^','$','\'等
规范分界符：'[',']','(',')','{','}'等
预定义转义字符集：/d,/w,/s等
其他特殊功能字符：# ，！，：，_等


基本设定：
[]字符集和设定符，由一对方括号括起来的字符，表明一个字符集合，能够匹配包括在其中的任意一个字符。如[abc123]表明字符a,b,c,1,2,3都符合他的要求。
在[]中还可以通过-来制定字符集的范围，如[a-zA-Z]所有英文字母都可以匹配，但不可以倒过来写[z-a]错误。
如果在[]的开头加一个^，则表示取非，即在括号里的字符都不包含，如不包含所有英文字母[^a-zA-Z]。但是如果^不在开头，则表示他本身，如[a-z^A-Z],所有字母，加上^都匹配


|或规则，表示将两个规则并列起来，以|连接，表示只要满足其中之一即可。如[a-zA-Z]|[0-9]表示满足数字或者字母就可以匹配，等价于[a-zA-Z0-9]
注意：他在[]中不在表示或，而是表示其本身；如果要在[]外面使用|字符，需要用反斜杠，'\|'

mm='abdc/dejl9032/dfaf'
re.findall('//',mm)
[]
re.findall('[/]',mm)
['/', '/']
mc='fasdj|324|fsl'
re.findall(r'|',mc)
['', '', '', '', '', '', '', '', '', '', '', '', '', '']
re.findall('/|',mc)
['', '', '', '', '', '', '', '', '', '', '', '', '', '']
re.findall('[|]',mc)
['|', '|']
re.findall('\|',mc)
|注意：他的有效范围是他两边的整条规则，如'dog|cat'匹配的是'dog'和'cat'，而不是单个的g,c字符。如果想限定他的有效范围，必须使用一个无捕获组'(?:)'
括起来。比如匹配'i have a dog'或者'i have a cat'要写成'i have a (?:dog|cat)'
ss='this my first program i have a dog or i have a cat'
re.findall('i have a (?:dog|cat)',ss)
['i have a dog', 'i have a cat']
re.findall(r'i have a dog|cat',ss)
['i have a dog', 'cat']


'.'匹配所有字符,匹配除了换行符'\n'之外的所有字符。如果使用了'S'选项，匹配包括'\n'的所有字符

s='123\nfsa;jf;a\nmfslf'
print(s)
123
fsa;jf;a
mfslf
re.findall(r'.+',s)
['123', 'fsa;jf;a', 'mfslf']
re.findall(r'.+',s,re.S)
['123\nfsa;jf;a\nmfslf']


'^' '$'匹配字符串开头和结尾，注意^不能出现在[]中，否则含义就发生变化了。

s='123\nfsa;jf;a\nmfslf'
print(s)
123
fsa;jf;a
mfslf
re.findall(r'.+',s)
['123', 'fsa;jf;a', 'mfslf']
re.findall(r'.+',s,re.S)
['123\nfsa;jf;a\nmfslf']
re.findall(r'^[0-9]',s)
['1']
re.findall(r'^[0-9][a-z]$',s)
[]
re.findall(r'^[0-9].+[a-z$]',s)
[]
re.findall(r'$[a-z]',s)
[]
re.findall(r'[a-z]$',s)
['f']
re.findall(r'^[0-9].*[a-z]$',s)
[]


\d匹配数字，等价于[0-9]


\D匹配非数字，大写小互补，等价[^0-9]


\w匹配字母数字，等价于[a-zA-Z0-9]


\W匹配非英文字母和数据，等价于[^a-zA-Z0-9]


\s匹配间隔符，即空格符、制表符、回车符等，他等价于[\t\r\n\f\v]


\S匹配非间隔符，等价于[^\t\r\n\f\v]


\A匹配字符串开头，只是匹配整个字符串的开头


\Z匹配字符串结尾，职匹配整个字符串的结尾

sss='12 34\n56 78\n90'
re.findall(r'^\d',sss)    #匹配字符串首个数字
['1']
re.findall(r'^\d+',sss)  #匹配字符串行首的数字
['12']
re.findall(r'^\d+',sss,re.M)  #匹配每一行首的数字
['12', '56', '90']
re.findall(r'\A\d',sss)  #匹配首行数字
['1']
re.findall(r'\A\d+',sss)
['12']
re.findall(r'\d+$',sss,re.M)  #匹配每行结尾数字
['34', '78', '90']
re.findall(r'\d+\Z',sss,re.M)  #匹配字符串结尾的数字
['90']

\b匹配单词边界，它匹配一个单词的边界，比如空格等，不过他是一个长度为0的字符创，它匹配完的字符串不会包括那个分界的字符。
而如果用\s来匹配的话，则会匹配出的字符串中会包含那个分界符



s='abc abcde bc bcd'
re.findall(r'\bbc\b',s)  #匹配一个单独的单词'bc',而当他是其他单词一部分的时候，不匹配
['bc']
re.findall(r'\sbc\s',s) #匹配一个单独的单词，不过注意前后有两个空格，这就是会包含分界符的意思
[' bc ']




\B匹配非边界，和\b相反，他只匹配非边界的字符。他同样是个长度为0的字符
匹配包含bc，但是不以bc为开头的单词，

re.findall(r'\Bbc\w+',s)
['bcde']




(?:)无捕获组，当要将一部分规则作为一个整体对他进行某些操作，比如指定其重复的次数时，则需要如此使用，
如匹配字符串中重复的ab

s='ababab abbabb aabaab'
re.findall(r'\b(?:ab)+\b',s)
['ababab']
re.findall(r'\b(ab)+\b',s)  #该处使用了比较复杂的组，因此得不到想要的
['ab']

ss='123.34 0.34 12 23e34'
re.findall(r'\b\d+[eE]?\.?\d*\b',s)
['123', '10e3']
re.findall(r'\d+.?\d*',s) #带小数点的数据匹配
['123 10', '3 20', '4e4', '20e', '5']
re.findall(r'\b\d+.?[eE]?\d*\b',s)
['123 ', '10e3', '20ee5']
re.findall(r'\b\d+.?[eE]?\d*\b',ss)
['123.34', '0.34', '12 ', '23e34']

'(?#)'注释，可以在正则表达式中用成对的该符号，表示注释


4.重复
正则表达式需要匹配不定长的字符串，那就一定需要表示重复的指示符。规则是在一条字符规则后面紧跟一个表示重复次数的规则，已表明需要重复前面的规则一定次数
* 0或者多次匹配
+一次或多次匹配

re.findall(r'\b[a-z]+\d*\b',s) #匹配单词中至少有一个字母开头，以连续数字或者无数字结尾
['aaa', 'bbb111']
re.findall(r'[a-z]+\d*')
Traceback (most recent call last):
File "<pyshell#48>", line 1, in <module>
re.findall(r'[a-z]+\d*')
TypeError: findall() missing 1 required positional argument: 'string'
re.findall(r'[a-z]+\d*',s) #不加\b边界指示符的话就是单独拆解，单词可能会被拆开
['aaa', 'bbb111', 'cc22', 'cc', 'dd']




? 0次或者1次
只匹配前面的规则0次或者1次
匹配一个数字，这个数字可以使一个整数，也可以是一个科学计数法记录的数字，比如123和10e3都是正确的数字

re.findall(r'\b\d+[eE]?\d*\b',s)  #匹配数字，格式是数字数字中间用空格分割，形如123，或者12e3,13E32 都是正常的
['123', '10e3']




{m} 精确匹配m次
{m,n} 匹配最少m次，最多n次（n>m）
如果只想指定一个最小或者一个最大次数，另一个次数可以省略
如{,5}最大5次，{5,}最小5次

s='1 22 333 4444 55555 666666'
re.findall(r'\b\d{3}\b',s)
['333']
re.findall(r'\b\\d{2,4}b',s)
[]
re.findall(r'\b\d{2,4}\b',s)
['22', '333', '4444']
re.findall(r'\b\d{5,}\b',s)
['55555', '666666']
re.findall(r'\b\d{1,4}\b',s)
['1', '22', '333', '4444']


'*?' '+?' '??'  原本他们通常单个字符时都是尽可能匹配多个字符。有时候我们希望尽可能少的匹配，

s=r'/* part1 */ code /* part2 */'
print(s)
/* part1 */ code /* part2 */
re.findall(r'/*.*/*/',s)
['/* part1 */ code /* part2 */']
re.findall(r'/*.*?/*/',s)
['/* part1 */', ' code /', '* part2 */']
#只要得到注释里面的内容，分割开来
re.findall(r'/\*.*?\*/',s)
['/* part1 */', '/* part2 */']
#只匹配到注释内容
/ ，\*转意字符*，.*?最小匹配，\*转意*，/




5.前后界定：
(?<=...) 前向界定，括号中代表希望匹配的字符串的前面应该出现的字符串


(?=...) 后向界定，代表字符串后面应该出现的字符串

s='山东电视台 杜兆龙'
import re
re.findall(r'(杜兆龙)',s)
['杜兆龙']
s=r'/* comment 1 */ code /* comment 2 */'
re.findall(r'(?<=/\*).+?(?=\*/)',s)
[' comment 1 ', ' comment 2 ']
re.findall(r'(?<=/\*).*?(?=\*/)',s)
[' comment 1 ', ' comment 2 ']

匹配相关的注释内容
s=r'上冻电视台；是发生'
re.findall(r'(.+)；(.+)',s)
[('上冻电视台', '是发生')]

中文分号；


前向界定括号中的表达式必须是常值，也就是不可以在前向界定的括号里写正则式。如要在字符串中想找到被字母夹在中间的数字，

s = 'aaa111aaa,bbb222,333ccc'
re.findall(r'(?<=[a-z]+)\d+(?=[a-z]+)',s)
Traceback (most recent call last):
File "<pyshell#9>", line 1, in <module>
re.findall(r'(?<=[a-z]+)\d+(?=[a-z]+)',s)
File "C:\Python33\lib\re.py", line 201, in findall
return _compile(pattern, flags).findall(string)
File "C:\Python33\lib\re.py", line 281, in _compile
p = sre_compile.compile(pattern, flags)
File "C:\Python33\lib\sre_compile.py", line 495, in compile
code = _code(p, flags)
File "C:\Python33\lib\sre_compile.py", line 480, in _code
_compile(code, p.data, flags)
File "C:\Python33\lib\sre_compile.py", line 115, in _compile
raise error("look-behind requires fixed-width pattern")
sre_constants.error: look-behind requires fixed-width pattern
re.findall(r'[a-z]+(\d+)[a-z]+',s)
['111']

匹配字母中间的数字，但是前向界定括号中不能够使用变量，可以使用前面的例子


(?<!...) 前向非界定
(?!...) 后向非界定
前面不是什么，后面不是什么


组的基本知识
() 无名组

s= 'aaa111aaa,bbb222,333ccc'
re.findall(r'[a-z]+()',s)
['', '', '', '']
re.findall(r'[a-z]+(\d+)[a-z]+',s)
['111']


(?P<name>...)命名组，调用已匹配的命名组 (?P=name),它里面的内容是和前面命名里的内容是一样的。


\number 通过序号调用已匹配的组

s='111aaa222aaa111,333bbb444bb33'
re.findall(r'(\d+)([a-z]+)(\d+)(\2)(\1)',s)
[('111', 'aaa', '222', 'aaa', '111')]




6.re模块的基本函数
findall(rule,target,[,flag])


compile(rule,[,flag])


match(rule,targetString,[,flag])


search(rule,targetString,[,flag])


sub(rule,replace,target,[,count])


subn(rule,replace,target,[,count])


split(rule,target,[,maxsplit])

s='i have a dog , you have a dog , he have a dog'
re.split(r'\s*,\s*',s)
['i have a dog', 'you have a dog', 'he have a dog']


空格，空格 分割出字符串


escape(string)


正则表达式也有组的标号，标号0为正则表达式本身；1为第一个正则表达式，2....

pattern = re.compile(r'(?P<name>[a-z]+)\s+(?P<age>\d+)\s+(?P<tel>\d+)*',re.I)
pattern.groupindex
{'age': 2, 'tel': 3, 'name': 1}
s='Tom 24 88888888 <='
m=pattern.search(s)
m.groups()
('Tom', '24', '88888888')
m.group('name')
'Tom'
m.group(1)
'Tom'
m.group(0)
'Tom 24 88888888'



pattern = re.compile(r'(?P<name>[a-z]+)\s+(?P<age>\d+)\s+(?P<tel>\d+)*',re.I)
pattern.groupindex
{'age': 2, 'tel': 3, 'name': 1}
s='Tom 24 88888888 <='
m=pattern.search(s)
m.groups()
('Tom', '24', '88888888')
m.group('name')
'Tom'
m.group(1)
'Tom'
m.group(0)
'Tom 24 88888888'


7.match对象的方法
group(index|id)获取匹配的组，缺省返回组0，也就是全不知
groups() 返回全部的组
groupdict() 返回以组名为key，匹配的内容为values的字典


start([group])
end([group])
span([group])
expand(template)

m.expand(r'name is \g<1>,age is \g<age> ,tel is \3')
'name is Tom,age is 24 ,tel is 88888888'

m.pos
0
m.endpos
18

pos 初始位置
endpos 结束位置
lastindex 最后匹配的组的序号
lastindex 最后匹配的组的序号
m.pos
0
m.endpos
18
m.lastindex
3
m.lastgroup
'tel'

m.re.pattern
'(?P<name>[a-z]+)\\s+(?P<age>\\d+)\\s+(?P<tel>\\d+)*'
m.string
'Tom 24 88888888 <='