install.packages("palmerpenguins")
library(palmerpenguins)
install.packages("summarytools")
summary(penguins)
View(penguins)

#Fechas y horas
#Cargar los paquetes tidyverse y lubridate

install.packages("tidyverse")
# carga los paquetes tidyverse y lubridate 
library(tidyverse)
library(lubridate)
today()
now()
ymd("2021-01-20")
ymd(20210120)
ymd_hms("2021-01-20 20:11:59")

#Marcos de datos
data.frame(x = c(1, 2, 3) , y = c(1.5, 5.5, 7.5))

#Crear, copiar y eliminar archivos en R.
dir.create ("destination_folder")

file.create ("new_text_file.txt")
file.create ("new_word_file.docx")
file.create ("new_csv_file.csv")

#Eliminar Archivos

unlink ("new_csv_file.csv")

#Matrices 

matrix(c(0:8), nrow = 9)
matrix(c(0:8), ncol = 9)
