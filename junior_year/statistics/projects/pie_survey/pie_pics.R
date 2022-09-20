pies <- read.csv("pie_survey.csv")
# pies - this command prints out the entire data set
pie_table = table(pies$What.s.your.favorite.kind.of.pie.)
pie_table
pie(pie_table, col = c("red", "purple", "yellow")) #not pretty by default
barplot(pie_table, col = c("blue", "brown", "orange"))
