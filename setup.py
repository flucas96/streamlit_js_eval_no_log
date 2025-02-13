import setuptools
import pathlib

component_name = "streamlit_js_eval_no_logs"

# See https://docs.streamlit.io/library/components/publish
# rm -rf dist/;python3 setup.py sdist bdist_wheel;twine upload dist/*
setuptools.setup(
    name=component_name,
    version="0.1.8",
    description="A custom Streamlit component to evaluate arbitrary Javascript expressions.",
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    author=['Alireza Ghasemi', "Fabian Lucas"],
    author_email=['ghasemi.a.ir@gmail.com', "fl@msr.de"],
    url='https://github.com/aghasemi/streamlit_js_eval_no_log',
    install_requires=["streamlit>=1.0.0"],
    keywords=['Python', 'Streamlit', 'JavaScript'],
    python_requires=">=3.8",
)