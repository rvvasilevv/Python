def vuprosi(**vuproscheta):
    ime=input("Kak se kazvash")
    if ime != str:
        print("Greshen format")
        ime=input("Napishi si pravilno imeto")
    rd=input("Koga si roden")
    adres=input("Kyde jiveesh")
    print(f'-Name:{ime}')
    print(f'Date of birth":{rd}')
    print(f'-Adres:{adres}')
vuprosi()
