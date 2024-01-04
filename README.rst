Data file for NMRforMD
======================

Raw trajectory files used to generate the data and figure from `nmrformd`_,
toghether with the associate LAMMPS or GROMACS input files.

.. _nmrformd: https://nmrformd.readthedocs.io

To reduce the size of the history:

.. math::

	java -jar /home/simon/Softwares/bfg-1.13.2.jar --strip-blobs-bigger-than 50M .git

	java -jar ../../../Softwares/bfg-1.13.2.jar --delete-files "*.lammpstrj" --no-blob-protection .git

	git reflog expire --expire=now --all

	git gc --prune=now --aggressive

        git push origin --force --all
