"""Build all published artifacts in their dependency order, without network access."""
import runpy
from pathlib import Path

for script in ('build_catalog.py', 'build_showcase.py', 'build_reference_gallery.py', 'build_image25_gallery.py', 'build_repository.py'):
    runpy.run_path(str(Path(__file__).with_name(script)), run_name='__main__')
