import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.preprocessing import StandardScaler
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
import random
import pickle
from sklearn.impute import KNNImputer
from PIL import Image
import requests
from io import BytesIO
from termcolor import colored, cprint

def get_models():
    models = dict()
    models['lm'] = LinearRegression()
    models['rf'] = RandomForestRegressor(random_state=35)
    models['gra'] = GradientBoostingRegressor(random_state=35)
    models['ada'] = AdaBoostRegressor(random_state=35)
    return models

def decade_star(df): 
    decade_list = list(song_decade['release_decade'].unique())
    artist_list = []
    dec = []
    song_num = []
    for decade in decade_list: 
        max_song = df[(df['release_decade']==decade)]['song'].max()
        artist = list(df['artist'][(df['release_decade']==decade) & (df['song']==max_song)])[0]
        dec.append(decade)
        artist_list.append(artist)
        song_num.append(max_song)
    decade_dict = {'decade':dec,'artist of the decade':artist_list,'count':song_num}
    decade_df = pd.DataFrame.from_dict(decade_dict)
    return decade_df


def search_song(title,artist):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret_id))
    try: 
        string = "tracks: " + title + "artist: " + artist
        song=sp.search(q=string,limit=1)
        id = song['tracks']['items'][0]['id']
    except:
        id = np.nan
    
    return id

def get_audio_features(list_of_songs_ids):
    features = sp.audio_features(list_of_songs_ids)
    return features

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def load(filename = "filename.pickle"): 
    try: 
        with open(filename, "rb") as file: 
            return pickle.load(file) 
    except FileNotFoundError: 
        print("File not found!") 

def find_your_drag_mother():
    while True: 
        location = input("Please choose a country you would like to visit:\n A.USA            B.Chile\n C.Thailand       D.UK\n E.Canada         F.Holland\n G.New Zealand    H.Spain\n I.France         J.Italy\n")
        if location not in ['A','B','C','D','E','F','G','H','I','J']: 
            print("")
            print("Please type the letter A,B,C or etc. to make the choice.")
            print("")
            continue
        else:
            break

    if location == 'A':
        fran = 'F10'
    elif location == 'B':
        fran = 'F18'
    elif location == 'C':
        fran = 'F13'
    elif location == 'D':
        fran = 'F14'
    elif location == 'E':
        fran = 'F15'
    elif location == 'F':
        fran = 'F16'
    elif location == 'G':
        fran = 'F17'
    elif location == 'H':
        fran = 'F18'
    elif location == 'I':
        fran = 'F21'
    else: 
        fran = 'F19'
    
    while True: 
        drag_type = input("Please select the word the resonates with you the most:\n A.Pageant B. Club C. Look D. Spooky E.Comedy ")
        if drag_type not in ['A','B','C','D','E']: 
            print("")
            print("Please type the letter A,B,C or etc. to make the choice.")
            print("")
            continue
        else:
            break
    if drag_type == 'A':
        drag = 'Pageant'
    elif drag_type == 'B':
        drag = 'Club'
    elif drag_type == 'C':
        drag = 'Look'
    elif drag_type == 'D':
        drag = 'Spooky'
    else: 
        drag = 'Comedy'
    
    while True: 
        con_type = input("True or False: Instead of becoming the queen of the drag herstory, I'd rather become the queen of the people.")
        if con_type not in ['True','False']: 
            print("")
            print("Please type True or False to continue.")
            print("")
            continue
        else:
            break
    queens = pd.read_csv('../Data/raw/ref_queen_img.csv')
    data = pd.read_csv('../Data/cleaned/all_season_results.csv')
    if con_type == "True":
        lst = data[(data['type']==drag) &  (data['miss_con']==1)].sample(1)
    else:
        lst = data[(data['original_season_id'].str.contains(fran)) & (data['type']==drag) & (data['miss_con']==0) & (data['final_place']<4)].sample(1)
    name = list(lst['name'])[0]
    response = requests.get(list(queens['link_image'][queens['name']==name])[0])
    img = Image.open(BytesIO(response.content))
    
    cprint('**************************************','green',attrs=['bold'])
    print(colored("Your drag mother is: "+name+"! She is a "+drag+" queen.",'black',attrs=['bold']))
    cprint('**************************************','green',attrs=['bold'])
    return img

