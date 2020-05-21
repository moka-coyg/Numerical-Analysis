import numpy as np

def bisection():
    epsilon = 1e-3 #float(input("収束判定条件εを入力してください："))
    a = 4 #float(input("左端の数値を入力してください："))
    b = 5 #float(input("右端の数値を入力してください："))
    flg = 0
    ans = 0
    step = 1
    while(flg == 0):
        c = (a + b) / 2
        d = abs(a - b) / 2
        if d < epsilon:
            ans = c
            flg = 1
        func_out = np.exp(c - 3) - 4
        print("Step:{0}, a = {1}, b = {2}, c = {3}, d = {4}, func_out = {5}".format(step, a, b, c, d, func_out))
        if func_out < 0:
            a = c
        elif func_out > 0:
            b = c
        else:
            ans = c
            flg = 1
        step += 1

    print("根は{:.4g}です".format(ans))

def newton():
    epsilon = 1e-3 #float(input("収束判定条件εを入力してください："))
    x_n = 5 #float(input("初期値を入力してください："))
    func_out = np.exp(x_n - 3) - 4
    func_bibun = np.exp(x_n - 3)
    step = 1
    flag = 0
    while(flag == 0):
        func_out = np.exp(x_n - 3) - 4
        func_bibun = np.exp(x_n - 3)
        x_next = x_n - func_out / func_bibun
        b = abs(x_next - x_n)
        c = abs(x_next)
        print("Step:{0}, x_n = {1}, f(x_n) = {2}, f'(x_n) = {3}, x_n - f(x_n)/f'(x_n) = {4}".format(step, x_n, func_out, func_bibun, x_next))
        if b > epsilon * c:
            x_n = x_next
            step += 1
        else:
            flag = 1
    print("根は{:.4g}です".format(x_next))

print("2分法：")
bisection()
print("\n")
print("ニュートン法：")
newton()