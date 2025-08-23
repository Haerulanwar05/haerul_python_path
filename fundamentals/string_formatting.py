# Old Style formatting

error_no = 45457984738
name = 'Haerul'

print('Hello, %s' %name)
print('%x' %error_no)

print('Hey %s, there is a 0x%x error!' %(name, error_no))
# output = Hey Haerul, there is a 0xa9581cce2 error!

print('Hey %(name)s, there is a 0x%(error_no)x error!' %{"name":name,"error_no":error_no})
# ouput sama 

# new style formatting

print('Hello, {}'.format(name))

print('Hey {}, there is a 0x{:x} error!'.format(name,error_no))
print('Hey {name}, there is a 0x{error_no:x} error!'.format(name=name,error_no=error_no))

# f-string 
print(f'Hello {name}')
print(f'ten plus ten = {10+10}')

print(f'Hey {name}, there is a {error_no:#x} error!')

