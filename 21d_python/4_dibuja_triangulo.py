def draw_triangle(size, character):
    triangle = ""
    for i in range(0, size):
        spaces = (size-i-1) * " "
        characters = (2*i+1) * character
        triangle = triangle + spaces + characters + spaces + "\n"
    
    return triangle

print (draw_triangle(10,"*"))

"""
Otra forma de resolver el problema:

def print_triangle(size, character):
    triangle = ""
    for i in range(1, size + 1):
        spaces = " " * (size - i)
        line = character * (2 * i - 1)
        if i == size:
         triangle += spaces + line
        else:   
         triangle += spaces + line + "\n"
    return triangle

print(print_triangle(10, "*"))
"""