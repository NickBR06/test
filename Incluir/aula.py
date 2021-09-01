from datetime import datetime 
import os
import shutil
import logging

# ------ Config. Log -------

logging.basicConfig(filename='LogTest.log', level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    filemode='w'
                    )

# ------ Código -------

caminho_original = input("Qual o caminho da pasta?: ")

banc = input("Qual o código do banco? ")
dat_atual = datetime.today().strftime('%m/%d')
try:
    logging.debug("--------Acesso primario----------")
    if banc == str("341"):
        logging.debug("Código correto foi inserido")
        op_usu = input("Qual operação deseja fazer?")

        if op_usu.upper() == str("PE"):
            logging.debug("Selecionado PE")
            rem_ou_ret = input("Enviar remesa ou receber retorno? ")
            print(rem_ou_ret)

            if rem_ou_ret.upper() == str("REM"):
                logging.debug("Selecionado REM")
                rem_ou_ret = str("/{}".format(rem_ou_ret))
                print("Tudo certo! Sua remesa esta a caminho!")

            elif rem_ou_ret.upper() == str("RET"):
                logging.debug("Selecionado RET")
                rem_ou_ret = str("/{}".format(rem_ou_ret))
                print("Tudo certo! Seu retorno esta a caminho!")

            else:
                logging.info("Opção selecionada invalida")
                print("opção invalida")

        if op_usu.upper() == str("CE"):
            logging.debug("Selecionado CE")
            rem_ou_ret = input("Enviar remesa ou receber retoro? ")
            print(rem_ou_ret)

            if rem_ou_ret.upper() == str("REM"):
                logging.debug("Selecionado REM")
                rem_ou_ret = str("/{}".format(rem_ou_ret))
                print("Tudo certo! Sua remesa esta a caminho!")

            elif rem_ou_ret.upper() == str("RET"):
                logging.debug("Selecionado RET")
                rem_ou_ret = str("/{}".format(rem_ou_ret))
                print("Tudo certo! Seu retorno esta a caminho!")

            else:  # Corrigir
                logging.info("Opção selecionada invalida")
                print("opção invalida")

        if op_usu.upper() == str("EXT"):
            logging.debug("Selecionado EXT")
            rem_ou_ret.upper = str("RET")
            rem_ou_ret = str("/{}".format(rem_ou_ret))
            print("Tudo certo! Seu retorno esta a caminho!")

        if op_usu.lower() == str("inbox"):
            logging.debug("Selecionado inbox")
            rem_ou_ret = "2"

        else:  # Corrigir
            logging.info("Operação inserida invalida")
            print("Operação invalida")
    else:
        logging.info("Código incorreto, pois não trabalhamos com esse banco")
        print("Este banco ainda não é aceito pelo sistema")





finally:
    if rem_ou_ret != ("2"):
        caminho_novo = str("C:/VAN_STAGE/{}/{}/{}".format(banc, op_usu.upper(), rem_ou_ret.upper(), dat_atual))
        print(caminho_novo)

    if rem_ou_ret == str("2"):
        caminho_novo = str("C:/VAN_STAGE/{}/{}/{}".format(banc, op_usu.upper(), dat_atual))
        print(caminho_novo)
try:
    logging.debug("Nova pasta criada com sucesso!")
    os.makedirs(caminho_novo)

except FileExistsError as e:
    logging.info("Pasta já existente")  # Corrigir
    print("A pasta {} já existe".format(caminho_novo))

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        if banc in file:
            logging.debug("Movido com sucesso")
            shutil.move(old_file_path, new_file_path)
            print("file {} movido com sucesso".format(file))
