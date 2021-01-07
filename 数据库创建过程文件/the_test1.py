import history_readfuns
import people_readfuns
import share_funs
#thelist=history_readfuns.readperiods()
#history_readfuns.readimg(thelist[9],'thetest.jpg')

thelist=share_funs.readnames()
for i in thelist:
    print(i)

name=thelist[0]
share_funs.readimg(name,'thetest.jpg')
content=share_funs.readcontent(name)


"""
print(name)
time=people_readfuns.readtime(name)
print(time)
print(content)
"""

