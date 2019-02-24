import csv

class mySorter():
    """ CLASS THAT HANDLES CSV FILES AND IMPLEMENTS METHODS FOR SORTING THEIR CONTENT"""
    
    def __init__(self, alist = None, sorted = None, fileini = None, filefin = None):
        self.alist = alist
        self.sorted = sorted
        self.fileini = fileini
        self.filefin = filefin
        
    def set_input_data(self, file_path_name: str):
        """This methods sets the information about the file that will be used to read the data"""
        self.fileini = file_path_name
        self.alist = []
        with open(self.fileini) as csvfile:
            readCSV = csv.reader(csvfile, delimiter = ',')
            for row in readCSV:
                for element in row:
                    self.alist.append(element)
    
    def set_output_data(self, alist, file_path_name: str):
        """This methods sets the information about the file that will be used to store the sorted data"""
        self.alist = alist
        self.filefin = file_path_name
        with open(self.filefin, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow(self.alist)
    
    def execute_merge_sort(self, arr):
        """This methods sorts the data contained in the file specified"""
        pass

    
    def execute_heap_sort():
        """This methods sorts the data contained in the file specified"""
        pass
    
    def execute_quick_sort(self, array, begin=0, end=None):
        """This methods sorts the data contained in the file specified"""
        if end is None:
            end = len(array) - 1
        return quick_sort_recursion(array, begin, end)
    
    def get_performance_data():
        """This method returns the performance data associated to the last sorting execution
            [Number of Records Sorted, TimeConsumed, StartTime, EndTime]"""
        pass
    
def _partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = _partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)

def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)

alist1 = mySorter()
print(type(alist1))
alist1.set_input_data('simplefile1.csv')
print(alist1.alist, type(alist1))
alist1.execute_quick_sort(alist1.alist)
print(alist1.alist, type(alist1))
#alist1.execute_merge_sort(alist1.alist)
#print(alist1.alist, type(alist1))
#mergeSort(alist1.alist)
#print(alist1.alist)
#alist1.set_output_data(alist1.alist, 'alist1ordered.csv')