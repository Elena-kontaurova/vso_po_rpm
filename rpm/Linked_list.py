class LinkedList: 
 
    class Item: 
        value = None 
        next = None 
 
        def __init__(self, value): 
            self.value = value 
 
    head:Item = None 
     
    def append_begin(self, value): 
        item = LinkedList.Item(value) 
        item.next = self.head 
        self.head = item 
 
    def append_end(self, value): 
        current = self.head 
        if current is None: 
            self.head = LinkedList.Item(value) 
            self.head.value = value 
            return 
         
        while current.next: 
            current = current.next 
         
        item = LinkedList.Item(value) 
        current.next = item 
 
 
    def append_by_index(self, value, index): 
        '''Метод всавляет значение по указанному индексу, 
        оставшиеся элементы сдвигаются''' 
        new_item = LinkedList.Item(value) 
 
        if index == 0: 
            new_item.next = self.head 
            self.head = new_item 
            return 
         
        current = self.head 
        count = 0 
        while count < index -1 and current.next: 
            current = current.next 
            count += 1 
 
        new_item.next = current.next 
        current.next = new_item  
 
    def __len__(self): 
        ''' возращать количество элементов списка''' 
        count = 0 
        current = self.head 
        while current: 
            count += 1 
            current = current.next 
        return count 
 
 
    def remove_first(self): 
        '''удаление первого элемента''' 
        if self.head is not None: 
            self.head = self.head.next 
         
     
    def remove_last(self): 
        ''' удаление последнего элемнта''' 
        if self.head is None: 
            raise ValueError("Удаление невозможно") 
        if self.head.next is None: 
            raise ValueError("Удаление невозожно") 
        
        current = self.head
        while current.next:
            current = current.next
            
        current.next = None
 
         
 
 
    def remove_at(self, value):
        '''Удаление первого на значению'''
        current = self.head
        if current is not None and current.value == value:
            self.head = current.next
            return

        prev = None
        while current is not None:
            if current.value == value:
                prev.next = current.next
                return
            prev = current
            current = current.next
        
    def remove_first_value(self, value):
        '''Удаление первого найденного по значению '''
        current = self.head
        prev = None

        
        while current is None:
            if current.value == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return 
            prev = current
            current = current.next
            
 
    def remove_last_value(self, value): 
        ''' удаление последнего найденного по значению ''' 
        current = self.head
        prev = None
        last_found = None
        
        while current is not None:
            if current.value == value:
                last_found = current
            prev = current
            current = current.next
            
        if last_found is None:
            raise ValueError("Удаление невозможно")
        if last_found == self.head:
            self.head = last_found.next
        else:
            prev.next = last_found.next 
     
         
 
my_list = LinkedList() 
my_list.append_begin(4) 
my_list.append_begin(5) 
my_list.append_begin(6) 
my_list.append_by_index(7, 1) 
my_list.append_begin(8) 
my_list.append_begin(9) 
my_list.append_begin(1) 
my_list.append_begin(5) 
my_list.remove_first() 
my_list.remove_last() 
my_list.remove_at(6)
my_list.remove_first_value(7)
my_list.remove_last_value(5)
print(len(my_list))
