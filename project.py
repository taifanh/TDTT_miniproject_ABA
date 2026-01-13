import json
import os

# -------------------------------Function------------------------------------------------
def color(text, c):
    return f"\033[{c}m{text}\033[0m"

def cal_TB(diem):
    sum = 0
    hs = [0, 1, 3, 6]
    for i in range(1, 4):
        if diem[i] == "":
            return ""
        sum += diem[i] * hs[i]
    return sum / 10 if sum % 10 != 0 else sum

def tt1(sv):
    while True:
        try:
            ma_sv = input(color("Nhập mã sinh viên (Nếu muốn hủy hãy nhấn Enter): ", 33))
            if ma_sv == "":
                return None
            if ma_sv in sv:
                print(color("Mã sinh viên đã tồn tại!", 31))
                continue
            ma_sv = int(ma_sv)
            break
        except:
            print(color("Nhập số nguyên!", 31))
    ma_sv = str(ma_sv)
    diem = []
    for cot in range(4):
        if cot == 0:
            ten_sv = input(color("Nhập tên sinh viên: ", 33))
            diem.append(ten_sv)
        else:
            muc = ["", "chuyên cần", "giữa kỳ", "cuối kỳ"]
            while True:
                diem_tp = input(color(f"Nhập điểm {muc[cot]} (Nhấn Enter để bỏ qua mục điểm): ", 33))
                if diem_tp == "":
                    break
                try:
                    diem_tp = int(diem_tp)
                    break
                except ValueError:
                    print(color("Nhập điểm số nguyên!", 31))
                
            diem.append(diem_tp)
    diem.append("")
    diem[4] = cal_TB(diem)
    sv[ma_sv] = diem

def tt2(sv):
    while True:
        try:
            ma_sv = input(color("Nhập mã sinh viên (Nếu muốn hủy hãy nhấn Enter): ", 33))
            if ma_sv == "":
                return None
            if ma_sv not in sv:
                print(color("Mã sinh viên không tồn tại!", 31))
                continue
            ma_sv = int(ma_sv)
            break
        except:
            print("Nhập số nguyên!")
    ma_sv = str(ma_sv)
    del sv[ma_sv]

def tt3(sv):
    while True:
        try:
            ma_sv = input(color("Nhập mã sinh viên (Nếu muốn hủy hãy nhấn Enter): ", 33))
            if ma_sv == "":
                return None
            if ma_sv not in sv:
                print(color("Mã sinh viên không tồn tại!", 31))
                continue
            ma_sv = int(ma_sv)
            break
        except:
            print(color("Nhập số nguyên!", 31))
    ma_sv = str(ma_sv)
    diem = []
    for cot in range(4):
        if cot == 0:
            ten_sv = sv[ma_sv][0]
            diem.append(ten_sv)
        else:
            muc = ["", "chuyên cần", "giữa kỳ", "cuối kỳ"]
            while True:
                diem_tp = input(color(f"Nhập điểm {muc[cot]} (Nhấn Enter để bỏ qua mục điểm): ", 33))
                if diem_tp == "":
                    break
                try:
                    diem_tp = int(diem_tp)
                    break
                except ValueError:
                    print(color("Nhập điểm số nguyên!", 31))
                
            diem.append(diem_tp)
    diem.append("")
    diem[4] = cal_TB(diem)
    sv[ma_sv] = diem

def in_hang(hang):
    print("|", end = "")
    sz = [8, 20, 3, 3, 3, 3]
    for i in range(len(hang)):
        x = str(hang[i])
        if len(x) > sz[i]:
            for j in range(sz[i]):
                print(x[j], end = "")
        else:
            print(x, end = "")
            print(" " * (sz[i] - len(x)), end = "")
        print("|", end = "")
    print('\n')

def tt4(sv):
    sv = dict(sorted(sv.items()))
    cot = ["Mã SV", "Tên SV", "CC", "GK", "CK", "TB"]
    print("-" * 47)
    in_hang(cot)
    for x, y in sv.items():
        z = []
        z.append(x)
        z += y
        in_hang(z)
    print("-" * 47)
# -----------------------------Main------------------------------------

filename = "data.txt"

if os.path.getsize(filename) == 0:
    sv = {}
else:
    with open(filename, "r", encoding="utf-8") as f:
        sv = json.load(f)
print(color("""
Nhập các số sau với thao tác mong muốn:
1: Nhập điểm sinh viên mới
2: Xóa sinh viên
3: Thay đổi điểm sinh viên
4: In bảng điểm
""", 34))
while True:
    while True:
        try:
            tt = input(color("Thao tác chọn (Nhấn Enter nếu muốn hủy): ", 33))
            if tt == "":
                break
            tt = int(tt)
            if tt > 5:
                print(color("Chọn số từ 1 đến 5!", 31))
                continue
            break
        except ValueError:
            print(color("Nhập số từ 1 đến 4!", 31))
    if tt == "":
        break
    if tt == 1:
        tt1(sv)
    elif tt == 2:
        tt2(sv)
    elif tt == 3:
        tt3(sv)
    else:
        tt4(sv)
    print(color("Đã xong\n", 32))

with open("data.txt", "w", encoding="utf-8") as f:
    json.dump(sv, f)