def lip_sync_recommender():
    while True: 
        try: 
            dance = str(input("I consider myself a dancing queen.\n A. Strongly agree B.Agree C.Neutral D.Disagree E.Strongly Disagree\n"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if dance not in ['A','B','C','D','E',]:
            print("")
            print("Please type the letter A,B,C or etc. to make the choice.")
            print("")
            continue
        else:
            break
    if dance == 'A':
        dance_score = random.uniform(0.8,1)
    elif dance == 'B':
        dance_score = random.uniform(0.6,0.8)
    elif dance == 'C':
        dance_score = random.uniform(0.4,0.6)
    elif dance == 'D':
        dance_score = random.uniform(0.2,0.4)
    else: 
        dance_score = random.uniform(0,0.2)
        
    while True: 
        try: 
            energy = str(input("I consider myself an energetic person.\n A. Strongly agree B.Agree C.Neutral D.Disagree E.Strongly Disagree\n"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if energy not in ['A','B','C','D','E',]:
            print("")
            print("Please type the letter A,B,C or etc. to make the choice.")
            print("")
            continue
        else:
            break
    if energy == 'A':
        energy_score = random.uniform(0.8,1)
    elif energy == 'B':
        energy_score = random.uniform(0.6,0.8)
    elif energy == 'C':
        energy_score = random.uniform(0.4,0.6)
    elif energy == 'D':
        energy_score = random.uniform(0.2,0.4)
    else: 
        energy_score = random.uniform(0,0.2)
    
    while True: 
        try: 
            loud = str(input("I like loud music.\n A. Strongly agree B.Agree C.Neutral D.Disagree E.Strongly Disagree\n"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if loud not in ['A','B','C','D','E',]:
            print("")
            print("Please type the letter A,B,C or etc. to make the choice.")
            print("")
            continue
        else:
            break
    if loud == 'A':
        loud_score = random.uniform(-4,0)
    elif loud == 'B':
        loud_score = random.uniform(-8,-4)
    elif loud == 'C':
        loud_score = random.uniform(-12,-8)
    elif loud == 'D':
        loud_score = random.uniform(-16,-12)
    else: 
        loud_score = random.uniform(-20,-16)
    
    while True: 
        try: 
            speech = str(input("I like songs that include dialogue.\n A. Strongly agree B.Agree C.Neutral D.Disagree E.Strongly Disagree\n"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if speech not in ['A','B','C','D','E',]:
            print("")
            print("Please type the letter A,B,C or etc. to make the choice.")
            print("")
            continue
        else:
            break
    if speech == 'A':
        speech_score = random.uniform(0.4,0.6)
    elif speech == 'B':
        speech_score = random.uniform(0.3,0.4)
    elif speech == 'C':
        speech_score = random.uniform(0.2,0.3)
    elif speech == 'D':
        speech_score = random.uniform(0.1,0.2)
    else: 
        speech_score = random.uniform(0,0.1)
        
    
    while True: 
        try: 
            ac = str(input("I usually prefer the acoustic versions.\n A. Strongly agree B.Agree C.Neutral D.Disagree E.Strongly Disagree\n"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if ac not in ['A','B','C','D','E',]:
            print("")
            print("Please type the letter A,B,C or etc. to make the choice.")
            print("")
            continue
        else:
            break
    if ac == 'A':
        ac_score = random.uniform(0.8,1)
    elif ac == 'B':
        ac_score = random.uniform(0.6,0.8)
    elif ac == 'C':
        ac_score = random.uniform(0.4,0.6)
    elif ac == 'D':
        ac_score = random.uniform(0.2,0.4)
    else: 
        ac_score = random.uniform(0,0.2)
    
    ins_score = 0
    
    while True: 
        try: 
            live = str(input("I usually prefer the live versions.\n A. Strongly agree B.Agree C.Neutral D.Disagree E.Strongly Disagree\n"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if live not in ['A','B','C','D','E',]:
            print("")
            print("Please type the letter A,B,C or etc. to make the choice.")
            print("")
            continue
        else:
            break
    if live == 'A':
        live_score = random.uniform(0.8,1)
    elif live == 'B':
        live_score = random.uniform(0.6,0.8)
    elif live == 'C':
        live_score = random.uniform(0.4,0.6)
    elif live == 'D':
        live_score = random.uniform(0.2,0.4)
    else: 
        live_score = random.uniform(0,0.2)
    
    while True: 
        try: 
            val = str(input("I usually prefer cheerful & euphoric songs than sad & angry songs.\n A. Strongly agree B.Agree C.Neutral D.Disagree E.Strongly Disagree\n"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if val not in ['A','B','C','D','E',]:
            print("")
            print("Please type the letter A,B,C or etc. to make the choice.")
            print("")
            continue
        else:
            break
    if val == 'A':
        val_score = random.uniform(0.8,1)
    elif val == 'B':
        val_score = random.uniform(0.6,0.8)
    elif live == 'C':
        val_score = random.uniform(0.4,0.6)
    elif val == 'D':
        val_score = random.uniform(0.2,0.4)
    else: 
        val_score = random.uniform(0,0.2)
    
    while True: 
        try: 
            tempo = str(input("I usually prefer songs with faster tempos.\n A. Strongly agree B.Agree C.Neutral D.Disagree E.Strongly Disagree\n"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if tempo not in ['A','B','C','D','E',]:
            print("")
            print("Please type the letter A,B,C or etc. to make the choice.")
            print("")
            continue
        else:
            break
    if tempo == 'A':
        tempo_score = random.uniform(180,203)
    elif tempo == 'B':
        tempo_score = random.uniform(150,180)
    elif live == 'C':
        tempo_score = random.uniform(120,150)
    elif tempo == 'D':
        tempo_score = random.uniform(90,120)
    else: 
        tempo_score = random.uniform(60,90)
    
    songs = pd.read_csv('../Data/cleaned/song_cluster.csv')
    song_num = songs.select_dtypes(np.number)
    song_num = song_num.drop(columns=['release_year','key','mode','duration_ms','time_signature','release_decade'])
    score_list = [dance_score,energy_score,loud_score,speech_score,ac_score,ins_score,live_score,val_score,tempo_score]
    arr = np.array(score_list)
    lst = pd.DataFrame(arr).T
    lst.columns = song_num.columns[0:-1]
    
    X = pd.concat([song_num,lst],axis=0)
    scaler = StandardScaler()
    scaler.fit(X)
    X_scaled = scaler.transform(X)
    X_scaled_df = pd.DataFrame(X_scaled, columns = X.columns)
    
    imputer = KNNImputer(n_neighbors=5)
    df_imputed = imputer.fit_transform(X_scaled)
    X_imputed = pd.DataFrame(df_imputed,columns=X_scaled_df.columns)
    cluster = int(X_imputed.iloc[-1,1])
    def make_clickable(val):
        """
        Function to convert a URL string to a clickable HTML link.
        """
        return f'<a href="{val}" target="_blank">{val}</a>'
    song_choice = songs[['song','artist','release_year','id']][(songs['cluster']==cluster) & (songs['hot']=='No')].sample(1)
    song_choice['id'] = song_choice['id'].apply(lambda x: "https://open.spotify.com/track/" + x)
    song_choice = song_choice.style.format({'id':make_clickable})
    
    cprint('**************************************','green',attrs=['bold'])
    print(colored("Now its' time for you to lip sync FOR YOUR LIFE! Good luck & Don't f**k it up!",'black',attrs=['bold']))
    cprint('**************************************','green',attrs=['bold'])
    return song_choice

def drag_name():
    data = pd.read_csv('../Data/cleaned/all_season_results.csv')
    drag_name = pd.read_csv('../Data/cleaned/drag_name.csv')
    while True:
        try:
            mother = input("Please type the name of your drag mother: \n")
        except ValueError:
            print("Sorry I don't understand.")
            continue 
        if mother not in list (data['name']):
            print("Please check the name and enter again.")
        else:
            break
    
    first_input = input("Please enter your first name: \n")
    first_name = list(drag_name['first_name'][drag_name['first_letter']==list(first_input)[0]])[0]
    
    while True:
        try:
            choice = input("Would you like to take your drag mother's name as part of your new name? \n A.Yes     B.No\n")
        except ValueError:
            print("Sorry I don't understand.")
            continue 
        if choice not in ['A','B']:
            print("Please enter only A or B to continue.")
        else:
            break
    if choice == "A":
        last_name = mother.split(" ")[-1]
        name = first_name+" "+last_name
    else: 
        last_input = input("Please enter your last name: \n")
        last_name = list(drag_name['surname'][drag_name['first_letter']==list(last_input)[0]])[0]
        name = first_name+" "+last_name

    return name