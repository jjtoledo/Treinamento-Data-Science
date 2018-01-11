# first quiz 
'''
print 'test'.find('t')
print "test".find('st')
print "Test".find('te')
print 'west'.find('test')

# second quiz
s = 'fdsaaf'
print s.find(s)
print s.find('s')
print 's'.find('s')
print s.find('')
print s.find(s + '!!!') + 1
'''
# with numbers now
i = 2
t = 'sa'
s = 'fdsaaf'
# print s[i:].find(t)
# print s.find(t)[i:]
# print s[i:].find(t) + i
print s[i:].find(t[i:])
