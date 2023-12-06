from PIL import Image

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def show_color(hex_code):
    rgb = hex_to_rgb(hex_code)
    img = Image.new('RGB', (100, 100), color=rgb)
    img.show()

if __name__ == "__main__":
    hex_code = input("Enter a hex code (e.g., #RRGGBB): ")
    show_color(hex_code)

