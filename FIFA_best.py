import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_csv("C:\\Users\\DELL\\Desktop\\FullData.csv")
del df['National_Kit']

#best Goalkeeper#
#weights
a=0.5
b=1
c=2
d=3
#goal keeping charecteristics
df["gk_Shot_Stopper"]=(b*df.Reactions + b*df.Composure + a*df.Speed + a*df.Strength + c*df.Jumping + b*df.GK_Positioning + c*df.GK_Diving + b*df.GK_Handling + d*df.GK_Reflexes)/(2*a+4*b+2*c+1*d)
df["gk_Sweeper"]=(b*df.Reactions + b*df.Composure + b*df.Speed + a*df.Short_Pass + a*df.Long_Pass + b*df.Jumping + b*df.GK_Positioning + b*df.GK_Diving + b*df.GK_Handling + d*df.GK_Reflexes +  d*df.GK_Kicking + c*df.Vision)/(2*a+7*b+1*c+2*d)

plt.Figure(figsize=(15,6))
sd1=df.sort_values("gk_Shot_Stopper",ascending=False)[:5]
x1=np.array(list(sd1["Name"]))
y1=np.array(list(sd1["gk_Shot_Stopper"]))
sns.barplot(x1,y1,palette="colorblind")
plt.ylabel("Shot Stopper")
plt.show()

plt.Figure(figsize=(15,6))
sd1=df.sort_values("gk_Sweeper",ascending=False)[:5]
x1=np.array(list(sd1["Name"]))
y1=np.array(list(sd1["gk_Sweeper"]))
sns.barplot(x1,y1,palette="colorblind")
plt.ylabel("Sweeper")
plt.show()

#4 best defenders 2 centre back 2 wing back
df["df_centre_backs"]=(d*df.Reactions+c*df.Interceptions+d*df.Sliding_Tackle+d*df.Standing_Tackle+b*df.Vision+b*df.Composure+b*df.Crossing+a*df.Short_Pass+b*df.Long_Pass+c*df.Acceleration+b*df.Speed
                       +d*df.Stamina+d*df.Jumping+d*df.Heading+b*df.Long_Shots+d*df.Marking+c*df.Aggression)/(6*b+3*c+7*d)
df["df_wb_Wing_Backs"]=(b*df.Ball_Control + a*df.Dribbling + a*df.Marking + d*df.Sliding_Tackle + d*df.Standing_Tackle + a*df.Attacking_Position + c*df.Vision + c*df.Crossing + b*df.Short_Pass + c*df.Long_Pass + d*df.Acceleration + d*df.Speed + c*df.Stamina
                        +a*df.Finishing)/(4*a+2*b+4*c+4*d)


plt.Figure(figsize=(15,6))
sd1=df[(df["Club_Position"]=="LCB")].sort_values("df_centre_backs",ascending=False)[:5]
x1=np.array(list(sd1["Name"]))
y1=np.array(list(sd1["df_centre_backs"]))
sns.barplot(x1,y1,palette="colorblind")
plt.ylabel("left centre back")
plt.show()

plt.Figure(figsize=(15,6))
sd1=df[(df["Club_Position"]=="RCB")].sort_values("df_centre_backs",ascending=False)[:5]
x1=np.array(list(sd1["Name"]))
y1=np.array(list(sd1["df_centre_backs"]))
sns.barplot(x1,y1,palette="colorblind")
plt.ylabel("right centre back")
plt.show()

plt.Figure(figsize=(15,6))
sd1=df[(df["Club_Position"]=="LWB") | (df["Club_Position"]=="LB")].sort_values("df_wb_Wing_Backs",ascending=False)[:5]
x1=np.array(list(sd1["Name"]))
y1=np.array(list(sd1["df_wb_Wing_Backs"]))
sns.barplot(x1,y1,palette="colorblind")
plt.ylabel("Best Left Wing Backs")
plt.show()

plt.Figure(figsize=(15,6))
sd1=df[(df["Club_Position"]=="RWB") | (df["Club_Position"]=="RB")].sort_values("df_wb_Wing_Backs",ascending=False)[:5]
x1=np.array(list(sd1["Name"]))
y1=np.array(list(sd1["df_wb_Wing_Backs"]))
sns.barplot(x1,y1,palette="colorblind")
plt.ylabel("Best Right Wing Backs")
plt.show()

