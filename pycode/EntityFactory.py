import random
from pycode.Background import Background
from pycode.Const import WIN_HEIGHT, WIN_WIDTH
from pycode.Enemy import Enemy
from pycode.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(20, WIN_HEIGHT - 20)))
            
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(20, WIN_HEIGHT - 20)))