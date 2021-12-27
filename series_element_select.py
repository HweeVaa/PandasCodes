import pandas as pd


# 튜플 데이터를 시리즈로 변환하여 변수 sr에 저장
tup_data = ("휘현", "1997-01-01", "남", True)
sr = pd.Series(tup_data, index=["이름", "생년월일", "성별", "학생여부"])
print(sr)


# 원소를 1개 선택
print(sr[0])
print(sr["이름"])


# 여러개의 원소를 선택
print(sr[[1, 2]])
print("\n")
print(sr[["생년월일", "성별"]])


# 여러개의 원소를 선택(인덱스 범위지정)
print(sr[1:2])
print("\n")
print(sr["생년월일":"성별"])
