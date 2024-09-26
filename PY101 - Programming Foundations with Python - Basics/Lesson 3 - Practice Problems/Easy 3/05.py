def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False

def is_color_valid_v1(color):
    return color == 'blue' or color == 'green'

def is_color_valid_v2(color):
    return color in ['blue', 'green']
