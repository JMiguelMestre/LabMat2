"""
# -*- coding: utf-8 -*-
"""
Laboratórios de Matemática 2
Parte 1 - Versão 3

Data: yyyy/mm/dd

Autores
1. 1160930 José Miguel Mestre Fernandes da Silva
2. 1160675 Gil Espirito Santo Nunes
3. 1160872 Maria João Guimarães
""
from __future__ import division
from __future__ import print_function
from LabMat1_Lib import *
import pylab as pl

clc()

#%% Bloco de identificação do trabalho
print('\n\nTrabalho curricular\nPARTE 1\nVERSÃO 3\n\n')
print('AUTORES:')
print('\t1160930\tJosé Miguel Mestre Fernandes da Silva')
print('\t1160675\tGil Espirito Santo Nunes')
print('\t1160872\tMaria João Guimarães')
#%% Leitura do ficheiro de dados
# Estrutura de dados: dados=array(Nlinhas,3colunas)
#  t/s |  Vin/V  | Vc/V
#
Ficheiro="Dados_TC_P1_V3.txt"
print('\n\nLeitura do ficheiro de dados:',Ficheiro,'...\n\n')
dados=loadtxt(Ficheiro)
print('      t/s      Vin/V     Vc/V ')
print(35*'-')
for i in range(0,5):
    print((3*"%10.3f") % tuple(dados[i,:]))
print('     .....     .....     .....')
for i in range(-5,0):
    print((3*"%10.3f") % tuple(dados[i,:]))
print(35*'-','\n\n')
    
#%% Resolução do trabalho
#%%Declaração de variáveis
R=1*(10**6) #R= 1MΩ
C=sym('C')
t=dados[:,0]
Vin=dados[:,1]
Vc=dados[:,2]
#%%Exercicio 1
disp('Exercício 1:')
ti=0  #tempo inicial obtido pelos dados fornecidos
tf=87.5 #tempo final obtido pelos dados fornecidos
N=(len(dados))/3 #Número de amostragens
f=(N/(tf-ti))-1 #Cálculo da frequência de amostragem
dt=1/f #Cálculo do intervalo de tempo entre amostras
ttotal=87,500 #Tempo obtido pelo tf-ti dado pelos dados fornecidos
print('Número de amostras: ',N)
print('Intervalo de tempo entre amostras: ',dt,'s')
print('Frequência de amostragem',f,'Hz')
print('Tempo durante o qual ocorreu a aquisição dos sinais Vin e Vc: ',ttotal,'s')
#%%Exercicio 2
disp('\n\nExercício 2:')
pl.plot(t,Vc,label='Vc');pl.plot(t,Vin,label='Vin') #gráfico dos potenciais Vin e Vc
xlabel('t/s')
ylabel('Vin e Vc / V')
legend()
grid()
title(u'Representação gráfica de Vc e Vin em função do tempo')
show()
#%%Exercicio 3
disp('\n\nExercício 3:')
disp('Derivada númerica progressiva e momentos que iniciam a descarga do condensador')
dDados=[]
for i in range(1,len(dados)-1):
    dDados.append((dados[i+1]-dados[i-1])/(2*dt))
dDadosi = (dados[1]-dados[0])/dt
dDadosf = (dados[-1]-dados[-2])/dt
dDados = [dDadosi]+dDados+[dDadosf]
figure();
plot(t,dDados,'.r'); plot(t,dDados,'-b') #gráfico representativo da diferencial de "dados" (dDados)
#%%Exercicio 4
#%%alinea a
