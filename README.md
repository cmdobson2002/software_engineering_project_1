# Software Engineering Project 1
This project takes in pairs of `xml` and `png` files. It parses the `xml` files and draws bounding boxes around the leaf-level elements on the corresponding UI screenshots.

### Steps for Running Project
1. Clone this repository with `git clone [repo-link]`
2. Navigate into the repository with `cd software_engineering_project_1`
3. Optionally, create a new virtual environment with `pyenv virtualenv [python-version] [venv-name]`. If you don't have pyenv installed, refer to [this guide](https://realpython.com/intro-to-pyenv/)
4. Run `pip install -r requirements.txt` to install appropriate python packages. If you don't have `pip` installed, refer to [the documentation](https://pip.pypa.io/en/stable/installation/) for installation instructions.
5. With python packages installed, run `python bounding_boxes.py`
6. Respond to the input prompts accordingly -- If you leave the inputs blank, the program will draw the bounding boxes for all `xml-png` pairs in `Programming-Assignment-Data`.
7. A new folder will be created, called `outlined_images`, which contains the UI screenshots with bounding boxes. Check the images in this folder for correctness.

### Explaination of Design
The program in `bounding_boxes.py` takes in user input for specifying the directory containing `xml-png` pairs, and also allows the user to specify a single file to parse instead of running on the entire directory. This allows the user a bit more control over the program. I included guardrails anywhere I thought they were necessary, such as checking that user-inputted files actually exist, and `try-excepting` possible points of failure like parsing XML files or saving the annotated image in local storage. 

The real functionality of parsing the files is included in the function `dig`. Using functionality provided by Python's built-in xml parser, the function iterates through all XML elements and finds those with no children, or leaf nodes. I possibly could have implemented `dig` recursively, but the `iter` function provided by Python's xml parser seemed more intuitive. 

I also defined a function for parsing the XML `bounds` attribute into an element that is decipherable to the Python Pillow package. If this code was used in a more extensive code base, I would probably define a class `Rectangle` to make the return type of `parse_out_points` less complicated, but considering this code is only being used in one file and for a single project, I think it's fine to leave as is. The choice to return a list element that held two tuples was purely driven by the fact that the Pillow package takes points in that format when drawing rectangles on images.
