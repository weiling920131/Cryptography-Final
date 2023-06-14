import pandas as pd
from pathlib import Path
import csv
import RSACrypto as RSA

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
    print(cipher)
    print(str(cipher))

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
            i[3] = cipher#str(cipher,'UTF-8')
            flag =False
    print(public_key,'++++++++++++++++++++++++++++++')
    if(flag):
        li.append([str(len(li)),str(voter_id),str(public_key),cipher])#str(cipher,'UTF-8')])
    store = pd.DataFrame(columns = columns,data = li)
    print(li)
    print(store)
    with open(path/'public_key.csv','w') as f:
        csv_writer  = csv.writer(f)
        csv_writer.writerow(columns)
        csv_writer.writerows(li)
    return

if __name__ == "__main__":
    print(type(get_ciper(10017)))
    update_public(10001,"123",b'\x90\x8051[ce\xf5kB\rSF\n\xbek\xb0\xcd\x079\xf2\xd9\x86%\xce\x98\xde\xb1\xb0}\xf4\x93\xf39\x06\xb5\x11\xa9\x7f\\"\x80w\x8a\xbciS+\x81\xa9\xd4_\xc1\xbd\xa5S)\xd5\xdb\xba\x0c$\xd7\x92s(\x9a\xad\x96\xa2\\%7\x00o^w\xe1\x05\xd5\xffQ\xe4_N\x7f\x00\xdf?\xa2\xaca\x13h\x94g3#[\xc9p\xa7}b\xbe\xa4i\x180\xf5\xf1*j\x8fE\x19\xfb\xa2\xf9\xd5W\xfe`\x13\xb8\xa2\xb1\xdd\xb8Sk\xbcj\x93D\xd2\xa2^\xbaj\xfa~\x9c\xc9\\Jd\x01FE\x9c+\xedc8\x15\xe8r\\\xbbh\x98\x12\xeb\xe4\xd0)\x18\xadl\xfaAx\x90eb1\xed\xebc\xbe\xfb\x98\x10\xfc\xc0}\xb0\xdd\xc6\xeed\x99\xb6\xea\xd0\x8be\xaf\xc7\x17\x999i}(\x19\x1f\xdc\xf0\x8d.\x8c\x1a\x16\xcf\xd5\xa1\xc6\xb2\xc9\xb1>\xa8\xb3\xa7{\x91\x95k\x85\xbf\xd1\xaa\x05\xb1\xee\xff\xe5\x0f\x1a\xa0\xd0\xbd\xca\xc2(oy{M\xd8\xf8\x15)\xab')



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
