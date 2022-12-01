# Created by lcg at 28.11.22
import numpy as np
from typing import List, Optional, Tuple, Union

import utils


def create_svg(
        contours: Tuple[np.ndarray],
        path: str,
        width: Union[float, str],
        height:  Union[float, str],
        scale_factor: float = 1,  # scaling factor
        min_delta: float = 0,  # min delta between points of paths (x- and y- direction)
        color: Union[str, List[str]] = 'black',
        stroke_width: Union[float, List[float]] = 1,
        fill: Optional[Union[str, List[str]]] = 'none',
        sep: str = ' '
):
    if not path.endswith('.svg'):
        path += '.svg'
    colors, stroke_widths, fills = utils.args2lists(len(contours), color,
                                                    stroke_width, fill)
    with open(path, 'w+') as f:
        f.write(
            f'<svg width="{width}" height="{height}" '
            f'xmlns="http://www.w3.org/2000/svg">'
        )
        for contour, color, stroke_width, fill in zip(
                contours, colors, stroke_widths, fills
        ):
            f.write(f'<path '
                    f'stroke="{color}" '
                    f'stroke-width="{stroke_width}" '
                    )
            if fill is not None:
                f.write(f'fill="{fill}"')
            f.write(f'd="M')
            x, y = contour[0][0]
            f.write(f'{int(x * scale_factor)}{sep}{int(y * scale_factor)}{sep}')
            x_tmp, y_tmp = x, y
            for i in range(1, len(contour)):
                x, y = contour[i][0]
                if abs(x-x_tmp) >= min_delta or abs(y-y_tmp) >= min_delta:
                    f.write(
                        f'{int(x * scale_factor)}{sep}{int(y * scale_factor)}{sep}'
                    )
                    x_tmp, y_tmp = x, y
            f.write('" />')
        f.write('</svg>')


