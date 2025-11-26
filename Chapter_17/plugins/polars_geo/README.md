# Polars Geo Plugin

A custom Polars plugin implementing geospatial operations using the Rust `geo` crate.

## Features

- **Point-in-Polygon**: Check if a point falls within a polygon boundary
- **Haversine Distance**: Calculate the great-circle distance between two points on Earth

## Installation

The plugin is compiled and installed using `maturin`:

```bash
cd Chapter_17/plugins/polars_geo
maturin develop --release
```

## Project Structure

```
polars_geo/
├── Cargo.toml              # Rust package configuration
├── src/
│   ├── lib.rs             # Module initialization
│   └── expression.rs      # Geospatial functions implementation
├── polars_geo/
│   └── __init__.py        # Python bindings and namespace registration
└── test_geo_plugin.py     # Test script
```

## Usage

### Import the Plugin

```python
import polars as pl
import polars_geo
```

### Using the Custom Namespace

```python
df = pl.DataFrame({
    "point": [[1.0, 1.0], [2.5, 2.5]],
    "polygon": [
        [[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]],
        [[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]],
    ],
    "destination": [[2.0, 2.0], [3.0, 3.0]],
})

# Check if points are inside polygons
result = df.select(
    pl.col("point").geo.point_in_polygon(pl.col("polygon")).alias("is_inside")
)

# Calculate Haversine distance in meters
result = df.select(
    pl.col("point").geo.haversine_distance(pl.col("destination")).alias("distance_m")
)
```

### Using Direct Function Calls

```python
# Alternative: use functions directly
result = df.select(
    polars_geo.point_in_polygon(pl.col("point"), pl.col("polygon")),
    polars_geo.haversine_distance(pl.col("point"), pl.col("destination"))
)
```

## Data Format

### Points
Points should be represented as lists of two floats `[longitude, latitude]` or `[x, y]`:
```python
[[1.0, 1.0], [2.0, 2.0]]
```

### Polygons
Polygons should be represented as lists of coordinate lists:
```python
[[[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]]]
```
Note: The first and last points should be the same to close the polygon.

## Implementation Details

### Rust Components

#### Helper Functions
- `extract_point()`: Parses a Polars Series into a `geo::Point`
- `extract_polygon()`: Parses a nested Polars Series into a `geo::Polygon`
- `geo_point_in_polygon()`: Core logic for point-in-polygon check
- `geo_haversine_distance()`: Core logic for distance calculation

#### Exported Functions
- `point_in_polygon()`: Polars expression returning Boolean
- `haversine_distance()`: Polars expression returning Float64

### Python Components

#### Registration
The `__init__.py` file registers both functions using `register_plugin_function` and creates a custom `.geo` namespace using `@pl.api.register_expr_namespace`.

## Dependencies

### Rust
- `geo`: Geospatial algorithms and data structures
- `polars`: Polars internals
- `pyo3`: Python bindings
- `pyo3-polars`: Polars plugin support

### Python
- `polars >= 1.0.0`

## Performance

The plugin is compiled in release mode with full optimizations enabled. Operations are:
- **Element-wise**: Processes each row independently for maximum parallelism
- **Amortized iteration**: Uses efficient iteration over nested structures
- **Zero-copy**: Leverages Polars' memory layout directly

## Testing

Run the test script to verify functionality:

```bash
python test_geo_plugin.py
```

Expected output:
- Point-in-polygon checks return Boolean values
- Haversine distances return values in meters
- Both namespace and direct function calls work correctly

## Examples

### Example 1: Parks and Locations
```python
parks_df = pl.DataFrame({
    "park_name": ["Central Park", "City Park"],
    "boundary": [
        [[-73.98, 40.77], [-73.97, 40.77], [-73.97, 40.78], [-73.98, 40.78], [-73.98, 40.77]],
        [[-74.00, 40.75], [-73.99, 40.75], [-73.99, 40.76], [-74.00, 40.76], [-74.00, 40.75]],
    ],
    "location": [[-73.975, 40.775], [-73.995, 40.755]]
})

# Check if locations are inside parks
result = parks_df.select(
    pl.col("park_name"),
    pl.col("location").geo.point_in_polygon(pl.col("boundary")).alias("inside")
)
```

### Example 2: Distance Calculations
```python
routes_df = pl.DataFrame({
    "from": [[-73.935, 40.730], [-118.243, 34.052]],  # NYC, LA
    "to": [[-0.127, 51.507], [-77.036, 38.907]]       # London, DC
})

# Calculate distances
result = routes_df.select(
    pl.col("from").geo.haversine_distance(pl.col("to")).alias("distance_meters")
)
```

## References

- Based on "Python Polars: The Definitive Guide" - Chapter 17
- Rust `geo` crate documentation: https://docs.rs/geo/
- Polars plugins guide: https://docs.pola.rs/user-guide/expressions/plugins/

## License

Same as the parent project.
