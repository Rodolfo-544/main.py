for i in range(5):
    meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "VDD": "abreviação da palavra verdade",
            "BISCOITAR": "postar algo para chamar a atenção",
            "HATER": "pessoa que está constamente criticando os outros",
            }
    word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('palavra não encontrada')
