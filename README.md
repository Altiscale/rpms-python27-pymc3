# python27-pymc3

This builds the pymc3 package for python27 scl.  Rebuilding is not straight forward.  Set these
parameters in the build job:

> RPM = pymc3
>
> DEFINES = build_number $BUILD_NUMBER,dist .alti6,scl_prefix python27-,scl python27
>
> ROOT = centos6.7-python27-x86_64
>
> REPO_NAME = rpms-python27-pymc3

All other parameters can use defaults.
