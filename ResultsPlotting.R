

s1_lda_3 = 36.3636363636
s1_lda_2 = 62.0689655172
s1_bayes_3 = 40.9090909091
s1_bayes_2 = 41.3793103448
s1_lg_3 = 38.6363636364
s1_lg_2 = 55.1724137931

s2_lda_3 = 22.7272727273
s2_lda_2 = 53.3333333333
s2_bayes_3 = 40.9090909091
s2_bayes_2 = 73.3333333333
s2_lg_3 = 27.2727272727
s2_lg_2 = 40.0

s3_lda_3 = 45.4545454545
s3_lda_2 = 60.0
s3_bayes_3 = 50.0
s3_bayes_2 = 73.3333333333
s3_lg_3 = 31.8181818182
s3_lg_2 = 46.6666666667

s4_lda_3 = 31.8181818182
s4_lda_2 = 20.0
s4_bayes_3 = 31.8181818182
s4_bayes_2 = 26.6666666667
s4_lg_3 = 36.3636363636
s4_lg_2 = 53.3333333333

s5_lda_3 = 50.0
s5_lda_2 = 46.6666666667
s5_bayes_3 = 36.3636363636
s5_bayes_2 = 73.3333333333
s5_lg_3 = 18.1818181818
s5_lg_2 = 33.3333333333

s6_lda_3 = 36.3636363636
s6_lda_2 = 53.3333333333
s6_bayes_3 = 13.6363636364
s6_bayes_2 = 33.3333333333
s6_lg_3 = 22.7272727273
s6_lg_2 = 60.0

all_lda_3 = 37.1428571429
all_lda_2 = 48.7179487179
all_bayes_3 = 41.4285714286
all_bayes_2 = 53.8461538462
all_lg_3 = 34.2857142857
all_lg_2 = 35.8974358974

subjects = c("Subject 1", "Subject 1", "Subject 1", 
             "Subject 2", "Subject 2", "Subject 2", 
             "Subject 3", "Subject 3", "Subject 3", 
             "Subject 4", "Subject 4", "Subject 4",
             "Subject 5", "Subject 5", "Subject 5", 
             "Subject 6", "Subject 6", "Subject 6", 
             "All subjects", "All subjects", "All subjects") 
accuracy = c(s1_lda_3, s1_bayes_3, s1_lg_3, s2_lda_3, s2_bayes_3, s2_lg_3,
             s3_lda_3, s3_bayes_3, s3_lg_3, s4_lda_3, s4_bayes_3, s4_lg_3,
             s5_lda_3, s5_bayes_3, s5_lg_3, s6_lda_3, s6_bayes_3, s6_lg_3,
             all_lda_3, all_bayes_3, all_lg_3)
accuracy = c(s1_lda_2, s1_bayes_2, s1_lg_2, s2_lda_2, s2_bayes_2, s2_lg_2,
             s3_lda_2, s3_bayes_2, s3_lg_2, s4_lda_2, s4_bayes_2, s4_lg_2,
             s5_lda_2, s5_bayes_2, s5_lg_2, s6_lda_2, s6_bayes_2, s6_lg_2,
             all_lda_3, all_bayes_3, all_lg_3)
classifier = c("LDA", "Naive Bayes", "Logistic regression",
               "LDA", "Naive Bayes", "Logistic regression",
               "LDA", "Naive Bayes", "Logistic regression",
               "LDA", "Naive Bayes", "Logistic regression",
               "LDA", "Naive Bayes", "Logistic regression",
               "LDA", "Naive Bayes", "Logistic regression",
               "LDA", "Naive Bayes", "Logistic regression")

df = data.frame(subjects, accuracy, classifier)       


ggplot(df, aes(x = classifier, y = accuracy))  + geom_bar(stat = "identity") + 
  facet_wrap(~ subjects, nrow=1) + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) + 
  geom_hline(yintercept=50, color = "red", size=2) + 
  geom_text(aes(label=round(accuracy, 1)), vjust=-0.2)
