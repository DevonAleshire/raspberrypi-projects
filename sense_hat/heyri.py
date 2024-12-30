from sense_hat import SenseHat
from time import sleep
import colorsys

# Initialize Sense HAT
sense = SenseHat()

def generate_rainbow_colors(steps=36):
    """Generate a list of rainbow colors."""
    colors = []
    for i in range(steps):
        hue = i / steps
        rgb = colorsys.hsv_to_rgb(hue, 1, 1)  # Convert HSV to RGB
        colors.append(tuple(int(c * 255) for c in rgb))  # Scale to 0-255
    return colors

def scroll_message_with_rainbow(message, speed=0.1):
    """Scroll a message across the Sense HAT LED matrix with rainbow colors."""
    rainbow_colors = generate_rainbow_colors()
    color_index = 0

    for i in range(len(message) * 8 + 8):  # Extra 8 for scrolling out
        sense.clear()  # Clear the display

        # Determine the current color from the rainbow
        current_color = rainbow_colors[color_index]
        color_index = (color_index + 1) % len(rainbow_colors)

        # Display the scrolling message
        sense.show_message(message, text_colour=current_color, scroll_speed=speed)

        sleep(speed)  # Adjust scroll speed if needed

# Main program
if __name__ == "__main__":
    try:
        # Scroll "HEYRI" in rainbow colors
        scroll_message_with_rainbow("HEYRI", speed=0.08)
    except KeyboardInterrupt:
        sense.clear()  # Clear the display on exit
