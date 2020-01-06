
# Load Packages
library(arcgisbinding)
library(sp)
library(spdep)

# Load ArcGIS License
arc.check_product()


# Load Data from ArcGIS Pro
rate_df <- arc.open(path = 'C:/Users/thewu/OneDrive/Documents/ArcGIS/Projects/SanFrancisco/SanFrancisco.gdb/San_Fran_Crime_Rates')


# Select the Data
rate_select_df <- arc.select(rate_df, fields = c("OBJECTID", "Crime_Counts", "Population", "Med_HomeValue", "Med_HomeIncome", "Renter_Count", "Grocery", "Restaurant", "EB_Rate"))






















