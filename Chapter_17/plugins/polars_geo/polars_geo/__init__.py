from pathlib import Path
import polars as pl
from polars.plugins import register_plugin_function
from polars.type_aliases import IntoExpr

PLUGIN_PATH = Path(__file__).parent

def point_in_polygon(point: IntoExpr, polygon: IntoExpr) -> pl.Expr:
	return register_plugin_function(
		plugin_path=PLUGIN_PATH,
		args=[point, polygon],
		function_name="point_in_polygon",
		is_elementwise=True,
	)

def haversine_distance(from_point: IntoExpr, to_point: IntoExpr) -> pl.Expr:
	return register_plugin_function(
		plugin_path=PLUGIN_PATH,
		args=[from_point, to_point],
		function_name="haversine_distance",
		is_elementwise=True,
	)

@pl.api.register_expr_namespace("geo")
class GeoNamespace:
	def __init__(self, expr: pl.Expr):
		self._expr = expr
	
	def point_in_polygon(self, polygon: IntoExpr) -> pl.Expr:
		return point_in_polygon(self._expr, polygon)
	
	def haversine_distance(self, to_point: IntoExpr) -> pl.Expr:
		return haversine_distance(self._expr, to_point)