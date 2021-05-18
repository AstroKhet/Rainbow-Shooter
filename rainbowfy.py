
def colour_spread(n):
    def dec_to_hex(dec):
        """Converts base 10 to valid hexadecimal for tbg hex input, where max value = 255"""
        hexadecimal = str(hex(dec))[2:]

        if len(hexadecimal) < 2:
            hexadecimal = "0" + hexadecimal

        return hexadecimal

    def hexafy(tpl):
        """Converts RGB list/tuple into valid hex color code"""
        hex_code = "#"
        for e in tpl:
            hex_code += dec_to_hex(e)
        return hex_code
    
    """Spreads colours evenly amongst a range of colours, starting from #ff0000 and ending with #ff0000"""
    if n <= 2:
        return ["#ff0000"] * n

    minus = 1530 / (n - 1)

    def_color = {1: [255, 0, 0], 2: [255, 255, 0], 3: [0, 255, 0], 4: [0, 255, 255], 5: [0, 0, 255], 6: [255, 0, 255]}
    color = [255, 0, 0]
    colors = ["#ff0000"]

    disposed = 0
    for i in range(n - 2):
        bef_state = disposed // 255 + 1
        disposed += minus
        state = disposed // 255 + 1
        if bef_state != state:
            color = def_color[state]

        if state == 1:
            color[1] = round(disposed - 255 * (state - 1))
        elif state == 2:
            color[0] = round(255 - (disposed - 255 * (state - 1)))
        elif state == 3:
            color[2] = round(disposed - 255 * (state - 1))
        elif state == 4:
            color[1] = round(255 - (disposed - 255 * (state - 1)))
        elif state == 5:
            color[0] = round(disposed - 255 * (state - 1))
        elif state == 6:
            color[2] = round(255 - (disposed - 255 * (state - 1)))

        colors.append(hexafy(color))

    return colors + ["#ff0000"]
