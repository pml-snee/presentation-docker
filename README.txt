use build.sh to create the docker image
use run.sh   to run the container on the input file in the storage directory
use run-interactively.sh to start the container but leave you at a command prompt

When run, container will read in the netCDF file in ~/storage and write a new file containing all of names of the variables in the input.nc
