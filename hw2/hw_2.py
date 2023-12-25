import json 
from datetime import date, datetime

now_data = date.today()



def process_data(input_path, output_path: str):
    with open(input_path, 'r', ) as file:
        data = json.load(file)
        now_data = date.today()
        count_user = len(data)
        age_result = {'0-18': 0, '18-25': 0, '25-45': 0, '45-60': 0, '60+': 0}
        time_score = {'<2':0, '7':0, '28-31':0, '182':0, '>182':0}

    
    for client in data.values():
        age = client.get('age')
        last_login = client.get('last_login')
        if age is None or last_login is None:
            raise ValueError('no values ​​provided')

        last_login_origin = datetime.fromisoformat(last_login).date()
        delta = (now_data - last_login_origin).days

        if age <=18:
            age_result['0-18']+=1
        elif  18 < age <= 25:
            age_result['18-25'] +=1
        elif 25 <= age <=45:
            age_result['45-60'] +=1
        elif 45 <= age <= 60:
            age_result['45-60'] +=1
        elif age >=60:
            age_result['60+'] +=1

        if delta < 2:
            time_score['<2'] +=1
        elif delta < 7:
            time_score['7'] +=1
        elif delta < 28:
            time_score['28-31'] +=1
        elif delta < 182:
            time_score['182'] +=1
        elif delta >= 182:
            time_score['>182'] +=1
    age_statistics = {category:( count / count_user * 100) for category, count in age_result.items()}
    time_statictics = { days: (count/ count_user * 100 ) for days, count in time_score.items()}

    print(age_statistics)
    print(time_statictics)
    
    out_data = {'age_statistics': age_statistics, 'time_statictics': time_statictics}
    with open(output_path, 'w' ) as ouput1:
        json.dump(out_data, ouput1)


process_data('/home/a/Рабочий стол/sirius1/hw2/data_hw2.json', '/home/a/Рабочий стол/sirius1/hw2/output1.json')