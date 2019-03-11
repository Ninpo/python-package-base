from setuptools import setup, find_packages
import versioneer


setup(
    name="my_package",
    description="A Description",
    author="Alex Boag-Munroe",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "attrs>=19.0.0,<20.0.0",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Database",
    ],
    entry_points={"console_scripts": ["my_package = my_package.cli:main"]},
)
