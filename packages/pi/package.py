# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.util.executable import which

class Pi(Package):
    """pi is a suite of high performant file system tool such as profile and copying"""
    #homepage = "https://github.com/fwang2/pi"
    # git = "https://github.com/fwang2/pi.git"
    # version = ('master', )
    
    url      = "https://github.com/fwang2/pi/archive/v0.1-alpha4.tar.gz"
    version('0.1-alpha4', sha256='86502b408e6ef04422204cc92e7a6a520c5d4f9817d0a3af3d11906696841de4')

    depends_on('go@1.11')

    def install(self, spec, prefix):
        go = which('go')
        go('build')
        mkdir(prefix.bin)
        install('pi', prefix.bin)
