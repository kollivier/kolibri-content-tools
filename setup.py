import io
from setuptools import find_packages, setup

requirements = [
    "beautifulsoup4",
    "django>=1.11",
    "django-mptt==0.11.0",
    "jsonfield==2.0.2",
    "le_utils",
    "PyPDF2",
    "whoosh"
]

setup(
    name="kolibri-content-tools",
    packages = find_packages(),
    version="0.1.0",
    description="LE-Content contains common functions for working with content across LE products.",
    install_requires=requirements,
    license="MIT",
    url="https://github.com/learningequality/kolibri-content-tools",
    download_url="https://github.com/learningequality/kolibri-content-tools/releases",
    keywords="le-content le_content LE content kolibri studio ricecooker content curation",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
    ],
    author="Kevin Ollivier",
    author_email="kevin@learningequality.org",
)
