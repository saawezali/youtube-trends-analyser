#!/usr/bin/env python3
"""
Setup script for YouTube Analytics Dashboard
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="youtube-trends-analyser",
    version="1.0.0",
    author="Saawez Ali",
    author_email="sayyedsaawezali@gmail.com",
    description="A powerful, real-time YouTube analytics dashboard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saawezali/youtube-trends-analyser",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Multimedia :: Video",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "flake8>=3.8.0",
            "black>=21.0.0",
            "bandit>=1.7.0",
            "safety>=1.10.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "youtube-analytics=app:main",
        ],
    },
    keywords="youtube analytics dashboard streamlit data-visualization api",
    project_urls={
        "Bug Reports": "https://github.com/saawezali/youtube-trends-analyser/issues",
        "Source": "https://github.com/saawezali/youtube-trends-analyser",
        "Documentation": "https://github.com/saawezali/youtube-trends-analyser#readme",
    },
)
