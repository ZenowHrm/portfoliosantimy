COLORS = {
    "degradado": "linear-gradient(0deg,rgba(40, 40, 40, 1) 0%, rgba(26, 26, 26, 1) 4%, rgba(0, 0, 0, 1) 100%)",
    "primary": "#d7d7d7",
    "light": "#eeeeee",
    "deep_gray": "#6D6D6D",
    "medium_gray": "#9d9d9d",
    "dark_bg": "#313131"
}

def hex_to_rgba(hex_color, alpha):
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return f"rgba({r}, {g}, {b}, {alpha})"