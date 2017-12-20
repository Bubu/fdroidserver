
<a name="build-status"></a>

| CI Builds                |  fdroidserver | buildserver | fdroid build --all | publishing tools |
|--------------------------|:-------------:|:-----------:|:------------------:|:----------------:|
| Debian                   | [![fdroidserver status on Debian](https://gitlab.com/fdroid/fdroidserver/badges/master/build.svg)](https://gitlab.com/fdroid/fdroidserver/builds) | [![buildserver status](https://jenkins.debian.net/job/reproducible_setup_fdroid_build_environment/badge/icon)](https://jenkins.debian.net/job/reproducible_setup_fdroid_build_environment) | [![fdroid build all status](https://jenkins.debian.net/job/reproducible_fdroid_build_apps/badge/icon)](https://jenkins.debian.net/job/reproducible_fdroid_build_apps/) | [![fdroid build all status](https://jenkins.debian.net/job/reproducible_fdroid_test/badge/icon)](https://jenkins.debian.net/job/reproducible_fdroid_test/) |
| macOS & Ubuntu/LTS       | [![Build Status](https://travis-ci.org/Bubu/fdroidserver.svg?branch=master)](https://travis-ci.org/Bubu/fdroidserver) | | | |


# F-Droid Server

Server for [F-Droid](https://f-droid.org), the Free Software repository system
for Android.

The F-Droid server tools provide various scripts and tools that are
used to maintain the main
[F-Droid application repository](https://f-droid.org/packages).  You
can use these same tools to create your own additional or alternative
repository for publishing, or to assist in creating, testing and
submitting metadata to the main repository.

For documentation, please see <https://f-droid.org/docs/>, or you can
find the source for the documentation in
[fdroid/fdroid-website](https://gitlab.com/fdroid/fdroid-website).


### What is F-Droid?

F-Droid is an installable catalogue of FOSS (Free and Open Source Software)
applications for the Android platform. The client makes it easy to browse,
install, and keep track of updates on your device.


### Installing

There are many was to install _fdroidserver_, they are documented on
the website:
https://f-droid.org/docs/Installing_the_Server_and_Repo_Tools

All sorts of other documentation lives there as well.


### Drozer Scanner

There is a new feature under development that can scan any APK in a
repo, or any build, using Drozer.  Drozer is a dynamic exploit
scanner, it runs an app in the emulator and runs known exploits on it.

This setup requires specific versions of two Python modules:
_docker-py_ 1.9.0 and _requests_ older than 2.11.  Other versions
might cause the docker-py connection to break with the containers.
Newer versions of docker-py might have this fixed already.

For Debian based distributions:

	apt-get install libffi-dev libssl-dev python-docker

## Translation

Everything can be translated.  See
[Translation and Localization](https://f-droid.org/docs/Translation_and_Localization)
for more info.
[![translation status](https://hosted.weblate.org/widgets/f-droid/-/fdroidserver/multi-auto.svg)](https://hosted.weblate.org/engage/f-droid/?utm_source=widget)
