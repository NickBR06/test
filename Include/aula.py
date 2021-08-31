from datetime import datetime
import os
import shutil

caminho_original = input("Qual o caminho da pasta?: ")

banc = input("Qual o código do banco? ")
dat_atual = datetime.today().strftime('%m/%d')
try:
    if banc == str("341"):
        op_usu = input("Qual operação deseja fazer? ")

        if op_usu.upper() == str("PE"):
            rem_ou_ret = input("Enviar remesa ou receber retoro? ")
            print(rem_ou_ret)

            if rem_ou_ret.upper() == str("REM"):
                rem_ou_ret = str("/{}".format(rem_ou_ret))
                print("Tudo certo! Sua remesa esta a caminho!")

            elif rem_ou_ret.upper() == str("RET"):
                rem_ou_ret = str("/{}".format(rem_ou_ret))
                print("Tudo certo! Seu retorno esta a caminho!")

        if op_usu.upper() == str("CE"):
            rem_ou_ret =  input("Enviar remesa ou receber retoro? ")
            print(rem_ou_ret)

            if rem_ou_ret.upper() == str("REM"):
                rem_ou_ret = str("/{}".format(rem_ou_ret))
                print("Tudo certo! Sua remesa esta a caminho!")

            elif rem_ou_ret.upper() == str("RET"):
                rem_ou_ret = str("/{}".format(rem_ou_ret))
                print("Tudo certo! Seu retorno esta a caminho!")

        if op_usu.upper() == str("EXT"):
                rem_ou_ret.upper = str("RET")
                rem_ou_ret = str("/{}".format(rem_ou_ret))
                print("Tudo certo! Seu retorno esta a caminho!")

        if op_usu.lower() == str("inbox"):
            rem_ou_ret = ("2")
    else :
        print("Este banco ainda não é aceito pelo sistema")

finally:
    if rem_ou_ret != ("2") :
        caminho_novo = str("C:/VAN_STAGE/{}/{}/{}".format(banc, op_usu.upper(),rem_ou_ret.upper(), dat_atual))
        print(caminho_novo)

    if rem_ou_ret == str("2"):
        caminho_novo = str("C:/VAN_STAGE/{}/{}/{}".format(banc, op_usu.upper(), dat_atual))
        print(caminho_novo)
try: 
    os.makedirs(caminho_novo)

except FileExistsError as e:
    print("A pasta {} já existe".format(caminho_novo))

for root, dirs, files in os.walk(caminho_original):
    for file in files: 
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if banc in file:

            shutil.move(old_file_path, new_file_path)
            print("file {} movido com sucesso".format(file))
