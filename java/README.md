javac -cp $(dpu-pkg-config --variable=java dpu) TrivialChecksumExampleMultiRank.java  
java -cp .:$(dpu-pkg-config --variable=java dpu) TrivialChecksumExampleMultiRank