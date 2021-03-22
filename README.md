# Spack


- [Spack](#spack)
  - [Prep Spack](#prep-spack)
  - [Set default compiler](#set-default-compiler)
  - [Using a different install tree](#using-a-different-install-tree)
  - [Spack Cheatsheet](#spack-cheatsheet)
  - [3rd Party Repo](#3rd-party-repo)
  - [Create New Packages](#create-new-packages)
  - [Leverage existing packages](#leverage-existing-packages)
  - [Make the Spack module loadable](#make-the-spack-module-loadable)
  - [Example: install pi on Summit](#example-install-pi-on-summit)

The following note is about using `spack` to manage 3rd party packages on
OLCF's Summit (ppc64le) and Andes (x86_64).


## Prep Spack

Download and unzip [a current Spack release](https://github.com/spack/spack/releases)

    ln -sf spack-0.16.1 spack
    export PATH=$HOME/spack/bin:$PATH
  
Now we have `spack` command.

## Set default compiler

The first thing we want to do is compiler configuration. This can be platform
specific. For example, on Summit, XL is the pre-loaded default compiler. To
check which compilers are available:

    spack compilers


With your desired compiler loaded, you can run the following command:

    spack compiler add

Spack will locate and add the compiler information to
`~/.spack/linux/compilers.yaml`.

The list can be fine tuned by:

    spack config edit compilers    


## Using a different install tree

This is done by putting `config.yaml` to `.spack`:

    cat .spack/config.yaml
    config:
        install_tree: /sw/aaims
        module_roots:
            tcl:    /sw/aaims/spack/modules
            lmod:   /sw/aaims/spack/lmod

## Spack Cheatsheet

The following is a list of frequently used spack commands:

```
spack list pkg_name                                # search package
spack install pkg_name                             # install package
spack install profbuf ^cmake@3.9.2 %gcc@6.4.0      # use existing setup cmake; gcc-ver
```


## 3rd Party Repo

There is a
[discussion](https://spack.readthedocs.io/en/latest/repositories.html) on
maintaining separate repo for Spack.
For example: 

```
$ mkdir ~/aaims-spack-repo
$ cd aaims-spack-repo; mkdir packages
$ cat repo.yaml
repo:
  namespace: aaims
``` 

Once this structure is established, you can add this repo by:

```
spack repo add ~/aaims-spack-repo
spack repo list
```

You can edit the repo list directly through: `.spack/linux/repos.yaml`.  Note
that you this `repos.yaml` is different from per repo set up.


## Create New Packages


    spack create https://github.com/fwang2/pi/archive/v0.1-alpha.tar.gz



## Leverage existing packages

This is accomplished through `packages.yaml`. For example:


    packages:
    # Core externals
    cmake:
        buildable: false
        modules:
        cmake@3.9.2: cmake/3.9.2
        cmake@3.6.1: cmake/3.6.1

    go:
        buildable: false
        modules:
        go@1.11: go/1.11

## Make the Spack module loadable

The [module](https://spack-tutorial.readthedocs.io/en/latest/tutorial_modules.html) discussion can be found here:

Add to the module search:

    module use /sw/exp9/spack/modules/[linux-rhel7-sandybridge]

You can be more specific about the target:

    module load pi-0.1-alpha3-gcc-4.8.5-dfenpn7

This is a bit verbose.

I have put in the following in the `.spack/modules.yaml` file:

    modules:
    tcl:
        hash_length: 0
        naming_scheme: '{name}/{version}'

in for a shorter and more readable name.

## Example: install pi on Summit

step 0: On summit, the correct arch is, linux-rhel7-power9le. This can be checked by `spack arch`. gcc 4.8.5 can only do power8, for power9 optimization, we need gcc 6.4.0 (default), and we can specify this compiler on command line by:

    spack install pi %gcc@6.4.0

step 2: make sure we use the correct module

    module use /sw/aaims/spack/modules/linux-rhel7-power9le

step 3: now we can load

    module load pi





