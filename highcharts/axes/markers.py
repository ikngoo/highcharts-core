from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.decorators import validate_types
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.animation import AnimationOptions
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern


class AxisMarker(HighchartsMeta):
    """The triangular marker on a scalar color axis that points to the value of the
    hovered area."""

    def __init__(self, **kwargs):
        self._animation = None
        self._color = None
        self._width = None

        self.animation = kwargs.pop('animation', None)
        self.color = kwargs.pop('color', None)
        self.width = kwargs.pop('width', None)

    @property
    def animation(self) -> Optional[bool | AnimationOptions]:
        """Animation for the marker as it moves between values. If
        :obj:`None <python:None>`, defaults to ``duration: 50``.

        .. hint::

          If set to ``False``, will disable animation of the marker.

        :rtype: :class:`AnimationOptions` or :class:`bool <python:bool>` or
          :obj:`None <python:None>`
        """
        return self._animation

    @animation.setter
    def animation(self, value):
        if value is False:
            self._animation = False
        else:
            self._animation = validate_types(value, AnimationOptions)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the marker. Defaults to :obj:`None <python:None>`, which
        applies '#999999'.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        if not value:
            self._color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Gradient.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Pattern.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def width(self) -> Optional[int | float | Decimal]:
        """The width of the marker. Defaults to :obj:`None <python:None>`, which applies
        a value of ``0.01``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = validators.numeric(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'animation': as_dict.pop('animation', None),
            'color': as_dict.pop('color', None),
            'width': as_dict.pop('width', None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'animation': self.animation,
            'color': self.color,
            'width': self.width,
        }

        return untrimmed