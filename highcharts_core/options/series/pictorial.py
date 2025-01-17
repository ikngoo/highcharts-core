from decimal import Decimal
from typing import Optional, List

from validator_collection import validators

from highcharts_core.options.series.base import SeriesBase
from highcharts_core.options.series.data.cartesian import CartesianData
from highcharts_core.options.plot_options.pictorial import PictorialOptions
from highcharts_core.utility_functions import mro__to_untrimmed_dict
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.decorators import class_sensitive
from highcharts_core.utility_classes.ast import AttributeObject


class PictorialPaths(HighchartsMeta):
    """Configuration of pictorial point images."""
    
    def __init__(self, **kwargs):
        self._definition = None
        self._max = None
        
        self.definition = kwargs.get('definition', None)
        self.max = kwargs.get('max', None)
        
    @property
    def definition(self) -> Optional[AttributeObject]:
        """Defines the path to be drawn, corresponding to the SVG ``d`` attribute.
        
        :rtype: :class:`AttributeObject <highcharts_core.utility_classes.ast.AttributeObject>` or
          :obj:`None <python:None>`
        """
        return self._definition
    
    @definition.setter
    @class_sensitive(AttributeObject)
    def definition(self, value):
        self._definition = value
        
    @property
    def max(self) -> Optional[int | float | Decimal]:
        """Determines height of the image. It is the ratio of ``yAxis.max`` to the ``paths.max``.
        
        Defaults to the maximum value of the y-axis.
        
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max
    
    @max.setter
    def max(self, value):
        self._max = validators.numeric(value, allow_empty = True)


    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'definition': as_dict.get('definition', None),
            'max': as_dict.get('max', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'definition': self.definition,
            'max': self.max
        }

        return untrimmed


class PictorialSeries(SeriesBase, PictorialOptions):
    """Options to configure a Pictorial series.

    A pictorial series uses vector images to represent the data, with the data's shape
    determined by the ``path`` parameter.

    .. figure:: ../../../_static/pictorial-example.png
      :alt: Pictorial Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._paths = None
        
        self.paths = kwargs.get('paths', None)
        
        super().__init__(**kwargs)

    @property
    def data(self) -> Optional[List[CartesianData]]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`CartesianData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              series = PictorialSeries()
              series.data = [0, 5, 3, 5]

            A one-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a ``y``-value, with its corresponding ``x``
            value automatically determined.

            If :meth:`PictorialSeries.point_start` is :obj:`None <python:None>`, ``x``
            values will begin at ``0``. Otherwise, they will start at ``point_start``.

            If :meth:`PictorialSeries.point_interval` is :obj:`None <python:None>`, ``x``
            values will be incremented by ``1``. Otherwise, they will be incremented
            by the value of ``point_interval``.

          .. tab:: 2D Collection

            .. code-block::

              series = PictorialSeries()
              # Category X-axis
              series.data = [
                  ['Category A', 0],
                  ['Category B', 5],
                  ['Category C', 3],
                  ['Category D', 5]
              ]

              # Numerical X-axis
              series.data = [
                  [9, 0],
                  [1, 5],
                  [2, 3],
                  [7, 5]
              ]

            A two-dimensional collection of values. Each member of the collection will be
            interpreted as an ``x`` and ``y`` pair. The ``x`` value can be a
            :class:`str <python:str>`, :class:`date <python:datetime.date>`,
            :class:`datetime <python:datetime.datetime>`, or numeric value.

            .. note::

              If the ``x`` value is a :class:`str <python:str>`, it will be interpreted
              as the name of the data point.

          .. tab:: Object Collection

            A one-dimensional collection of :class:`CartesianData` objects.

        :rtype: :class:`list <python:list>` of :class:`CartesianData` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not value:
            self._data = None
        else:
            self._data = CartesianData.from_array(value)

    @property
    def paths(self) -> Optional[PictorialPaths]:
        """Configuration of the point image.
        
        :rtype: :class:`PictorialPaths <highcharts_core.options.series.pictorial.PictorialPaths>` or
          :obj:`None <python:None>`
        """
        return self._paths
    
    @paths.setter
    @class_sensitive(PictorialPaths)
    def paths(self, value):
        self._paths = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'allow_point_select': as_dict.get('allowPointSelect', None),
            'animation': as_dict.get('animation', None),
            'class_name': as_dict.get('className', None),
            'clip': as_dict.get('clip', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'custom': as_dict.get('custom', None),
            'dash_style': as_dict.get('dashStyle', None),
            'data_labels': as_dict.get('dataLabels', None),
            'description': as_dict.get('description', None),
            'enable_mouse_tracking': as_dict.get('enableMouseTracking', None),
            'events': as_dict.get('events', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'keys': as_dict.get('keys', None),
            'label': as_dict.get('label', None),
            'linked_to': as_dict.get('linkedTo', None),
            'marker': as_dict.get('marker', None),
            'on_point': as_dict.get('onPoint', None),
            'opacity': as_dict.get('opacity', None),
            'point': as_dict.get('point', None),
            'point_description_formatter': as_dict.get('pointDescriptionFormatter', None),
            'selected': as_dict.get('selected', None),
            'show_checkbox': as_dict.get('showCheckbox', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'skip_keyboard_navigation': as_dict.get('skipKeyboardNavigation', None),
            'sonification': as_dict.get('sonification', None),
            'states': as_dict.get('states', None),
            'sticky_tracking': as_dict.get('stickyTracking', None),
            'threshold': as_dict.get('threshold', None),
            'tooltip': as_dict.get('tooltip', None),
            'turbo_threshold': as_dict.get('turboThreshold', None),
            'visible': as_dict.get('visible', None),

            'animation_limit': as_dict.get('animationLimit', None),
            'boost_blending': as_dict.get('boostBlending', None),
            'boost_threshold': as_dict.get('boostThreshold', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'connect_nulls': as_dict.get('connectNulls', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'data_sorting': as_dict.get('dataSorting', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_width': as_dict.get('lineWidth', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'step': as_dict.get('step', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'color_axis': as_dict.get('colorAxis', None),
            'connect_ends': as_dict.get('connectEnds', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'negative_color': as_dict.get('negativeColor', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'stacking': as_dict.get('stacking', None),
            
            'depth': as_dict.get('depth', None),
            'edge_color': as_dict.get('edgeColor', None),
            'edge_width': as_dict.get('edgeWidth', None),
            'grouping': as_dict.get('grouping', None),
            'group_padding': as_dict.get('groupPadding', None),
            'group_z_padding': as_dict.get('groupZPadding', None),
            'max_point_width': as_dict.get('maxPointWidth', None),
            'min_point_length': as_dict.get('minPointLength', None),
            'point_padding': as_dict.get('pointPadding', None),
            'point_range': as_dict.get('pointRange', None),
            'point_width': as_dict.get('pointWidth', None),

            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),
            
            'paths': as_dict.get('paths', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'paths': self.paths
        }
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
