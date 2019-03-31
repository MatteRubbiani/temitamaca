from flask_restful import Resource, request
from Models.SimulazioneModel import SimulazioneModel
from Models.ProblemiSimulazioneModel import ProblemiSimulazioneModel
from Models.ProblemaModel import ProblemaModel
from Models.GaraModel import GaraModel
import time
class GetGare(Resource):

    def get (self):
        return [{
            "nome":"gara",
            "descrizione":"questa e' una gara",
            "autore":"Matteo",
            "numeroProblemi":10

        },
        {
            "nome":"No-Skin",
            "descrizione":"anche questa e' una gara",
            "autore":"Sempre Matteo",
            "numeroProblemi":20

        },
        {
            "nome":"LA-LONGA-DANCE",
            "descrizione":"questa non e' una gara",
            "autore":"ILREDD",
            "numeroProblemi":8

        },
        {
            "nome":"Bianca neve e i 7 silvestri",
            "descrizione":"questa sembra una gara",
            "autore":"IO",
            "numeroProblemi":15

        },
        {
            "nome":"MATTEO RUBBIANI",
            "descrizione":"questa e'",
            "autore":"Rubbia The Best",
            "numeroProblemi":12

        }

        ]
