import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
import os

def dig(root, bound_list):
    for child in root:
        if len(list(child)) == 0:
            # bounds is a str -- let's do some parsing!
            bounds = child.get("bounds")
            point_one_str = bounds[:bounds.index("]")+1]
            point_two_str = bounds[bounds.index("]")+1:]
            point_one_x = int(point_one_str[1:point_one_str.index(",")])
            point_one_y = int(point_one_str[point_one_str.index(",")+1:-1])
            point_two_x = int(point_two_str[1:point_two_str.index(",")])
            point_two_y = int(point_two_str[point_two_str.index(",")+1:-1])
            bound_list.append([(point_one_x, point_one_y), (point_two_x, point_two_y)])
        else:
            dig(child, bound_list)


def main():
    xml_to_png_dict = {}
    input_path = "Programming-Assignment-Data"
    save_path = "outlined_images"
    if os.path.exists(save_path):
        for path in os.listdir(save_path):
            os.remove(path)
    else:
        os.mkdir(save_path)
    for file in os.listdir(input_path):
        file_name = os.path.splitext(file)[0]
        xml_to_png_dict[f"{file_name}.xml"] = f"{file_name}.png"

    for key in xml_to_png_dict:
        xml_tree = ET.parse(os.path.join(input_path, key))
        png_file = xml_to_png_dict[key]
        point_list = []
        dig(xml_tree.getroot(), point_list)

        with Image.open(os.path.join(input_path, png_file)) as im:
            draw = ImageDraw.Draw(im)
            for point in point_list:
                draw.rectangle(point, width=5, outline=(255, 255, 0))

            im.save(os.path.join(save_path, png_file))


if __name__ == "__main__":
    main()

