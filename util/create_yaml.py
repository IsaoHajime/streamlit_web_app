import csv
import yaml
import streamlit_authenticator as stauth    # releas 0.2.3 :2023.09.08

users_csv_path = "user_info.csv"
config_yaml_path = "config.yaml"

## ユーザー設定の一覧が記述されたデータを読み込み
with open(users_csv_path, "r") as f:
    csvreader = csv.DictReader(f)
    users = list(csvreader)

## yaml 設定一覧が記述されたデータを読み込み
with open(config_yaml_path,"r") as f:
    yaml_data = yaml.safe_load(f)

## パスワードのハッシュ化
print('パスワードのハッシュ化開始')

users_dict = {}
for user in users:
    user["password"] = stauth.Hasher([user["password"]]).generate()[0]
    # user["password"] = Hasher.hash_passwords([user["password"]])  # release 0.3.1以降のmethod
    tmp_dict = {
        "name": user["name"],
        "password": user["password"],
        "email": user["email"],
    }
    users_dict[user["id"]] = tmp_dict
    print('パスワードのハッシュ化やってます…')

## yaml 書き込み
print('yaml 書き込み開始')
yaml_data["credentials"]["usernames"] = users_dict
with open(config_yaml_path, "w") as f:
    yaml.dump(yaml_data, f)
    print("完了")