#3 mid fielders#
df['mf_controller']=(b*df.Weak_foot + d*df.Ball_Control + a*df.Dribbling + a*df.Marking + a*df.Reactions + c*df.Vision + c*df.Composure + d*df.Short_Pass + d*df.Long_Pass)/(2*c + 3*d + 4*a)
df['mf_playmaker']=(d*df.Ball_Control + d*df.Dribbling + a*df.Marking + d*df.Reactions + d*df.Vision + c*df.Attacking_Position + c*df.Crossing + d*df.Short_Pass + c*df.Long_Pass + c*df.Curve
                    + b*df.Long_Shots + c*df.Freekick_Accuracy)/(1*a + 1*b + 5*c + 5*d)
df['mf_beast']=(d*df.Agility + c*df.Balance + b*df.Jumping + c*df.Strength + d*df.Stamina + a*df.Speed + c*df.Acceleration + d*df.Short_Pass + c*df.Aggression + d*df.Reactions + b*df.Marking
                + b*df.Sliding_Tackle + b*df.Standing_Tackle)/(1*a + 4*b + 4*c + 4*d)


plt.Figure(figsize=(15,6))
sd1=df[(df["Club_Position"]=="LCM") | (df["Club_Position"]=="LM")].sort_values("mf_controller",ascending=False)[:5]
x1=np.array(list(sd1["Name"]))
y1=np.array(list(sd1["mf_controller"]))
sns.barplot(x1,y1,palette="colorblind")
plt.ylabel("controller score")
plt.show()


plt.Figure(figsize=(15,6))
sd1=df[(df["Club_Position"]=="CAM") | (df["Club_Position"]=="RAM") | (df["Club_Position"]=="LAM")].sort_values("mf_playmaker",ascending=False)[:5]
x1=np.array(list(sd1["Name"]))
y1=np.array(list(sd1["mf_playmaker"]))
sns.barplot(x1,y1,palette="colorblind")
plt.ylabel("Play Maker Score")
plt.show()


plt.Figure(figsize=(15,6))
sd1=df[(df["Club_Position"]=="RCM") | (df["Club_Position"]=="RM")].sort_values("mf_beast",ascending=False)[:5]
x1=np.array(list(sd1["Name"]))
y1=np.array(list(sd1["mf_beast"]))
sns.barplot(x1,y1,palette="colorblind")
plt.ylabel("beast score")
plt.show()

#best 3 Attackers#
df["att_left_wing"]=(c*df.Weak_foot + c*df.Ball_Control + c*df.Dribbling + c*df.Speed + d*df.Acceleration + b*df.Vision + c*df.Crossing + b*df.Short_Pass + b*df.Long_Pass + b*df.Freekick_Accuracy
                     + d*df.Finishing)/(a+6*b+6*c+2*d)
df["att_right_wing"]=(c*df.Weak_foot + c*df.Ball_Control + c*df.Dribbling + c*df.Speed + d*df.Acceleration + b*df.Vision + c*df.Crossing + b*df.Short_Pass + b*df.Long_Pass + b*df.Freekick_Accuracy
                     + d*df.Finishing)/(a+6*b+6*c+2*d)
df["att_striker"]= (b*df.Weak_foot + b*df.Ball_Control + a*df.Vision + b*df.Agility + b*df.Aggression +a*df.Curve + a*df.Long_Shots + d*df.Balance + d*df.Finishing + d*df.Heading + c*df.Jumping
                    + c*df.Dribbling)/(3*a + 4*b + 2*c + 3*d)


plt.Figure(figsize=(15,6))
sd1=df[(df["Club_Position"]=="LW") | (df["Club_Position"]=="LM") | (df["Club_Position"]=="LS")].sort_values("att_left_wing",ascending=False)[:5]
x1=np.array(list(sd1["Name"]))
y1=np.array(list(sd1["att_left_wing"]))
sns.barplot(x1,y1,palette="colorblind")
plt.ylabel("left wing score")
plt.show()


plt.Figure(figsize=(15,6))
sd1=df[(df["Club_Position"]=="RW") | (df["Club_Position"]=="RM") | (df["Club_Position"]=="RS")].sort_values("att_right_wing",ascending=False)[:5]
x1=np.array(list(sd1["Name"]))
y1=np.array(list(sd1["att_right_wing"]))
sns.barplot(x1,y1,palette="colorblind")
plt.ylabel("right wing score")
plt.show()


plt.Figure(figsize=(15,6))
sd1=df[(df["Club_Position"]=="ST") | (df["Club_Position"]=="LS") | (df["Club_Position"]=="RS")].sort_values("att_striker",ascending=False)[:5]
x1=np.array(list(sd1["Name"]))
y1=np.array(list(sd1["att_striker"]))
sns.barplot(x1,y1,palette="colorblind")
plt.ylabel("striker score")
plt.show()

print("Here Is The List of FIFA best XI Players")