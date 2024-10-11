def is_leap_year(year):
    # tu código aquí 👈
    if year >= 0 and type(year) == int:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            return True
        else:
            return False
    else:
        return False

print(is_leap_year(2000))
print(is_leap_year(-2024))
print(is_leap_year(1984.25))

"""
Otra forma de resolverlo:

def is_leap_year(year):
    if year % 1 != 0 or year <= 0:
      return False
    
    elif year % 4 == 0:
      if year % 100 == 0 and year % 400 == 0:
         return True

      elif year % 100 == 0: # else: return False
         return False
    
    else:
        return False
       
response = is_leap_year(2000)
print(response)
"""