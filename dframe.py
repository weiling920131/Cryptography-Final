import pandas as pd
from pathlib import Path

path = Path("database")

def get_ciper(voter_id):
    df = pd.read_csv(path/'public_key.csv',dtype=str)
    #print(df)
    li = df.values.tolist()
    for i in li:
        if i[1]==str(voter_id):
            return str(i[3])
    return None
def update_public(voter_id, public_key, cipher):
    # cipher = cipher.decode()


    df = pd.read_csv(path/'public_key.csv',dtype=str)
    columns =df.columns.tolist() 
    for i in range(len(columns)):
        if columns[i][:9] =="Unnamed: ":
            columns[i]=""
    li = df.values.tolist()
    flag = True
    for i in li:
        if i[1] == str(voter_id):
            i[2] = str(public_key)
            i[3] = cipher
            flag =False
    if(flag):
        li.append([str(len(li)),str(voter_id),str(public_key),str(cipher)])
    store = pd.DataFrame(columns = columns,data = li)
    store.to_csv(path/'public_key.csv',encoding='utf-8',index = False)
    return

def count_reset():
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Name','Gender','Zone','City','Passw','hasVoted']]
    for index, row in df.iterrows():
        df['hasVoted'].iloc[index]=0
    df.to_csv(path/'voterList.csv')

    df=pd.read_csv(path/'cand_list.csv')
    df=df[['Sign','Name','Vote Count']]
    for index, row in df.iterrows():
        df['Vote Count'].iloc[index]=0
    df.to_csv (path/'cand_list.csv')


def reset_voter_list():
    df = pd.DataFrame(columns=['voter_id','Name','Gender','Zone','City','Passw','hasVoted'])
    df=df[['voter_id','Name','Gender','Zone','City','Passw','hasVoted']]
    df.to_csv(path/'voterList.csv')

def reset_cand_list():
    df = pd.DataFrame(columns=['Sign','Name','Vote Count'])
    df=df[['Sign','Name','Vote Count']]
    df.to_csv(path/'cand_list.csv')


def verify(vid,passw):
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Passw','hasVoted']]
    for index, row in df.iterrows():
        if df['voter_id'].iloc[index]==vid and df['Passw'].iloc[index]==passw:
            return True
    return False


def isEligible(vid):
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Name','Gender','Zone','City','Passw','hasVoted']]
    for index, row in df.iterrows():
        if df['voter_id'].iloc[index]==vid and df['hasVoted'].iloc[index]==0:
            return True
    return False


def vote_update(st,vid):
    if isEligible(vid):
        df=pd.read_csv (path/'cand_list.csv')
        df=df[['Sign','Name','Vote Count']]
        for index, row in df.iterrows():
            if df['Sign'].iloc[index]==st:
                df['Vote Count'].iloc[index]+=1

        df.to_csv (path/'cand_list.csv')

        df=pd.read_csv(path/'voterList.csv')
        df=df[['voter_id','Name','Gender','Zone','City','Passw','hasVoted']]
        for index, row in df.iterrows():
            if df['voter_id'].iloc[index]==vid:
                df['hasVoted'].iloc[index]=1

        df.to_csv(path/'voterList.csv')

        return True
    return False


def show_result():
    df=pd.read_csv (path/'cand_list.csv')
    df=df[['Sign','Name','Vote Count']]
    v_cnt = {}
    for index, row in df.iterrows():
        v_cnt[df['Sign'].iloc[index]] = df['Vote Count'].iloc[index]
    # print(v_cnt)
    return v_cnt


def taking_data_voter(name,gender,zone,city,passw):
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Name','Gender','Zone','City','Passw','hasVoted']]
    row,col=df.shape
    if row==0:
        vid = 10001
        df = pd.DataFrame({"voter_id":[vid],
                    "Name":[name],
                    "Gender":[gender],
                    "Zone":[zone],
                    "City":[city],
                    "Passw":[passw],
                    "hasVoted":[0]},)
    else:
        vid=df['voter_id'].iloc[-1]+1
        df1 = pd.DataFrame({"voter_id":[vid],
                    "Name":[name],
                    "Gender":[gender],
                    "Zone":[zone],
                    "City":[city],
                    "Passw":[passw],
                    "hasVoted":[0]},)

        df = pd.concat([df, df1],ignore_index=True)

    df.to_csv(path/'voterList.csv')

    return vid
