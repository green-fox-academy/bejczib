class Elem(object):
    __slots__ = ['value', 'next']

    def __repr__ (self):
        return '({}, {})'.format(self.value, self.next)

def new_elem(value):
    elem = Elem()
    elem.value = value
    elem.next = None
    return elem

def at(head, index):
    elem = head
    i= 0
    while i < index:
        elem = elem.next
        i += 1
    return elem

def append(head, value):
    end = head
    while end.next is not None:
        end = end.next
    end.next = new_elem(value)
    return head

def insert(head, index, value):
    if index ==0:
        new = new_elem(value)
        new.next = head
        return new


    prev = at(head, index-1)

    # prev = head
    # i = 0
    # while i < index-1:
    #     prev = prev.next
    #     i += 1

    new = new_elem(value)
    new.next = prev.next
    prev.next = new

    return head

def remove(head, index):
    if index == 0:
        alma = head.next #Dear Eggdice, this value is only exist, bacause of the better understanding
        return alma

    prev = at(head, index-1)
    # prev = head
    # n = 0
    # while n < index-1:
    #     prev = prev.next
    #     i += 1
    prev.next = prev.next.next
    return prev
