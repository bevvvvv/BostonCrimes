---
title: "Time Tracking EDA"
author: "Joseph Sepich"
date: "2019-10-16"
output: 
  html_document:
    keep_md: yes
  html_notebook: default
---

# Background

I have begun tracking how I spend my time. I can export those records into a relational table that are imported here. What can I discover about my time management? How much time do I allocate to work compared to leisure? Let's find out.


```
## -- Attaching packages ---------------------------------------------------------------------------------------------- tidyverse 1.2.1 --
```

```
## v ggplot2 3.1.0     v purrr   0.2.5
## v tibble  2.0.1     v dplyr   0.7.8
## v tidyr   0.8.3     v stringr 1.3.1
## v readr   1.3.1     v forcats 0.4.0
```

```
## -- Conflicts ------------------------------------------------------------------------------------------------- tidyverse_conflicts() --
## x dplyr::filter() masks stats::filter()
## x dplyr::lag()    masks stats::lag()
```

```
## 
## Attaching package: 'data.table'
```

```
## The following objects are masked from 'package:dplyr':
## 
##     between, first, last
```

```
## The following object is masked from 'package:purrr':
## 
##     transpose
```

```
## 
## Attaching package: 'lubridate'
```

```
## The following objects are masked from 'package:data.table':
## 
##     hour, isoweek, mday, minute, month, quarter, second, wday,
##     week, yday, year
```

```
## The following object is masked from 'package:base':
## 
##     date
```

# Inspect data


```r
time_table <- fread("./Data/time_data_10_16.csv")
```


```r
str(time_table)
```

```
## Classes 'data.table' and 'data.frame':	55 obs. of  9 variables:
##  $ Domain          : chr  "Standard" "Standard" "Standard" "Standard" ...
##  $ Project         : chr  "Hope" "Hope" "Commute" "APO" ...
##  $ Task            : chr  "TV" "Homework" "Walk" "Meeting" ...
##  $ Details         : logi  NA NA NA NA NA NA ...
##  $ Start           : chr  "2019-10-14 17:51" "2019-10-14 18:42" "2019-10-14 19:27" "2019-10-14 19:43" ...
##  $ End             : chr  "2019-10-14 18:42" "2019-10-14 19:27" "2019-10-14 19:43" "2019-10-14 20:55" ...
##  $ TimeZone        : chr  "UTC-4:00" "UTC-4:00" "UTC-4:00" "UTC-4:00" ...
##  $ Duration        : chr  "0:51" "0:45" "0:16" "1:12" ...
##  $ Decimal Duration: num  0.85 0.75 0.267 1.2 0.2 ...
##  - attr(*, ".internal.selfref")=<externalptr>
```


```r
head(time_table, 10)
```

```
##       Domain  Project     Task Details            Start              End
##  1: Standard     Hope       TV      NA 2019-10-14 17:51 2019-10-14 18:42
##  2: Standard     Hope Homework      NA 2019-10-14 18:42 2019-10-14 19:27
##  3: Standard  Commute     Walk      NA 2019-10-14 19:27 2019-10-14 19:43
##  4: Standard      APO  Meeting      NA 2019-10-14 19:43 2019-10-14 20:55
##  5: Standard Personal    Email      NA 2019-10-14 20:55 2019-10-14 21:07
##  6: Standard      APO Scouting      NA 2019-10-14 21:19 2019-10-14 21:28
##  7: Standard Personal    Games      NA 2019-10-14 21:29 2019-10-14 21:36
##  8: Standard Personal       TV      NA 2019-10-14 21:49 2019-10-14 22:25
##  9: Standard Personal    Games      NA 2019-10-14 22:25 2019-10-14 23:12
## 10: Standard Personal       TV      NA 2019-10-14 23:12 2019-10-14 23:31
##     TimeZone Duration Decimal Duration
##  1: UTC-4:00     0:51        0.8500000
##  2: UTC-4:00     0:45        0.7500000
##  3: UTC-4:00     0:16        0.2666667
##  4: UTC-4:00     1:12        1.2000000
##  5: UTC-4:00     0:12        0.2000000
##  6: UTC-4:00     0:09        0.1500000
##  7: UTC-4:00     0:07        0.1166667
##  8: UTC-4:00     0:36        0.6000000
##  9: UTC-4:00     0:47        0.7833333
## 10: UTC-4:00     0:19        0.3166667
```


```r
tail(time_table, 10)
```

```
##       Domain  Project                 Task Details            Start
##  1: Standard Personal            Housework      NA 2019-10-16 07:25
##  2: Standard  Commute                  Bus      NA 2019-10-16 07:33
##  3: Standard     Work                  ARL      NA 2019-10-16 07:58
##  4: Standard  Commute                  Bus      NA 2019-10-16 09:37
##  5: Standard Personal             Bathroom      NA 2019-10-16 10:03
##  6: Standard      APO             Scouting      NA 2019-10-16 10:07
##  7: Standard  Commute                 Walk      NA 2019-10-16 10:37
##  8: Standard Personal                 Food      NA 2019-10-16 10:45
##  9: Standard Personal                Email      NA 2019-10-16 11:14
## 10: Standard Personal Programming Projects      NA 2019-10-16 11:24
##                  End TimeZone Duration Decimal Duration
##  1: 2019-10-16 07:33 UTC-4:00     0:08      0.133333333
##  2: 2019-10-16 07:58 UTC-4:00     0:25      0.416666667
##  3: 2019-10-16 09:37 UTC-4:00     1:39      1.650000000
##  4: 2019-10-16 10:03 UTC-4:00     0:26      0.433333333
##  5: 2019-10-16 10:07 UTC-4:00     0:04      0.066666667
##  6: 2019-10-16 10:37 UTC-4:00     0:30      0.500000000
##  7: 2019-10-16 10:45 UTC-4:00     0:08      0.133333333
##  8: 2019-10-16 11:14 UTC-4:00     0:29      0.483333333
##  9: 2019-10-16 11:24 UTC-4:00     0:10      0.166666667
## 10: 2019-10-16 11:24 UTC-4:00     0:00      0.009166667
```

# Overall Time Spent


## Time spent per Task


```r
time_table %>%
  group_by(Task, Project) %>%
  summarise(total_duration = sum(`Decimal Duration`)) %>%
  ggplot(aes(x=reorder(Task, total_duration),y=total_duration,fill=Project)) +
    geom_bar(stat='identity') +
    coord_flip() +
    xlab('Task Name') +
    ylab('Duration in Hours') +
    ggtitle('Total Task Duration')
```

![](TrackingExploration_files/figure-html/unnamed-chunk-6-1.png)<!-- -->

## Time spen per Project


```r
time_table %>%
  group_by(Project) %>%
  summarise(total_duration = sum(`Decimal Duration`)) %>%
  ggplot(aes(x=reorder(Project, total_duration),y=total_duration)) +
    geom_bar(stat='identity') +
    coord_flip() +
    xlab('Project Name') +
    ylab('Duration in Hours') +
    ggtitle('Total Project Duration')
```

![](TrackingExploration_files/figure-html/unnamed-chunk-7-1.png)<!-- -->















