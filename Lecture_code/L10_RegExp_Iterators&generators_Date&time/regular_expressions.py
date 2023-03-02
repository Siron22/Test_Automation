text = """
<link rel="shortcut icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/favicon.ico?v=ec617d715196">
<link rel="apple-touch-icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">
<link rel="image_src" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">
"""

s = "as,df,a,sfdf"
print(s.isalnum())
print(s.split('s,'))

import re

# pattern = 'href="(.*)"'
# re_obj = re.compile(pattern)
# res = re_obj.findall(text)
#
# print(res)
#
# res2 = re.findall(pattern, text)
# print(res2)
#
# pattern = 'rel="(.*)" href="(.*)"'
# res3 = re.findall(pattern, text)
# print(res3)
#
# pattern = 'rel="(.*) "Qhref="(.*)"'
# res4 = re.findall(pattern, text)
# print(res4)

# ####################################################33

pattern = 'href="(.*)"'
res5 = re.search(pattern, text)
print(res5.span())
print(res5.group())

pattern = 'href="(QQ.*)"'
res6 = re.search(pattern, text)
print(res6)
if res6:
    print(res6.group())
else:
    print("Nothing found")

# ####################################################33

text = "[1,2,3,[4,5],6,7]"
pattern = "[\[,\]]"
res7 = re.split(pattern, text)
print(res7)

pattern = '[a-z]'
text = "sdfsadsafdGJHGJHFHFS"
res = re.findall(pattern, text, flags=re.IGNORECASE)
print(res)

# TODO: dsdds
# FIXME: dfffsdf
# HELPME: dsdsdsdsd
# GoodLine: