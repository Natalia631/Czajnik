
'wprowadza uzytkowanik:'
import math

T_ = 22;                      'temperatura poczatkowa wody, [st. C]'
T_k_ = 100;                      'temperatura koncowa wody, [st. C]'

cp = 4189.9;                   'cieplo wlasciwe wody, [J/(kg*K)]'
ro = 997 ;                 'gestosc wody, [kg/m3]'
R = 0.15   ;                 'srednica podstawy czajnika, [m]'
h = 0.15  ;                  'wysokosc slupa wody w czajniku, [m]'
V = 3.14 * (R/2)**2 * h ;     'objetosc wody w czajniku, [m3]'
Cv = cp * ro * V ;           'pojemnosc cieplna wody, [J/K] '
Tp = 0.1  ;                 'okres probkowania, [s]'
t_sim = 10 * 3600   ;        'czas symulacji, [s]'
N = round(t_sim / Tp) ;      'liczba probek'
T_0 = T_ + 273 ;             'temperatura poczatkowa wody, [K]'
P = 2200     ;               'moc grzalki, [W]'
T_k = T_k_ + 273    ;          'zadana temperatura, jaka woda ma osiagnac, [K]'
t = Cv / P * (T_k - T_0) ;   'czas potrzebny na ogrzanie wody do zadanej temperatury'
#Qg_0= 180*P/N  ;               'cieplo dostarczane przez grzalke w czasie Tp - grzałka zagotuje wodę w czajniku do 100 stC w 3 minuty'
Qg_0=P*Tp
e=[];
Qg = [];
reg=1;              #wybór regulatora : 1-PD, 2-rozmyty PD

#Nastawy regulatora PID
Kp=0.01
Td=100

