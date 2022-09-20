#passenger class is categorical and ordinal
#gender is categorical
#age is numerical

titanic <- read.csv("titanic.csv")
ls.str(titanic)
table(titanic$pclass)
