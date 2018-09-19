# http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpc.client
conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

print(conn.system.listMethods())
# ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']

print(conn.system.methodHelp('phone'))
# Returns the phone of a person

print(conn.system.methodSignature('phone'))
# [['string', 'string']]

print(conn.phone('bert'))
# He is not the evil

print(conn.phone('Bert'))
# 555-ITALY
