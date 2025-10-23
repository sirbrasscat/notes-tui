"""
Setup configuration for notes-tui package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="notes-tui",
    version="0.1.0",
    author="sirbrasscat",
    description="Terminal User Interface for Personal Markdown Notebook System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sirbrasscat/notes-tui",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business",
        "Topic :: Text Editors",
    ],
    python_requires=">=3.8",
    install_requires=[
        "textual>=0.35.0",
        "rich>=13.0.0",
        "pyyaml>=6.0",
        "click>=8.1",
        "pygments>=2.15",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4",
            "pytest-asyncio>=0.21.0",
            "black>=23.0",
            "flake8>=6.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "notes-tui=notes_tui:main",
        ],
    },
)
