import numpy as np
import matplotlib.pyplot as plt
import colorspacious as cs

def okhsl_to_srgb_hex(h, s, l):
    # Convert OKHSL to JzAzBz
    jzazbz = cs.cspace_convert([h, s, l], from_space="JzAzBz", to_space="sRGB1")
    # Convert JzAzBz to sRGB and scale to [0, 255]
    srgb = np.clip(np.array(jzazbz) * 255, 0, 255).astype(int)
    # Convert to Hex
    return '#{:02x}{:02x}{:02x}'.format(*srgb)

def generate_palette(hue, saturation, lightness_scale):
    palette = []
    for l in lightness_scale:
        hex_color = okhsl_to_srgb_hex(hue, saturation, l)
        palette.append(hex_color)
    return palette

def save_palette_as_image(palette, filename):
    fig, ax = plt.subplots(1, len(palette), figsize=(len(palette), 1))
    for i, color in enumerate(palette):
        ax[i].imshow([[color]])
        ax[i].axis('off')
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    hue = 145  # Green
    saturation = 90
    lightness_scale = np.linspace(0, 100, 11)  # From 0 to 100 in 10 steps

    palette = generate_palette(hue, saturation, lightness_scale)
    print(palette)

    save_palette_as_image(palette, "green_palette.png")
