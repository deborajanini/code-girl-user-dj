from uuid import uuid4

class UserDatabase: #criar uma instancia
    
    users = []
    
    def __init__(self): #inicializador/construtor
        pass #iniciar a conexão com o banco na tabela user

    def add_user(self,user: dict):
        user['id'] = str(uuid4())#2º pegar o user e dar um id para ele
        self.users.append(user) # 1º antes de usar o apeend
        #tem que criar um ID aleatório para ele então from 
        #uuid import uuid4 - que gera uma sting aleatória
        #depois que criou um id para o usuário que eu vou salvá-lo

        #agora por fim, vou retornar o novo usuário com o id dele
        return user

        """
        AGORA IMPLEMENRTAÇÃO DOS OUTRO MÉTODOS SEGUINDO
        A MESMA LÓGICA DO MÉTODO ACIMA DEMONSTRADO
        """
    def get_user(self, user_id: str):  #pega o id de cada usuário definido
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None

    #agora quero pegar todos os usuários
    #que é simplesmente retornar a lista de usuários:
    def  get_users(self):
        return self.users
    
    #método de update
    #i = index, u = user

    def update_user(self, user_id ,new_user:dict):
        for index, user in enumerate(self.users):
            if user['id'] == user_id:
                self.users[index].update(new_user)
                return self.users[index] 
        return None


    #método de delete
    #i = index, u = user

    def delete_user(self, user_id:str):
        for index, user in enumerate(self.users):
            if user['id'] == user_id:
                self.users.pop(index)
                return True
        return False