from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

mat = []

add_point(mat, 0, 0, 0)
add_point(mat, 0, 100, 0)
add_point(mat, 100, 100, 0)
add_point(mat, 100, 0, 0)
add_point(mat, 0, 0, 0)
draw_lines(mat, screen, [255, 255, 255])

scalmat = scale(1.1, 1.1, 0)
for i in range(16):
    mat = matrix_mult(mat, scalmat)
    draw_lines(mat, screen, [255, 255, 255])

display(screen)