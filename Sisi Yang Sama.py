try:
    Line1 = float(input("Input Line 1: "))
    Line2 = float(input("Input Line 2: "))
    Line3 = float(input("Input Line 3: "))

    if Line1 <= 0 or Line2 <= 0 or Line3 <= 0:
        print("INVALID INPUT! [Lines Cannot Exceeds Below 0, Try Again...]")
    else:
        if Line1 == Line2 == Line3:
            print("3 Lines Equal")
        elif Line1 == Line2 or Line1 == Line3 or Line2 == Line3:
            print("2 Lines Equal")
        else:
            print("No Lines Equal")

except ValueError:
    print("INPUT INVALID! [Input Except Nummbers Only...]")

    # Memasukkan Sisi Garis Yang Salah : Menggunakan "Try" & "Except" Dengan Tambahan "If" & "Else"
    # [Line 1, 6, 8, 16]
