from octodiary import __version__
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fr:
    requirements = fr.read().splitlines()


setup(
    name="octodiary",
    version=__version__,
    author="OctoDiary",
    description="Python библиотека для использования API: МЭШ / Моя Школа.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OctoDiary/OctoDiary-py",
    packages=find_packages(),
    license="Apache License 2.0",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords=["octodiary", "api", "мэш", "моя школа", "myschool", "myschool api" "mesh"],
    python_requires=">=3.9",
    project_urls={
        "Bug Reports": "https://github.com/OctoDiary/OctoDiary-py/issues",
        "Source": "https://github.com/OctoDiary/OctoDiary-py",
        "Organization": "https://github.com/OctoDiary",
        "Telegram-Channel": "https://t.me/OctoDiary",
    }
)
