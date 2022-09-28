[![Python Versions](https://img.shields.io/pypi/pyversions/pyqlib.svg?logo=python&logoColor=white)](https://pypi.org/project/pyqlib/#files)
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-lightgrey)](https://pypi.org/project/pyqlib/#files)

# About Project

[Gaia catalogs](https://www.cosmos.esa.int/web/gaia/release) are queried using ADQL, a query language very similar to SQL. In the latest data release (DR3), Gaia includes a mass estimate for the observed stars.

This project was developed to perform a query on the masses determined by Gaia. With these data, comparisons are made with the masses determined by me, using a new method of mass determination, which can be consulted [here](https://repositorio.unifei.edu.br/jspui/handle/123456789/3349).

The results of the comparisons are visually expressed in two graphs relating the masses, so that we can study possible systematic differences.

# Run

In this project it is possible to compare open clusters individually or as a whole sample. Such objects are in the “results_eDR3_likelihood_2022” folder.

In the [main.py](https://github.com/ander-son-almeida/open-clusters-mass-query/blob/master/main.py) file we have two parameters that assume boolean values: 1) “all_cluster” if set to “True” compares the mass of all clusters and 2) “cluster_target”, if set to “True” automatically activates “cluster_name”, that the user can manually enter the name of the open cluster. Both boolean values cannot be the same, it is up to the user to decide which analysis to select.

## E**xample of results**

![all_clusterr_git](https://user-images.githubusercontent.com/70342250/192856889-bb72c007-b3eb-4626-88d9-7bfef918decb.png)

![pleiades_git](https://user-images.githubusercontent.com/70342250/192856896-b3721b41-e549-40bb-8a6c-67a736775c5c.png)

# R**equirements**

- Numpy
- Pandas
- Matplotlib
- Astroquery
