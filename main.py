import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

df16 = pd.read_csv('./Data/2016-17_teamBoxScore.csv')
df17 = pd.read_csv('./Data/2017-18_teamBoxScore.csv')
df = pd.concat([df16, df17],ignore_index=True)

df = df[["teamAbbr", "teamPTS", "teamPTS1", "teamPTS2", "teamPTS3", "teamPTS4", "teamPTS5", "opptAbbr", "opptPTS", "opptPTS1", "opptPTS2", "opptPTS3", "opptPTS4", "opptPTS5"]]

# Each pair of rows is equivalent, but reversing the first and second teams.
# Remove each second row to avoid this "duplicated" (mirrored) data.
df = df.iloc[::2, :].reset_index(drop = True)
for i in range(1, 6):
  df["ptsDiff%s" % i] = df["teamPTS%s" % i] - df["opptPTS%s" % i]
df["teamWin"] = (df["teamPTS"] > df["opptPTS"]).apply(lambda x: x and 1.0 or -1.0)
df["wentToOT"] = (df["teamPTS5"] + df["opptPTS5"]) > 0

df2 = df[['ptsDiff1','ptsDiff2','ptsDiff3','ptsDiff4','teamWin']]
print(df2.corr())

dfOT = df[['ptsDiff1','ptsDiff2','ptsDiff3','ptsDiff4','ptsDiff5','teamWin','wentToOT']]
dfOT = dfOT[dfOT['wentToOT']].drop(['wentToOT'], axis=1)
print(dfOT.corr())