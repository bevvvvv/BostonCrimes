---
title: "Boston Crime Data EDA"
author: "Joseph Sepich"
date: "2019-07-31"
output: 
  html_document:
    keep_md: yes
  html_notebook: default
---

# Front matter


```r
# always clean up R environment
rm(list = ls())
# load all packages here
library(mdsr) # book package of utilities
library(tidyr) # tidyverse utilities
library(lubridate) # date utility package
library(data.table) # using fread function
library(tidyverse) # utitlity package
```

# Obtaining the data

## Import data


```r
crime_data <- fread("Data/crimes-in-boston/crime.csv")
offense_codes <- fread("Data/crimes-in-boston/offense_codes.csv")
```


```r
head(crime_data)
```

```
##    INCIDENT_NUMBER OFFENSE_CODE              OFFENSE_CODE_GROUP
## 1:      I182070945          619                         Larceny
## 2:      I182070943         1402                       Vandalism
## 3:      I182070941         3410                           Towed
## 4:      I182070940         3114            Investigate Property
## 5:      I182070938         3114            Investigate Property
## 6:      I182070936         3820 Motor Vehicle Accident Response
##                           OFFENSE_DESCRIPTION DISTRICT REPORTING_AREA
## 1:                         LARCENY ALL OTHERS      D14            808
## 2:                                  VANDALISM      C11            347
## 3:                        TOWED MOTOR VEHICLE       D4            151
## 4:                       INVESTIGATE PROPERTY       D4            272
## 5:                       INVESTIGATE PROPERTY       B3            421
## 6: M/V ACCIDENT INVOLVING PEDESTRIAN - INJURY      C11            398
##    SHOOTING    OCCURRED_ON_DATE YEAR MONTH DAY_OF_WEEK HOUR   UCR_PART
## 1:          2018-09-02 13:00:00 2018     9      Sunday   13   Part One
## 2:          2018-08-21 00:00:00 2018     8     Tuesday    0   Part Two
## 3:          2018-09-03 19:27:00 2018     9      Monday   19 Part Three
## 4:          2018-09-03 21:16:00 2018     9      Monday   21 Part Three
## 5:          2018-09-03 21:05:00 2018     9      Monday   21 Part Three
## 6:          2018-09-03 21:09:00 2018     9      Monday   21 Part Three
##         STREET      Lat      Long                    Location
## 1:  LINCOLN ST 42.35779 -71.13937 (42.35779134, -71.13937053)
## 2:    HECLA ST 42.30682 -71.06030 (42.30682138, -71.06030035)
## 3: CAZENOVE ST 42.34659 -71.07243 (42.34658879, -71.07242943)
## 4:  NEWCOMB ST 42.33418 -71.07866 (42.33418175, -71.07866441)
## 5:    DELHI ST 42.27537 -71.09036 (42.27536542, -71.09036101)
## 6:  TALBOT AVE 42.29020 -71.07159 (42.29019621, -71.07159012)
```


```r
str(crime_data)
```

```
## Classes 'data.table' and 'data.frame':	319073 obs. of  17 variables:
##  $ INCIDENT_NUMBER    : chr  "I182070945" "I182070943" "I182070941" "I182070940" ...
##  $ OFFENSE_CODE       : int  619 1402 3410 3114 3114 3820 724 3301 301 3301 ...
##  $ OFFENSE_CODE_GROUP : chr  "Larceny" "Vandalism" "Towed" "Investigate Property" ...
##  $ OFFENSE_DESCRIPTION: chr  "LARCENY ALL OTHERS" "VANDALISM" "TOWED MOTOR VEHICLE" "INVESTIGATE PROPERTY" ...
##  $ DISTRICT           : chr  "D14" "C11" "D4" "D4" ...
##  $ REPORTING_AREA     : int  808 347 151 272 421 398 330 584 177 364 ...
##  $ SHOOTING           : chr  "" "" "" "" ...
##  $ OCCURRED_ON_DATE   : chr  "2018-09-02 13:00:00" "2018-08-21 00:00:00" "2018-09-03 19:27:00" "2018-09-03 21:16:00" ...
##  $ YEAR               : int  2018 2018 2018 2018 2018 2018 2018 2018 2018 2018 ...
##  $ MONTH              : int  9 8 9 9 9 9 9 9 9 9 ...
##  $ DAY_OF_WEEK        : chr  "Sunday" "Tuesday" "Monday" "Monday" ...
##  $ HOUR               : int  13 0 19 21 21 21 21 20 20 20 ...
##  $ UCR_PART           : chr  "Part One" "Part Two" "Part Three" "Part Three" ...
##  $ STREET             : chr  "LINCOLN ST" "HECLA ST" "CAZENOVE ST" "NEWCOMB ST" ...
##  $ Lat                : num  42.4 42.3 42.3 42.3 42.3 ...
##  $ Long               : num  -71.1 -71.1 -71.1 -71.1 -71.1 ...
##  $ Location           : chr  "(42.35779134, -71.13937053)" "(42.30682138, -71.06030035)" "(42.34658879, -71.07242943)" "(42.33418175, -71.07866441)" ...
##  - attr(*, ".internal.selfref")=<externalptr>
```


