# Software Engineering Project 1
This project takes in pairs of `xml` and `png` files. It parses the `xml` files and draws bounding boxes around the leaf-level elements on the corresponding UI screenshots. 

### Steps for running project
1. Clone this repository with `git clone [repo-link]`
2. Navigate into the repository with `cd software_engineering_project_1`
3. Run `pip install -r requirements.txt` to install appropriate python packages. If you don't have `pip` installed, refer to (the documentation)[https://pip.pypa.io/en/stable/installation/] for installation instructions.
4. With python packages installed, run `python bounding_boxes.py`
5. A new folder will be created, called `outlined_images`, which contains the UI screenshots with bounding boxes. Check the images in this folder for correctness.
