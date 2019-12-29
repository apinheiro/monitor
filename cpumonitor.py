#!/usr/bin/python3

import psutil
import asyncio
from datetime import datetime
import time


#TODO: Criar o sistema de pacote para este programa.

logfile = "/var/log/monitorcpu/saida.data"

def retornaValores(cpus,qtde,datahora):
   sair = True
   for i in range(qtde):
       sair = False if cpus[i].idle != 100.0 else True
   
   if sair:
       return

   for j in range(qtde):
      print("%s\t%d\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f" % 
              (datahora, j, cpus[j].user,cpus[j].nice, cpus[j].system,cpus[j].idle, 
              cpus[j].iowait,cpus[j].irq,cpus[j].guest,cpus[j].softirq),
              file=open(logfile,"a+"))
        
def ajusta_tempo():
    hora = datetime.timestamp(datetime.now())
    men = int(hora) + 0.9
    time.sleep(men - hora)


if __name__ == "__main__":
    
    try:
        ncpus = psutil.cpu_count()
        ajusta_tempo()

        while True:
            now  = datetime.now()
            timestamp = datetime.timestamp(now)

            # Buscando os dados de CPU
            cpus = psutil.cpu_times_percent(interval=None, percpu=True)

            # TODO: Buscando os dados de memória

            # TODO: Transformar esta chamada em chamada assíncrona
            retornaValores(cpus,ncpus,now)

            now1  = datetime.now()
            inter = datetime.timestamp(now1) - timestamp
            time.sleep(.49 - inter)
    except KeyboardInterrupt:
        print("Programa encerrado")
   
