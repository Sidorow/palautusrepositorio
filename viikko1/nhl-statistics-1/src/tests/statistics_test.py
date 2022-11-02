import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
  def get_players(self):
    return [
      Player("Semenko", "EDM", 4, 12),
      Player("Lemieux", "PIT", 45, 54),
      Player("Kurri",   "EDM", 37, 53),
      Player("Yzerman", "DET", 42, 56),
      Player("Gretzky", "EDM", 35, 89)
    ]


class TestStatistics(unittest.TestCase):
  def setUp(self):
    self.statistics = Statistics(PlayerReaderStub())
    
  def test_haku_palauttaa_pelaajan(self):
    self.assertAlmostEqual(str(self.statistics.search("Semenko")), "Semenko EDM 4 + 12 = 16")
    
  def test_virheellinen_haku_ei_palauta_mitaan(self):
    self.assertAlmostEqual(str(self.statistics.search("MattiPekka")), "None")
    
  def test_top_palauttaa_oikean_listan(self):
    lista = self.statistics.top(2)
    top3 = []
    for player in lista:
      top3.append(str(player))
    expected = ['Gretzky EDM 35 + 89 = 124', 'Lemieux PIT 45 + 54 = 99', 'Yzerman DET 42 + 56 = 98']
    self.assertCountEqual(top3, expected)
    
  def test_team_palauttaa_oikean_pelaajan(self):
    lista = self.statistics.team("PIT")
    lista2 = []
    for player in lista:
      lista2.append(str(player))
    expected = ['Lemieux PIT 45 + 54 = 99']
    self.assertCountEqual(lista2, expected)