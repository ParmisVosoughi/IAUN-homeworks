rows1 = int(input("تعداد سطرهای ماتریس اول: "))
cols1 = int(input("تعداد ستون‌های ماتریس اول: "))
rows2 = int(input("تعداد سطرهای ماتریس دوم: "))
cols2 = int(input("تعداد ستون‌های ماتریس دوم: "))

if cols1 != rows2:
    print("ضرب ماتریس امکان‌پذیر نیست!")
else:
    matrix1 = []
    matrix2 = []
    result = []

    print("ماتریس اول:")
    for i in range(rows1):
        row = []
        for j in range(cols1):
            value = int(input(f"عنصر [{i}][{j}]: "))
            row.append(value)
        matrix1.append(row)

    print("ماتریس دوم:")
    for i in range(rows2):
        row = []
        for j in range(cols2):
            value = int(input(f"عنصر [{i}][{j}]: "))
            row.append(value)
        matrix2.append(row)

    for i in range(rows1):
        row = []
        for j in range(cols2):
            sum_val = 0
            for k in range(cols1):
                sum_val += matrix1[i][k] * matrix2[k][j]
            row.append(sum_val)
        result.append(row)

    print("حاصل ضرب ماتریس‌ها:")
    for i in range(rows1):
        for j in range(cols2):
            print(result[i][j], end=" ")
        print()

#Parmis-vosoughi