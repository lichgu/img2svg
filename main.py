# Created by lcg at 26.11.22
import os
from pathlib import Path

import img_prep as ip
import svg_generator as svg

root_dir = Path(os.path.dirname(__file__))
in_dir = os.path.join(root_dir, 'data/samples')
out_dir = os.path.join(root_dir, 'data/converted')

# - [OpenCV tutorial on hierarchy of contours](https://docs.opencv.org/4.x/d9/d8b/tutorial_py_contours_hierarchy.html)

if __name__ == '__main__':
    import cv2
    filepath = os.path.join(in_dir, 'seagull.jpg')
    # contour detection
    run_contour_detection = True
    if run_contour_detection:
        contours = ip.contour_detection(
            filepath, save_converted_img=True,
            out_path=os.path.join(out_dir, 'seagull_contours.png'),
            min_length=10
        )
        print(type(contours))
        print(len(contours))
        #print(contours)
    """
    # contour detection with different contour retrieval mode
    contours = ip.contour_detection(
        filepath, False, True, True,
        os.path.join(out_dir, 'seagull_contours_external.png'),
        contour_retrieval_mode=cv2.RETR_EXTERNAL
    )
    """

    # edge detection
    img_edges = ip.edge_detection(
        filepath, True, True, True,
        out_path=os.path.join(out_dir, 'seagull_edges.png'),
    )

    # svg creation
    img = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    width, height = img.shape[0:2]
    # svg (default setting)
    path = os.path.join(out_dir, 'seagull_path_default.svg')
    svg.create_svg(contours, path, width, height)
    # svg (1 color and 1 stroke width specified, no fill)
    path = os.path.join(out_dir, 'seagull_path_simple.svg')
    svg.create_svg(contours, path, width, height,
                   color='orange', stroke_width=5,
                   fill=None)
    # svg (different colors and stroke widths, no fill)
    path = os.path.join(out_dir, 'seagull_path_params.svg')
    svg.create_svg(contours, path, width, height,
                   color=['orange', 'blue'], stroke_width=[5, 7, 1],
                   fill=None)
    # svg (smaller size, image scaled and reduced)
    path = os.path.join(out_dir, 'seagull_path_small.svg')
    svg.create_svg(contours, path, width/2, height/2,
                   scale_factor=4, min_delta=10)


