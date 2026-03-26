# you need to install:
# MAC brew install (or port install)
# UBUNTU sudo apt install
#
# cdo
# wget
# ncview
# netcdf-dev (ubuntu) netcdf (brew)

year1=1998
year2=2005
ddir="/home/hp/ESM/textbook/DATA/gpcp"  # this is above the level of the python book, to not ad files to git
# get the data
wget -q -c -P $ddir http://clima-dods.ictp.it/Users/tompkins/data/cru/cru_tmax_yearmean.nc



