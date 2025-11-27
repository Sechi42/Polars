mod expression;

use pyo3::types::{PyAnyMethods, PyModule};
use pyo3::{pymodule, Bound, PyResult};
use pyo3_polars::PolarsAllocator;

#[global_allocator]
static ALLOC: PolarsAllocator = PolarsAllocator::new();

#[pymodule]
fn polars_geo(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.setattr("__version__", env!("CARGO_PKG_VERSION"))?;
    Ok(())
}