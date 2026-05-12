# ft_package

This is a sample Python package for 42's Python module exercise.

## Function

- `count_in_list(list, item)` – returns how many times `item` appears in the list.



pyproject.toml is a configuration file used in modern Python projects to define build system requirements and manage project metadata. It is part of PEP 518 and has become the standard way to specify how Python projects are built and packaged

how to use the venv
python3 -m venv venv
source venv/bin/activate
(venv) xzhang@debianxf:~/Documents/.../ex09$




rm -rf build dist *.egg-info
python3 -m build
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
