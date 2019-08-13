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
crime_data <- fread("Data/tmpney_to1g.csv")
offense_codes <- fread("Data/crimes-in-boston/offense_codes.csv")
```


```r
head(crime_data)
```

```
##    INCIDENT_NUMBER OFFENSE_CODE              OFFENSE_CODE_GROUP
## 1:      I192059153         2006    Restraining Order Violations
## 2:      I192059147         3115              Investigate Person
## 3:      I192059146         3115              Investigate Person
## 4:      I192059145         3115              Investigate Person
## 5:      I192059144         3115              Investigate Person
## 6:      I192059142         3802 Motor Vehicle Accident Response
##                    OFFENSE_DESCRIPTION DISTRICT REPORTING_AREA SHOOTING
## 1: VIOL. OF RESTRAINING ORDER W ARREST       B3            441         
## 2:                  INVESTIGATE PERSON       B3            465         
## 3:                  INVESTIGATE PERSON       B3            465         
## 4:                  INVESTIGATE PERSON       B3            465         
## 5:                  INVESTIGATE PERSON       B3            465         
## 6:    M/V ACCIDENT - PROPERTY Â DAMAGE                      NA         
##       OCCURRED_ON_DATE YEAR MONTH DAY_OF_WEEK HOUR   UCR_PART
## 1: 2019-07-30 21:40:00 2019     7     Tuesday   21   Part Two
## 2: 2019-07-30 21:50:00 2019     7     Tuesday   21 Part Three
## 3: 2019-07-30 21:49:00 2019     7     Tuesday   21 Part Three
## 4: 2019-07-30 21:48:00 2019     7     Tuesday   21 Part Three
## 5: 2019-07-30 21:47:00 2019     7     Tuesday   21 Part Three
## 6: 2019-07-27 12:00:00 2019     7    Saturday   12 Part Three
##            STREET      Lat      Long                    Location
## 1: NIGHTINGALE ST 42.29540 -71.08238 (42.29540175, -71.08237834)
## 2:  BLUE HILL AVE 42.28483 -71.09137 (42.28482577, -71.09137369)
## 3:  BLUE HILL AVE 42.28483 -71.09137 (42.28482577, -71.09137369)
## 4:  BLUE HILL AVE 42.28483 -71.09137 (42.28482577, -71.09137369)
## 5:  BLUE HILL AVE 42.28483 -71.09137 (42.28482577, -71.09137369)
## 6:                      NA        NA    (0.00000000, 0.00000000)
```


```r
str(crime_data)
```

```
## Classes 'data.table' and 'data.frame':	408235 obs. of  17 variables:
##  $ INCIDENT_NUMBER    : chr  "I192059153" "I192059147" "I192059146" "I192059145" ...
##  $ OFFENSE_CODE       : int  2006 3115 3115 3115 3115 3802 801 2629 1842 3201 ...
##  $ OFFENSE_CODE_GROUP : chr  "Restraining Order Violations" "Investigate Person" "Investigate Person" "Investigate Person" ...
##  $ OFFENSE_DESCRIPTION: chr  "VIOL. OF RESTRAINING ORDER W ARREST" "INVESTIGATE PERSON" "INVESTIGATE PERSON" "INVESTIGATE PERSON" ...
##  $ DISTRICT           : chr  "B3" "B3" "B3" "B3" ...
##  $ REPORTING_AREA     : int  441 465 465 465 465 NA 400 358 485 624 ...
##  $ SHOOTING           : chr  "" "" "" "" ...
##  $ OCCURRED_ON_DATE   : chr  "2019-07-30 21:40:00" "2019-07-30 21:50:00" "2019-07-30 21:49:00" "2019-07-30 21:48:00" ...
##  $ YEAR               : int  2019 2019 2019 2019 2019 2019 2019 2019 2019 2019 ...
##  $ MONTH              : int  7 7 7 7 7 7 7 7 7 7 ...
##  $ DAY_OF_WEEK        : chr  "Tuesday" "Tuesday" "Tuesday" "Tuesday" ...
##  $ HOUR               : int  21 21 21 21 21 12 21 21 21 21 ...
##  $ UCR_PART           : chr  "Part Two" "Part Three" "Part Three" "Part Three" ...
##  $ STREET             : chr  "NIGHTINGALE ST" "BLUE HILL AVE" "BLUE HILL AVE" "BLUE HILL AVE" ...
##  $ Lat                : num  42.3 42.3 42.3 42.3 42.3 ...
##  $ Long               : num  -71.1 -71.1 -71.1 -71.1 -71.1 ...
##  $ Location           : chr  "(42.29540175, -71.08237834)" "(42.28482577, -71.09137369)" "(42.28482577, -71.09137369)" "(42.28482577, -71.09137369)" ...
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
## Classes 'data.table' and 'data.frame':	408235 obs. of  12 variables:
##  $ INCIDENT_NUMBER    : chr  "I192059153" "I192059147" "I192059146" "I192059145" ...
##  $ OFFENSE_CODE       : int  2006 3115 3115 3115 3115 3802 801 2629 1842 3201 ...
##  $ OFFENSE_CODE_GROUP : chr  "Restraining Order Violations" "Investigate Person" "Investigate Person" "Investigate Person" ...
##  $ OFFENSE_DESCRIPTION: chr  "VIOL. OF RESTRAINING ORDER W ARREST" "INVESTIGATE PERSON" "INVESTIGATE PERSON" "INVESTIGATE PERSON" ...
##  $ DISTRICT           : chr  "B3" "B3" "B3" "B3" ...
##  $ REPORTING_AREA     : int  441 465 465 465 465 NA 400 358 485 624 ...
##  $ SHOOTING           : chr  "" "" "" "" ...
##  $ OCCURRED_ON_DATE   : chr  "2019-07-30 21:40:00" "2019-07-30 21:50:00" "2019-07-30 21:49:00" "2019-07-30 21:48:00" ...
##  $ UCR_PART           : chr  "Part Two" "Part Three" "Part Three" "Part Three" ...
##  $ STREET             : chr  "NIGHTINGALE ST" "BLUE HILL AVE" "BLUE HILL AVE" "BLUE HILL AVE" ...
##  $ Lat                : num  42.3 42.3 42.3 42.3 42.3 ...
##  $ Long               : num  -71.1 -71.1 -71.1 -71.1 -71.1 ...
##  - attr(*, ".internal.selfref")=<externalptr>
```


```r
crime_data_tidy %>%
  write.csv("Data/tidy_crimes.csv")
```

## Cast types

Now let's convert the OCCURRED_ON_DATE field to a date field.


```r
crime_data_tidy$OCCURRED_ON_DATE <- ymd_hms(crime_data_tidy$OCCURRED_ON_DATE)

str(crime_data_tidy$OCCURRED_ON_DATE)
```

```
##  POSIXct[1:408235], format: "2019-07-30 21:40:00" "2019-07-30 21:50:00" ...
```














