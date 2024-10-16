import math

class CollisionService:
    @staticmethod
    def is_collision(entity1, entity2):
        distance = math.sqrt(math.pow(entity1.x - entity2.x, 2) + math.pow(entity1.y - entity2.y, 2))
        return distance < 27
