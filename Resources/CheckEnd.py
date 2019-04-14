from Models.SimulazioneModel import SimulazioneModel
from Models.ProblemiSimulazioneModel import ProblemiSimulazioneModel
import time


def CheckEnd(simulazione):
    sim=SimulazioneModel.find_by_nome(simulazione)
    now=int(time.time())
    try:
        expected_end=sim.inizio+sim.durata
        if expected_end<now:
            if expected_end>now+1200:
                ProblemiSimulazioneModel.delete_by_simulazione_id(sim.id)
                sim.delete_from_db()
            return True
        return False
    except:
        return False

def CheckStatus(simulazione):
        sim=SimulazioneModel.find_by_nome(simulazione)
        if sim == None:
            return 0
        finished=CheckEnd(simulazione)
        sim1=SimulazioneModel.find_by_nome(simulazione)
        if sim1 == None:
            return 0
        if finished:
            return 1

        if sim1.started:
            return 2

        return 3
        #0__non esiste, 1__e' finita, 2__e' in corso, 3__non e' ancora iniziata
