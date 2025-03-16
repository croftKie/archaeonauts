import random
class MapManager():
    def __init__(self, gm):
        self.gm = gm
        self.active_map = None
        self.puzzle_manager = None,
        self.gen_map = []
        self.connection_line = None
    def generate_map(self, size = 8):
        ## select start point cell
        ## check for all surrounding open cell
            ## store list of open cells
        ## select first open cell
            ## check if selected open cell has surrounding open cell
                ## if no, return to check next cell in list
                ## if yes
                    ## replace possible open cells with those surrounding current selected cell
                    ## assign cell data to current selected cell
        spawn_seed = [0,0,0,0,1,2,2,3,3,3]

        map = [];
        for i in range(0, size):
            row = []
            gen_row = []
            con_line = []
            for j in range(0, size):
                spawn = spawn_seed[random.randrange(0, len(spawn_seed))]
                row.append([{
                    "id": f"{i}-{j}",
                    "type": spawn,
                    "discovered": False,
                }])
                block_type = " "
                block = "[ ]" if j == size - 1 else "[ ]-" 
                gen_row.append(block)
                con_line.append(" | " if j == size - 1 else " |  ")
            map.append(row)
            self.gen_map.append(gen_row)
            self.connection_line = "".join(con_line)

        self.active_map = map

    
    def get_active_map(self):
        return
