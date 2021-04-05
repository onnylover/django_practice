from guestbook01.models import findall,insert,deletebynoandpw

def test_findall():
    results = findall()
    for result in results:
        print(f"""{result["no"]}:{result["name"]}:{result["reg_date"]}:{result["message"]}""")

def test_instert():
    name = "DingDong"
    password = "1234"
    message = "hola hola!"
    result = insert(name,password,message)
    print(f"insert result : {result}")

def test_delete():
    no = 3
    password = "1234"
    result = deletebynoandpw(no,password)
    print(f"delete result : {result}")

def main():
    #test_instert()
    test_delete()
    test_findall()

if __name__ == "__main__":
    main()