```r
str(offense_codes)
```

```
## Classes 'data.table' and 'data.frame':	576 obs. of  2 variables:
##  $ CODE: int  612 613 615 1731 3111 2646 2204 3810 3801 3807 ...
##  $ NAME: chr  "LARCENY PURSE SNATCH - NO FORCE" "LARCENY SHOPLIFTING" "LARCENY THEFT OF MV PARTS & ACCESSORIES" "INCEST" ...
##  - attr(*, ".internal.selfref")=<externalptr>
```

The cases of the csv are in a tidy format, but we can combine the information stored in the csv. We can also convert some data types. For instance the OCCURRED_ON_DATE field contains all the information regarding time data. We can transform this into a date time field. One question to answer after that is if shooting is a boolean type field or not.

## Remove redundant columns

Let's consolidate our time fields and our location information.


```r
crime_data_tidy <- crime_data %>%
  select(-c(YEAR,MONTH,DAY_OF_WEEK,HOUR,Location))

str(crime_data_tidy)
```

```
## Classes 'data.table' and 'data.frame':	319073 obs. of  12 variables:
##  $ INCIDENT_NUMBER    : chr  "I182070945" "I182070943" "I182070941" "I182070940" ...
##  $ OFFENSE_CODE       : int  619 1402 3410 3114 3114 3820 724 3301 301 3301 ...
##  $ OFFENSE_CODE_GROUP : chr  "Larceny" "Vandalism" "Towed" "Investigate Property" ...
##  $ OFFENSE_DESCRIPTION: chr  "LARCENY ALL OTHERS" "VANDALISM" "TOWED MOTOR VEHICLE" "INVESTIGATE PROPERTY" ...
##  $ DISTRICT           : chr  "D14" "C11" "D4" "D4" ...
##  $ REPORTING_AREA     : int  808 347 151 272 421 398 330 584 177 364 ...
##  $ SHOOTING           : chr  "" "" "" "" ...
##  $ OCCURRED_ON_DATE   : chr  "2018-09-02 13:00:00" "2018-08-21 00:00:00" "2018-09-03 19:27:00" "2018-09-03 21:16:00" ...
##  $ UCR_PART           : chr  "Part One" "Part Two" "Part Three" "Part Three" ...
##  $ STREET             : chr  "LINCOLN ST" "HECLA ST" "CAZENOVE ST" "NEWCOMB ST" ...
##  $ Lat                : num  42.4 42.3 42.3 42.3 42.3 ...
##  $ Long               : num  -71.1 -71.1 -71.1 -71.1 -71.1 ...
##  - attr(*, ".internal.selfref")=<externalptr>
```

## Cast types

Now let's convert the OCCURRED_ON_DATE field to a date field.


```r
crime_data_tidy$OCCURRED_ON_DATE <- ymd_hms(crime_data_tidy$OCCURRED_ON_DATE)

str(crime_data_tidy$OCCURRED_ON_DATE)
```

```
##  POSIXct[1:319073], format: "2018-09-02 13:00:00" "2018-08-21 00:00:00" ...
```














