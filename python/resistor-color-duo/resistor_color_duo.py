colors_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def value(colors):
    val = 0
    for i, color in enumerate(colors):
        if i == 2:
            break
        val = (val * 10) + colors_list.index(color)
    return val