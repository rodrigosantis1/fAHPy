from setuptools import setup, find_packages

setup(
    name="ahp_fuzzy_lib",
    version="0.1.0",
    description="A library for AHP and Fuzzy AHP calculations with triangular fuzzy number distribution plotting.",
    author="Seu Nome",
    author_email="seuemail@example.com",
    packages=find_packages(),
    install_requires=["numpy", "matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
