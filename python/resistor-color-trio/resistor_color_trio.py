colors_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def label(colors):
    val = 0
    ohm = "ohms"
    for i, color in enumerate(colors):
        if i == 2:
            for i in range(0, colors_list.index(color)):
                val = val * 10
            break
        val = (val * 10) + colors_list.index(color)

    if val >= 1000:
        if val >= 1000000:
            if val >= 1000000000:
                val /= 1000000000
                return str(int(val)) + " gigaohms"
            val /= 1000000
            return str(int(val)) + " megaohms"
        val /= 1000
        return str(int(val)) + " kiloohms"
    return str(val) + " ohms"

print(label(["orange", "orange", "orange"]))
