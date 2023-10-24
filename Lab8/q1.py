import re
properties=dir(re)                  # Lists all properties and methods of the given object without specifying values
ans=[]
for name in properties:
    if re.search('find',name):      # Search function given by regex module
        ans.append(name)
ans = sorted(ans)                   # Returns new sorted list
print(ans)