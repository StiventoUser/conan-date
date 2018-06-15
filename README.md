# conan-date

[ ![Download](https://api.bintray.com/packages/vkrapivin/conan/date%3Avkrapivin/images/download.svg) ](https://bintray.com/vkrapivin/conan/date%3Avkrapivin/_latestVersion)
[![Build Status](https://travis-ci.org/StiventoUser/conan-date.svg?branch=testing%2F2.4)](https://travis-ci.org/StiventoUser/conan-date)
[![Build status](https://ci.appveyor.com/api/projects/status/nqjr5e8s4f3h9oag?svg=true)](https://ci.appveyor.com/project/StiventoUser/conan-date)

[Conan.io](https://conan.io) package for [HowardHinnant's date](https://github.com/HowardHinnant/date) project
 
The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/vkrapivin/conan/date%3Avkrapivin).

## For Users: Use this package

### Basic setup

    $ conan install date/0.54@vkrapivin/testing

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    date/2.4@vkrapivin/testing

    [generators]
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## For Packagers: Publish this Package

The example below shows the commands used to publish to bincrafters conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly.

## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create date/testing

## Add Remote

    $ conan remote add vkrapivin https://api.bintray.com/conan/vkrapivin/conan 

## Upload

    $ conan upload date/2.4@vkrapivin/testing --all -r vkrapivin

## License
[LICENSE_TYPE](LICENSE)
