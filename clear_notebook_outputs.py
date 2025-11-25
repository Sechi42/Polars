import json
import sys

def clear_notebook_outputs(notebook_path):
    """Clear all outputs and execution counts from a Jupyter notebook."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Clear outputs and execution counts
    cells_cleared = 0
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'code':
            if cell.get('outputs'):
                cell['outputs'] = []
                cells_cleared += 1
            if 'execution_count' in cell:
                cell['execution_count'] = None
    
    # Write back
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print(f"✓ Cleared outputs from {cells_cleared} cells in {notebook_path}")
    return cells_cleared

if __name__ == '__main__':
    notebook_path = sys.argv[1] if len(sys.argv) > 1 else 'Chapter_16/Notebook_16.ipynb'
    clear_notebook_outputs(notebook_path)
