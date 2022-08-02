import unittest
from test import NBAPlayersHeightsRepository

class Testing(unittest.TestCase):
    def test_Target_alphanumeric(self):
        target_sum="15o"                        
        result=NBAPlayersHeightsRepository("https://mach-eight.uc.r.appspot.com/").search_players_by_heights_sum(target_sum)
        self.assertEqual("The input value should be an Integer",result)

    def test_Target_float(self):
        target_sum="15.5"                        
        result=NBAPlayersHeightsRepository("https://mach-eight.uc.r.appspot.com/").search_players_by_heights_sum(target_sum)
        self.assertEqual("The input value should be an Integer",result)

    def test_Target_out_upper_bound(self):
        target_sum="181"                        
        result=NBAPlayersHeightsRepository("https://mach-eight.uc.r.appspot.com/").search_players_by_heights_sum(target_sum)
        self.assertEqual("No matches found",result)

    def test_Target_out_lower_bound(self):
        target_sum="137"                        
        result=NBAPlayersHeightsRepository("https://mach-eight.uc.r.appspot.com/").search_players_by_heights_sum(target_sum)
        self.assertEqual("No matches found",result)

    def test_pair_doesnt_exist(self):
        target_sum="178"                        
        result=NBAPlayersHeightsRepository("https://mach-eight.uc.r.appspot.com/").search_players_by_heights_sum(target_sum)
        self.assertEqual("No matches found",result)

    def test_pair_139(self):
        target_sum="139"                        
        result=NBAPlayersHeightsRepository("https://mach-eight.uc.r.appspot.com/").search_players_by_heights_sum(target_sum)
        expected_result="- Nate Robinson\tBrevin Knight\n- Nate Robinson\tMike Wilks\n"
        self.assertEqual(result,expected_result)

    def test_pair_142(self):
        target_sum="142"                        
        result=NBAPlayersHeightsRepository("https://mach-eight.uc.r.appspot.com/").search_players_by_heights_sum(target_sum)
        expected_result="- Chucky Atkins\tSpeedy Claxton\n"
        self.assertEqual(result,expected_result)
    
    def test_pair_177(self):
        target_sum="177"                        
        result=NBAPlayersHeightsRepository("https://mach-eight.uc.r.appspot.com/").search_players_by_heights_sum(target_sum)
        expected_result="- Zydrunas Ilgauskas\tYao Ming\n"
        self.assertEqual(result,expected_result)

if __name__ == '__main__':
    unittest.main()
