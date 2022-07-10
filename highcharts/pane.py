from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern


class PaneBackground(HighchartsMeta):
    """Configuration of the background items to display within a :class:`Pane`."""

    def __init__(self, **kwargs):
        self._background_color = None
        self._border_color = None
        self._border_width = None
        self._class_name = None
        self._inner_radius = None
        self._outer_radius = None
        self._shape = None

        self.background_color = kwargs.pop('background_color',
                                           constants.DEFAULT_PANE_BACKGROUND.get('background_color'))
        self.border_color = kwargs.pop('border_color',
                                       constants.DEFAULT_PANE_BACKGROUND.get('border_color'))
        self.border_width = kwargs.pop('border_width',
                                       constants.DEFAULT_PANE_BACKGROUND.get('border_width'))
        self.class_name = kwargs.pop('class_name',
                                     constants.DEFAULT_PANE_BACKGROUND.get('class_name'))
        self.inner_radius = kwargs.pop('inner_radius',
                                       constants.DEFAULT_PANE_BACKGROUND.get('inner_radius'))
        self.outer_radius = kwargs.pop('outer_radius',
                                       constants.DEFAULT_PANE_BACKGROUND.get('outer_radius'))
        self.shape = kwargs.pop('shape',
                                constants.DEFAULT_PANE_BACKGROUND.get('shape'))

    @property
    def background_color(self) -> Optional[str | Gradient | Pattern]:
        f"""The background color or gradient for the pane. Defaults to
        ``'{constants.DEFAULT_PANE_BACKGROUND.get('background_color')}'``.

        :returns: The backgorund color for the outer chart area.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        if not value:
            self._background_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._background_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._background_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._background_color = Gradient.from_dict(value)
                else:
                    self._background_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._background_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._background_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._background_color = Pattern.from_dict(value)
                else:
                    self._background_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._background_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        f"""The color of the pane border. Defaults to
        ``'{constants.DEFAULT_PANE_BACKGROUND.get('border_color')}'``.

        :returns: The color of the pane's border.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        if not value:
            self._border_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._border_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._border_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Gradient.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._border_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._border_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Pattern.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._border_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        f"""The border width (in pixels) applied to the outer chart border. Defaults to
        ``{constants.DEFAULT_PANE_BACKGROUND.get('border_width')}``.

        :returns: The border width to apply to the pane.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value, allow_empty = True)

    @property
    def class_name(self) -> Optional[str]:
        f"""A classname to apply styling using CSS. Defaults to
        ``'{constants.DEFAULT_PANE_BACKGROUND.get('class_name')}'``.

        :returns: The classname to apply to enable styling via CSS.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def inner_radius(self) -> Optional[int | float | Decimal | str]:
        f"""The inner radius (in pixels if numeric or as a percentage string) applied to
        the pane. Defaults to ``{constants.DEFAULT_PANE_BACKGROUND.get('inner_radius')}``.

        :returns: The inner radius of the pane background.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._inner_radius

    @inner_radius.setter
    def inner_radius(self, value):
        if value is None or value == '':
            self._inner_radius = None
        else:
            try:
                self._inner_radius = validators.string(value, allow_empty = True)
            except ValueError:
                self._inner_radius = validators.numeric(value, allow_empty = True)

    @property
    def outer_radius(self) -> Optional[int | float | Decimal | str]:
        f"""The outer radius (in pixels if numeric or as a percentage string) applied to
        a circular pane background. Defaults to
        ``{constants.DEFAULT_PANE_BACKGROUND.get('outer_radius')}``.

        :returns: The outer radius of the pane background.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._outer_radius

    @outer_radius.setter
    def outer_radius(self, value):
        if value is None or value == '':
            self._outer_radius = None
        else:
            try:
                self._outer_radius = validators.string(value, allow_empty = True)
            except ValueError:
                self._outer_radius = validators.numeric(value, allow_empty = True)

    @property
    def shape(self) -> Optional[str]:
        f"""The shape of the pane background. Defaults to
        ``'{constants.DEFAULT_PANE_BACKGROUND.get('shape')}'``.

        Accepts:

          * ``'circle'``
          * ``'solid'``
          * ``'arc'``

        .. note::

          When ``'solid'``, the background is circular.
          When ``'arc'``, the background extends only from the min to the max of the value
          axis.

        :rtype: :class:`str` or :obj:`None <python:None>`
        """
        return self._shape

    @shape.setter
    def shape(self, value):
        if not value:
            self._shape = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['circle', 'solid', 'arc']:
                raise errors.HighchartsValueError(f'shape expects "circle", "solid", or '
                                                  f'"arc". Received: {value}')
            self._shape = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'background_color': as_dict.pop('backgroundColor',
                                            constants.DEFAULT_PANE_BACKGROUND.get('background_color')),
            'border_color': as_dict.pop('borderColor',
                                        constants.DEFAULT_PANE_BACKGROUND.get('border_color')),
            'border_width': as_dict.pop('borderWidth',
                                        constants.DEFAULT_PANE_BACKGROUND.get('border_width')),
            'class_name': as_dict.pop('className',
                                      constants.DEFAULT_PANE_BACKGROUND.get('class_name')),
            'inner_radius': as_dict.pop('innerRadius',
                                        constants.DEFAULT_PANE_BACKGROUND.get('inner_radius')),
            'outer_radius': as_dict.pop('outerRadius',
                                        constants.DEFAULT_PANE_BACKGROUND.get('outer_radius')),
            'shape': as_dict.pop('shape', constants.DEFAULT_PANE_BACKGROUND.get('shape'))
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'backgroundColor': self.background_color,
            'borderColor': self.border_color,
            'borderWidth': self.border_width,
            'className': self.class_name,
            'innerRadius': self.inner_radius,
            'outerRadius': self.outer_radius,
            'shape': self.shape
        }

        return self.trim_dict(untrimmed)


