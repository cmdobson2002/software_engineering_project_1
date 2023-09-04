import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from PIL import Image, ImageDraw
import os
from typing import List


def parse_out_points(bounds: str) -> [(int, int), (int, int)]:
    """
    Helper function to parse out the points to draw a bounding rectangle
    :param bounds: String representation of the bounds of the form "[0,0][1440,2368]"
    :return: List element of the form [(0, 0), (1440, 2368)]
    """

    # Get the individual points based on the index of the first closing bracket
    point_one_str = bounds[: bounds.index("]") + 1]
    point_two_str = bounds[bounds.index("]") + 1 :]

    # Get the x,y coordinates of each point
    point_one_x = int(point_one_str[1 : point_one_str.index(",")])
    point_one_y = int(point_one_str[point_one_str.index(",") + 1 : -1])
    point_two_x = int(point_two_str[1 : point_two_str.index(",")])
    point_two_y = int(point_two_str[point_two_str.index(",") + 1 : -1])

    return [(point_one_x, point_one_y), (point_two_x, point_two_y)]


def dig(root: Element) -> List:
    """
     Function to find all leaf-elements in a given xml file.
    :param root: The root element of the XML file
    :return: rect_list, which is a list holding elements of the form [(x1, y1), (x2, y2)]
    """
    rect_list = []

    # Loop through each element in the XML tree
    for child in root.iter():

        # Shorthand for if the element child has no child elements
        if not len(child):

            # We found a leaf-element -- Get the bounds attribute from the XML node
            bounds = child.get("bounds")

            # The variable bounds is a string, so we need to do some parsing
            rect_elem = parse_out_points(bounds)

            # Append the two points as tuples since Pillow takes tuples when drawing rectangles
            rect_list.append(rect_elem)

    return rect_list


def main():

    # Folder names for assignment data, output direectory
    input_path = "Programming-Assignment-Data"
    save_path = "outlined_images"

    # Delete any existing images in the output directory
    if os.path.exists(save_path):
        for path in os.listdir(save_path):
            os.remove(os.path.join(save_path, path))
    else:
        # If the output directory doesn't exist, create it
        os.mkdir(save_path)

    # Dictionary to hold mappings {xml_file : png_file}
    xml_to_png_dict = {}

    # Go through each file in the input data directory
    for file in os.listdir(input_path):
        name_ext = os.path.splitext(file)

        # Get the file name, extension
        file_name = name_ext[0]
        file_ext = name_ext[1]

        # If it's an XML file, add a dictionary entry mapping to the corresponding PNG
        if file_ext == ".xml":
            xml_to_png_dict[f"{file_name}.xml"] = f"{file_name}.png"

    # For each XML file in the dictionary
    for key in xml_to_png_dict:

        # Build the path to the XML file
        xml_path = os.path.join(input_path, key)

        # Try to load the XML file into a parser
        try:
            xml_tree = ET.parse(xml_path)
            print(f"Parsing xml file {xml_path}")

        except Exception as e:
            print(e)
            print(f"Couldn't parse XML for {xml_path}. Trying next file.")
            continue

        # Pass in XML root and coordinate list to function which will get all leaf-elements
        rect_list = dig(xml_tree.getroot())

        # Get the corresponding PNG file
        png_file = xml_to_png_dict[key]

        # Build the path for the png image
        image_path = os.path.join(input_path, png_file)

        # If our png image does not exist, move to the next file
        if not os.path.exists(image_path):
            print("Couldn't find png file for drawing. Trying next file.")
            continue

        # Open the file with Pillow
        with Image.open(image_path) as im:
            draw = ImageDraw.Draw(im)

            # For each bounding box, draw it on the image
            for point in rect_list:
                draw.rectangle(point, width=5, outline=(255, 255, 0))

            # Save the image to local output directory
            im.save(os.path.join(save_path, png_file))


if __name__ == "__main__":
    main()
