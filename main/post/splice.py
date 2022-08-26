
#    Nev Aerospace flight controller built for the raspberry PI ecosystem
#     Copyright (C) 2022  StoneMcYT (https://github.com/StoneMcYT)

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.



#Mhm only run this when the flight is done and the data is set in the DB and ready to be processed d
#Please make sure you are mentally sane when running this
def DataSpliceMethod():
    print("Data Splice shall begain now")
    DataStatus = []
    print(DataStatus)
    for x in DataStatus:
        if DataStatus[2][x] << DataStatus[2][x+1]:
            print("Test ")
