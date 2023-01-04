# img2svg
Some quick python utility functions to
- detect contours (and edges) from images using cv2
- create svg images (defined by paths)

### Usage

Import svg generator:

    >>> import svg_generator as svg_gen

Create a svg using the default settings:

    >>> svg_gen.create_svg(contours, path, width, height)

The file will is stored at the location specified by the `path` argument.

To create a svg, the contours of the image must be known. To extract them from an existing image (e.g. JPG) the `countour_detection` function provided in `img_prep.py` can be used.

    >>> import img_prep as ip
    >>> contours = ip.contour_detection(
            filepath, 
            min_length=10
        )

The `min_length` argument is used to restrict the returned contours to those `>= min_length` to clean up the resulting svg file. See the `img_prep.py` for further options.

Further options to modify the generated svg file:

    >>> # new color and stroke width specified (same for all contours), no fill
    >>> svg.create_svg(contours, path, width, height,
                   color='orange', stroke_width=5,
                   fill=None)

    >>> # different colors and stroke widths for contours, no fill
    >>> svg.create_svg(contours, path, width, height,
                   color=['orange', 'blue'], stroke_width=[5, 7, 1],
                   fill=None)

    >>> # smaller size, image scaled and reduced
    >>> svg.create_svg(contours, path, width/2, height/2,
                   scale_factor=4, min_delta=10)


### References
- [Wikipedia SVG](https://en.wikipedia.org/wiki/SVG)
- [OpenCV findContours() documentation](https://docs.opencv.org/4.x/d3/dc0/group__imgproc__shape.html#gadf1ad6a0b82947fa1fe3c3d497f260e0)
- [OpenCV Canny() documentation](https://docs.opencv.org/4.x/dd/d1a/group__imgproc__feature.html#ga04723e007ed888ddf11d9ba04e2232de)
- [Quick contour and edge detection tutorial using cv2](https://medium.com/@tejas9723/contour-detection-edge-detection-with-opencv-96a74097e1f6)
- [OpenCV tutorial on hierarchy of contours](https://docs.opencv.org/4.x/d9/d8b/tutorial_py_contours_hierarchy.html)
