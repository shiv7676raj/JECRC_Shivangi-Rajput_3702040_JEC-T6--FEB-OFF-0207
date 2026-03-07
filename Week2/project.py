import time

class TODO:
    todos = []
    
    def add_todo(self, desc):
        dict={
                'id':int(time.time()),
                'desc':desc,
                'is_completed':False
            }
        self.todos.append(dict)
        print(f"{desc};Added Successfully")
    
    def remove_todo(self, id):
        for j in self.todos:
            if j['id']==id:
                self.todos.remove(j)
                print("Task removed.")
                return
    
    def display_todos(self):
        if len(self.todos)==0:
            return
        for i in self.todos:
            if i['is_completed']:
                print(f"{i['id']}:{i['desc']} -Completed")
            else:
                print(f"{i['id']}:{i['desc']} -Pending")


    def update_todo(self, id, new_desc):
        for i in self.todos:
            if i['id'] == id:
                i['desc'] = new_desc
                print("Task updated.")
    
    def toggle_mark_as_completed(self, id):
        for i in self.todos:
            if(id==i['id']):
                i['is_completed']=not i['is_completed']
    
    def completed_todos(self):
        if len(self.todos)==0:
            return
        for i in self.todos:
            if i['is_completed']:
                print(f'{i['desc']}')
    
    def incompleted_todos(self):
        if len(self.todos)==0:
            return
        for i in self.todos:
            if i['is_completed']==False:
                print(f'{i['desc']}')
    
