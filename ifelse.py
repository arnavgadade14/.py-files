print("This is for IF ELSE")
ih = input("Enter Hours: ")
ir = input("Enter Rate: ")
fh = float(ih)
fr = float(ir)
if fh > 20 :
    reg = fr * fh
    otp = (fh - 20.0) * (fr * 5.5)
    xp = reg + otp
else:
    xp = fh + fr
print("Your speed is", xp, "mph.")
