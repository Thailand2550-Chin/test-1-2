midterm = float(input('คะเเนนสอบกลางภาค:'))
Final = float(input('คะเเนนสอบปลายภาค:'))
if 0 <= midterm <= 60 and 0 <= Final <= 60:
    x = midterm + Final
    y = (midterm + Final)/2
    print("Total:",x)
    print("Average:",y)
else:
    print("ไม่สามารถระบุได้ข้อมูลที่กรอกมีเงื่อนไขผิด")
