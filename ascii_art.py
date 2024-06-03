import pyfiglet
print(pyfiglet.FigletFont.getFonts())
def create_ascii_art(text, font='slant'):
    """ Generates ASCII art from text using the specified font. """
    ascii_art = pyfiglet.figlet_format(text, font=font)
    return ascii_art

if __name__ == "__main__":
    input_text = input("Enter the text for ASCII art: ")
    font_choice = input("Enter the font (or leave blank for default): ")
    font_choice = font_choice if font_choice else 'slant'  

    art = create_ascii_art(input_text, font=font_choice)
    print(art)
