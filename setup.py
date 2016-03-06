from setuptools import setup, find_packages

setup(
    name="pycephes",
    version="0.1.0",
    description="Python wrapper for CEPHES using CFFI and numba",
    author="Juan Luis Cano",
    author_email="hello@juanlu.space",
    url="https://github.com/poliastro/pycephes",
    packages=find_packages("src"),
    package_dir={"": "src"},
    setup_requires=["cffi>=1.0.0"],
    install_requires=[
        "numpy",
        "cffi>=1.0.0",
        "numba>=0.23",
        #"cephes==2014.10.04",
    ],
    tests_require=[
        "pytest",
        "scipy",
    ],
    cffi_modules=["src/_cffi_src/build_hyper.py:ffi"],
)
