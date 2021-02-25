import x

T_wody = [];                'temperatura wody, [st. C]'
T_wody2 = [];

x.Qg.append(x.Qg_0)
T_wody.append(x.T_0)
T_wody2.append(x.T_0-273)
x.e.append(x.T_k)


def regulator(e1, e2):
    sygn = [["DU", "DU", "SU", "MU", "Z", "MD", "DD"],
            ["DU", "DU", "SU", "Z", "SD", "DD", "DD"],
            ["DU", "MU", "Z", "MD", "SD", "DD", "DD"]]

    ce = e2 - e1
    if e2 ... :
        if ce ...:
            return


for n in range(1, x.N+1):
    x.e.append(x.T_k - T_wody[n-1])

    u = regulator(x.e[n - 2], x.e[n - 1])
    x.Qg[n - 1] = u * 220
    T_n = x.Tp / x.Cv * x.Qg[n - 1] + T_wody[n - 1]

    T_wody.append(T_n)
    T_wody2.append(T_n - 273)
    x.Qg.append(x.Qg_0)