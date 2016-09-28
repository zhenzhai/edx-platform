from setuptools import setup

setup(
    name="sandbox-packages",
    version="0.2.43",
    packages=[
        "loncapa",
        "verifiers",
        "hint",
        "hint.hint_class",
        "hint.hint_class_helpers",
        "hint.hint_class_helpers.expr_parser"
    ],
    py_modules=[
        "eia",
    ],
    install_requires=[
    ],
)
