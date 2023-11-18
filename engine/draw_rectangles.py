from PIL import Image, ImageDraw
import os


def draw_rectangles(image_path, rectangles, output_folder, output_name):
    # Load the image
    with Image.open(image_path) as img:
        draw = ImageDraw.Draw(img)

        # Draw rectangles
        for rect in rectangles:
            x1, x2, y1, y2 = rect
            draw.rectangle([x1, y1, x2, y2],fill="#ffffff")

        # Save the image
        output_path = os.path.join(output_folder, output_name)
        img.save(output_path)

    return output_path