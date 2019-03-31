from Models.SimulazioneModel import SimulazioneModel
from Models.ProblemiSimulazioneModel import ProblemiSimulazioneModel
import time


def CheckEnd(simulazione):
    sim=SimulazioneModel.find_by_nome(simulazione)
    now=int(time.time())
    try:

        expected_end=sim.inizio+sim.durata
        if expected_end<now:
            if expected_end<now+180:
                ProblemiSimulazioneModel.delete_by_simulazione_id(sim.id)
                sim.delete_from_db()
            return True
        return False
    except:
        return False