class Pane(HighchartsMeta):
    """The pane serves as a container for axes and backgrounds for circular gauges and
    polar charts."""

    def __init__(self, **kwargs):
        self._background = None
        self._center = None
        self._end_angle = None
        self._inner_size = None
        self._size = None
        self._start_angle = None

        self.background = kwargs.pop('background', None)
        self.center = kwargs.pop('center', constants.DEFAULT_PANE.get('center'))
        self.end_angle = kwargs.pop('end_angle', constants.DEFAULT_PANE.get('end_angle'))
        self.inner_size = kwargs.pop('inner_size', constants.DEFAULT_PANE.get('inner_size'))
        self.size = kwargs.pop('size', constants.DEFAULT_PANE.get('size'))
        self.start_angle = kwargs.pop('start_angle', constants.DEFAULT_PANE.get('start_angle'))

    @property
    def background(self) -> Optional[List[PaneBackground]]:
        """An array of background items for the pane.

        :rtype: :class:`list <python:list>` of :class:`PaneBackground`, or
          :obj:`None <python:None>`
        """
        return self._background

    @background.setter
    @class_sensitive(PaneBackground, force_iterable = True)
    def background(self, value):
        self._background = value

    @property
    def center(self) -> Optional[List[str | int]]:
        f"""The center of a polar chart or angular gauge, given as an array of ``[x, y]``
        positions. Positions can be given as integers that transform to pixels, or as
        percentages of the plot area size. Defaults to
        ``{constants.DEFAULT_PANE.get('center')}``.

        :returns: Collection of positions, or :obj:`None <python:None>`
        :rtype: :class:`list <python:list>` of two-item :class:`list <python:list>`
          where each item is either a :class:`str <python:str>` or
          :class:`int <python:int>`, or :obj:`None <python:None>`
        """
        return self._center

    @center.setter
    def center(self, value):
        if not value:
            self._center = None
        else:
            value = [validators.iterable(x,
                                         allow_empty = False,
                                         minimum_length = 2,
                                         maximum_length = 2)
                     for x in validators.iterable(value, allow_empty = False)]
            for item in value:
                try:
                    item[0] = validators.string(item[0])
                except ValueError:
                    item[0] = validators.numeric(item[0])
                try:
                    item[1] = validators.string(item[1])
                except ValueError:
                    item[1] = validators.numeric(item[1])

            self._center = value

    @property
    def end_angle(self) -> Optional(int | float | Decimal):
        """The end angle of the polar X axis or gauge value axis, given in degrees where
        ``0`` is north. Defaults to :meth:`Pane.start_angle` if :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._end_angle

    @end_angle.setter
    def end_angle(self, value):
        self._end_angle = validators.numeric(value, allow_empty = True)

    @property
    def inner_size(self) -> Optional[int | float | Decimal | str]:
        f"""The inner size of the pane, either as a number defining pixels, or a
        percentage defining a percentage of the pane's size. Defaults to
        ``{constants.DEFAULT_PANE.get('inner_size')}``.

        :rtype: numeric or :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._inner_size

    @inner_size.setter
    def inner_size(self, value):
        if not value:
            self._inner_size = None
        else:
            try:
                self._inner_size = validators.string(value)
            except ValueError:
                self._inner_size = validators.numeric(value)

    @property
    def size(self) -> Optional[int | float | Decimal | str]:
        f"""The size of the pane, either as a number defining pixels, or a
        percentage defining a percentage of the pane's size. Defaults to
        ``{constants.DEFAULT_PANE.get('size')}``.

        :rtype: numeric or :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._size

    @size.setter
    def size(self, value):
        if not value:
            self._size = None
        else:
            try:
                self._size = validators.string(value)
            except ValueError:
                self._size = validators.numeric(value)

    @property
    def start_angle(self) -> Optional(int | float | Decimal):
        f"""The start angle of the polar X axis or gauge value axis, given in degrees where
        ``0`` is north. Defaults to ``{constants.DEFAULT_PANE.get('start_angle')}``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._start_angle

    @start_angle.setter
    def start_angle(self, value):
        self._start_angle = validators.numeric(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'background': as_dict.pop('background', None),
            'center': as_dict.pop('center', constants.DEFAULT_PANE.get('center')),
            'end_angle': as_dict.pop('endAngle', constants.DEFAULT_PANE.get('end_angle')),
            'inner_size': as_dict.pop('innerSize', constants.DEFAULT_PANE.get('inner_size')),
            'size': as_dict.pop('size', constants.DEFAULT_PANE.get('size')),
            'start_angle': as_dict.pop('startAngle', constants.DEFAULT_PANE.get('start_angle'))
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'background': self.background,
            'center': self.center,
            'endAngle': self.end_angle,
            'innerSize': self.inner_size,
            'size': self.size,
            'startAngle': self.start_angle
        }

        return self.trim_dict(untrimmed)
