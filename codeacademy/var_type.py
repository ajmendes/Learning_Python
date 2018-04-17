def is_numeric(num):
  if type(num)==int: return "int"
  elif type(num)==float: return "float"
  elif type(num)==str: return "string"

print(is_numeric(1.1))
print(is_numeric("char"))
print(is_numeric(1))
print(is_numeric(1+2.2))