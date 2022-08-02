import json, math, urllib.request

class utils:

    def loadJsonDataset(url):
        with urllib.request.urlopen(url) as json_dataset:
            return json.load(json_dataset)

    def check_input_integer(inputValue):
            try:            
                int(inputValue)
                return True
            except ValueError:                     
                return False

    def printTwoListCombination(list_a,list_b):
        combination_result=""
        for x_index in range(0,len(list_a)):
            for y_index in range(0,len(list_b)):
                combination_result+="- "+str(list_a[x_index])+"\t"+str(list_b[y_index])+"\n"
        return combination_result

    def printOneListCombination(list_a):
        combination_result=""
        for x_index in range(0,len(list_a)):
            for y_index in range(x_index+1,len(list_a)):
                combination_result+="- "+str(list_a[x_index])+"\t"+str(list_a[y_index])+"\n"
        return combination_result

class NBAPlayersHeightsRepository:   

    def __init__(self, url):
        self.dataset=utils.loadJsonDataset(url)
        self.heights_dict = {}
        self.min_height = math.inf
        self.max_height = 0
        self._loadHeightsDict()
    
    def _loadHeightsDict(self):
        for nba_player in self.dataset['values']:
            nba_player_height=int(nba_player['h_in'])
            if(nba_player_height<=self.min_height):
                self.min_height=nba_player_height
            if(nba_player_height>=self.max_height):
                self.max_height=nba_player_height                   

            if(nba_player_height in self.heights_dict):
                self.heights_dict[nba_player_height].append(nba_player['first_name']+" "+nba_player['last_name'])
            else:
                self.heights_dict[nba_player_height]= [nba_player['first_name']+" "+nba_player['last_name']]

    def _check_input_range(self,target):
        if(utils.check_input_integer(target)):
            if(int(target)<2*self.min_height or int(target)>2*self.max_height):                
                return False,"No matches found"
            return True,"Number in range"        
        return False, "The input value should be an Integer"
    
    def search_players_by_heights_sum(self,target):
        validation_input,validation_message=self._check_input_range(target)
        if validation_input:
            target=int(target)
            sorted_heights=sorted(list(self.heights_dict.keys()))
            players_pairs=""        
            for height in sorted_heights:  
                if(height>target//2):
                    break                    
                complement= target-height
                if complement == height:
                    players_pairs=utils.printOneListCombination(self.heights_dict[height])
                elif complement in self.heights_dict:
                    players_pairs=utils.printTwoListCombination(self.heights_dict[height],self.heights_dict[complement])            
            return players_pairs if players_pairs!="" else "No matches found"
        return validation_message     

def main():
    target_sum=input()
    nba_player_data=NBAPlayersHeightsRepository("https://mach-eight.uc.r.appspot.com/")    
    print(nba_player_data.search_players_by_heights_sum(target_sum))

if __name__ == '__main__':
    main()

#main()