try:
    month = int(input("Insert Month (1-12): "))

    if month < 1 or month > 12:
        print("INPUT INVALID! [Month Cannot Exceeds Above 12 And Below 1, Try Again...]")
    else:
        if month == 2:
            day = 29
        elif month in [4, 6, 9, 11]:
            day = 30
        else:
            day = 31

        print("Days Total:", day)

except ValueError:
    print("INPUT INVALID! [Input Has In Number Category, Between 1 to 12, Try Again...]")
    
    # Memasukkan Bulan Yang Salah : Menggunakan "Try" & "Except" Dengan Tambahan "If" & "Else"
    # [Line 1, 4, 6, 16]
