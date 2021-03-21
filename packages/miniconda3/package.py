# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install miniconda3-py38-4-9-2-linux-ppc64le-sh
#
# You can edit this file again by typing:
#
#     spack edit miniconda3-py38-4-9-2-linux-ppc64le-sh
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
from os.path import split

class Miniconda3(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://conda.io/miniconda.html"
    url      = "https://repo.anaconda.com/miniconda/Miniconda3-py38_4.9.2-Linux-ppc64le.sh"

    version('4.9.2', sha256="2b111dab4b72a34c969188aa7a91eca927a034b14a87f725fa8d295955364e71", 
            url='https://repo.anaconda.com/miniconda/Miniconda3-py38_4.9.2-Linux-ppc64le.sh',
            expand=False)

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['fwang2']


    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def install(self, spec, prefix):
        # peel the name of the script out of the pathname of the
        # downloaded file
        dir, script = split(self.stage.archive_file)
        bash = which('bash')
        bash(script, '-b', '-f', '-p', self.prefix)
