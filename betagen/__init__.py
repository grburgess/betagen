import matplotlib.pyplot as plt
from colour import Color
from betagen.utils import colorscale


class BetaGen(object):
    def __init__(self, base_dark):

        (
            self._dark,
            self._dark_highlight,
            self._mid,
            self._mid_highlight,
            self._light,
            self._light_highlight,
        ) = betagen(base_dark)


    @property
    def dark(self):

        return self._dark 

    @property
    def dark_highlight(self):

        return self._dark_highlight 


    @property
    def mid(self):

        return self._mid 

    @property
    def mid_highlight(self):

        return self._mid_highlight 

    @property
    def light(self):

        return self._light 

    @property
    def light_highlight(self):

        return self._light_highlight 


    
        
def betagen(base_dark):

    HL_scale = 0.85
    darkscale = 0.9

    dark = base_dark

    c_dark = Color(dark)

    flag = True

    counts = 0
    new_counts = 0
    while flag:

        try:
            dark_highlight = colorscale(c_dark.hex, HL_scale)

            c = Color(dark)

            c.luminance = c.luminance * 1.7
            c.saturation = c.saturation * 0.55

            mid = c.hex

            mid_highlight = colorscale(mid, HL_scale)

            c = Color(mid)

            c.luminance = c.luminance * 1.35
            c.saturation = c.saturation * 0.95

            light = c.hex

            light_highlight = colorscale(light, HL_scale)

            flag = False
        except:
            counts += 1

            if counts < 100:

                c_dark.luminance = c_dark.luminance * 0.9

            elif new_counts < 500:

                new_counts += 1
                c_dark.luminance = c_dark.luminance * 1.1

            else:

                print(c_dark.luminance)
                print(c_dark.saturation)
                raise RuntimeError("This color sucks")

            dark = c_dark.hex

    return dark, dark_highlight, mid, mid_highlight, light, light_highlight


def display(base_dark):

    dark, dark_highlight, mid, mid_highlight, light, light_highlight = betagen(
        base_dark
    )

    x = [dark, mid, light]
    xh = [dark_highlight, mid_highlight, light_highlight]

    fig, ax = plt.subplots()

    for i, c, in enumerate(xh):

        ax.hlines(i, 0, 1, colors=c, linewidth=18)
        ax.hlines(i, 0.1, 0.9, colors=x[i], linewidth=10)

    ax.set_ylim(-1, len(x))
    _despine(ax, True)


def _despine(ax, all=False):
    if all is True:
        for sp in ax.spines:
            ax.spines[sp].set_visible(False)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    else:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
