import os
import sys

sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
)

from sou import E_compute  # noqa:

print(sys.path)


def test_E_compute():
    default_values = {
        "item": 1,
        "rib_hight": 1,
        "alpha_v": 1,
        "lambda_rib": 1,
        "rib_wall_thickness": 1,
        "dp_rib": 1,
        "d_rib": 1,
    }
    E_res = E_compute(**default_values)
    assert E_res == 0.6281834549054397
