

from queue import Queue

int_queue= Queue()



int_queue.put(3)
int_queue.put(1)
int_queue.put(4)
print(int_queue.get()) ## What will this return and why?
int_queue.put(2)
print(int_queue.get()) ## What will this return and why?



