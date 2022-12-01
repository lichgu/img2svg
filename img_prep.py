# Created by lcg at 27.11.22
import cv2
import numpy as np
from typing import Tuple

import utils


def contour_detection(
        img_path: str,
        show_img: bool = False,
        show_converted_img: bool = False,
        save_converted_img: bool = False,
        out_path: str = 'contour.png',
        threshold: float = 225,
        contour_retrieval_mode: int = cv2.RETR_TREE,
        contour_approx_mode: int = cv2.CHAIN_APPROX_SIMPLE,
        min_length: int = 1,
) -> Tuple[np.ndarray]:
    utils.assert_file_exists(img_path)
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(img_grey, threshold, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(binary, contour_retrieval_mode,
                                           contour_approx_mode)

    if min_length > 1:
        contours = _select_contours_by_length(contours, min_length)

    if show_img:
        _show_image(img_grey, 'image')
    img_contours = None
    if show_converted_img or save_converted_img:
        img_contours = _create_contour_image(contours, img)
    if show_converted_img:
        _show_image(img_contours, 'contours')
    if save_converted_img:
        cv2.imwrite(out_path, img_contours)
    return contours


def edge_detection(
        img_path: str,
        show_img: bool = False,
        show_converted_img: bool = False,
        save_converted_img: bool = False,
        out_path: str = 'edges.png',
        canny_lower_limit=150,
        canny_upper_limit=200,
) -> np.ndarray:
    utils.assert_file_exists(img_path)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    # blur image if necessary
    # kernel_size = (5, 5)  # Gaussian kernel size
    # sigma = 20  # Gaussian kernel standard deviation in X and Y direction
    # img = cv2.GaussianBlur(img, kernel_size, sigmaX=sigma, sigmaY=sigma)
    # _show_image(img, 'blurred image')
    img_edges = cv2.Canny(img, canny_lower_limit, canny_upper_limit)
    if show_img:
        _show_image(img, 'image')
    if show_converted_img:
        _show_image(img_edges, 'edges')
    if save_converted_img:
        cv2.imwrite(out_path, img_edges)
    return img_edges


def _select_contours_by_length(contours: Tuple[np.ndarray], min_length: int
                               ) -> Tuple[np.ndarray]:
    return tuple([c for c in contours if c.shape[0] >= min_length])


def _show_image(img: np.ndarray, label: str = ''):
    print('Press key to continue.')
    cv2.imshow(label, img)
    cv2.waitKey(0)


def _create_contour_image(contours: Tuple[np.ndarray], img: np.ndarray
                          ) -> np.ndarray:
    img_contours = np.zeros(img.shape)
    cv2.drawContours(img_contours, contours, -1, (255, 255, 255), 3)
    return img_contours
