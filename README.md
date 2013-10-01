hackingarts-tweeter
===================

Turn tweets into midi events to create music


Requirements
------------

rtmidi C++ library and python wrapper:
* https://github.com/superquadratic/rtmidi-python.git
* http://www.music.mcgill.ca/~gary/rtmidi/release/rtmidi-2.0.1.tar.gz


Installation
------------

TODO.

tweeter requires that you have a twitter developer account, which is free
to set up, and that you have created an app, which can be read-only.  You
need it for the consumer key and the consumer secret.


Usage
-----

  $ $PATH_TO_TWEETER/bin/tweeter \
    <app name> <consumer key> <consumer secret> <hashtag without "#">
