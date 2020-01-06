
# Load Packages
library(arcgisbinding)
library(sp)
library(spdep)

# Load ArcGIS License
arc.check_product()


# Load Data from ArcGIS Pro
enrich_df <- arc.open(path = 'C:/Users/thewu/OneDrive/Documents/ArcGIS/Projects/SanFrancisco/SanFrancisco.gdb/San_Fran_Crimes_Hot_Spot_Enrich_HasData')

# Select variables desired
enrich_select_df <- arc.select(object = enrich_df, fields = c('OBJECTID', 'SUM_VALUE', 'historicalpopulation_tspop10_cy', 'wealth_medval_cy', 'wealth_medhinc_cy', 'ownerrenter_renter_cy', 'businesses_n13_bus', 'businesses_n37_bus'))

# Tranform to sp dataframe
enrich_spdf <- arc.data2sp(enrich_select_df)

# Renaming Attribute names
col_names <- c("OBJECTID", "Crime_Counts",
               "Population", "Med_HomeValue", "Med_HomeIncome",
               "Renter_Count", "Grocery",
               "Restaurant")
colnames(enrich_spdf@data) <- col_names

# head(enrich_spdf@data)

# Empirical Bayes Crime Rate Analysis
n <- enrich_spdf@data$Crime_Counts
x <- enrich_spdf@data$Population
EB <- EBest (n, x)
p <- EB$raw
b <- attr(EB, "parameters")$b
a <- attr(EB, "parameters")$a
v <- a + (b/x)
v[v < 0] <- b/x
z <- (p - b)/sqrt(v)

enrich_spdf@data$EB_Rate <- z

# Save new data to ArcGIS Pro
arcgis_df <- arc.sp2data(enrich_spdf)
arc.write('C:/Users/thewu/OneDrive/Documents/ArcGIS/Projects/SanFrancisco/SanFrancisco.gdb/San_Fran_Crime_Rates', arcgis_df, shape_info = arc.shapeinfo(enrich_df))





































