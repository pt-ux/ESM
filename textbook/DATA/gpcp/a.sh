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
fname=gpcp_v01r03_daily_
# get the data

stub=gpcp_v01r03_daily_
for year in $(seq ${year1} ${year2}); do
   file=${stub}${year}.nc
   if [ ! -f "$FILE_PATH" ]; then
       wget -q -c -P $ddir http://clima-dods.ictp.it/Users/tompkins/Observations/GPCP/v1.3/${stub}${year}.nc
   fi
done
