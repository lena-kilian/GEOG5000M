library(tidyverse)

data <- read.csv('Footprint_data.csv')



headers = colnames(data)
headers[1] = 'LSOA_code'

colnames(data) = headers

#write.csv(data, 'Data/Data/co2_bristol_data.csv')
