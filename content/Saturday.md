Title: pip install 
Date: 2017-03-25 11:41
Category: Tech

##Install packages from:

PyPI (and other indexes) using requirement specifiers.
VCS project urls.
Local project directories.
Local or remote source archives.
pip also supports installing from "requirements files", which provide an easy way to specify a whole environment to be installed.

Overview
Pip install has several stages:

Identify the base requirements. The user supplied arguments are processed here.
Resolve dependencies. What will be installed is determined here.
Build wheels. All the dependencies that can be are built into wheels.
Install the packages (and uninstall anything being upgraded/replaced).
Argument Handling
When looking at the items to be installed, pip checks what type of item each is, in the following order:

Project or archive URL.
Local directory (which must contain a setup.py, or pip will report an error).
Local file (a sdist or wheel format archive, following the naming conventions for those formats).
A requirement, as specified in PEP 440.
Each item identified is added to the set of requirements to be satisfied by the install.

##Working Out the Name and Version
For each candidate item, pip needs to know the project name and version. For wheels (identified by the .whl file extension) this can be obtained from the filename, as per the Wheel spec. For local directories, or explicitly specified sdist files, the setup.py egg_info command is used to determine the project metadata. For sdists located via an index, the filename is parsed for the name and project version (this is in theory slightly less reliable than using the egg_info command, but avoids downloading and processing unnecessary numbers of files).

##Any URL may use the #egg=name syntax (see VCS Support) to explicitly state the project name.