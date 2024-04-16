""" 
Here you have a class named IntArray with an implementation of 
an Array that can store integer values. It uses another class 
ReservedMemory (also provided) to store the integer values in 
memory as bytes (you can convert values to byte type or you can 
just use integer values between 0 and 255. Both are fine. In the 
code provided the latter form is used).
When instantiating an IntArray variable, the size of the array 
elements can be defined. By default this value is 2 bytes, that 
gives room to store values from -32768 to 32767 (65536 different 
values in total, i.e. 16 bit range)
Some internal methods and some public methods have been already 
implemented. Your job is to implement a new method "insert". The 
definition of the method is already present. Just replace the 
placeholder code provided with your own code.
This new insert method has to be able to insert a new element 
at whatever position/index of the array. For that a new array
 has to be created and the old content has to be copied making room for the new value

You will have to study a little bit the provided code to understand how it works. 
And you can use the already implemented methods as an example on what can be done.
Notice that ReservedMemory has a copy function you can use to copy the content 
of an old array to a new one. """
from __future__ import annotations
import ctypes

class ReservedMemory():
    """
    A class to reserve and handle a contigous area of memory. The
    constructor needs the size of the memory area (in bytes) to be
    reserved.
    """
    def __init__(self, size: int) -> None:
        """
        Initialize object allocating a memory area of given size
        """
        if not isinstance(size, int):
            raise(TypeError('Memory size must be a positive integer > 0!'))
        if not 1 <= size <= 65536:
            raise(ValueError('Reserved memory size must be between 1 and 65536 bytes!'))
        
        self._reserved_memory = ctypes.create_string_buffer(size)

    def __len__(self) -> int:
        return len(self._reserved_memory)

    def __repr__(self) -> str:
        """
        Custom representation of the reserved memory area
        """
        l = len(self._reserved_memory)
        plural = 's' if l>1 else ''
        str_repr = f"[{', '.join(str(ord(i)) for i in self._reserved_memory)}]"
        return f"ReservedMemory ({l} byte{plural}): {str_repr}"

    def copy(self, mem_source:ReservedMemory, count:int=None, source_index:int=0, destination_index:int=0) -> None:
        """
        Copy the content of another ReservedMemory object (mem_source)
        to this object's memory area. By default the whole source memory
        area is copied to the start of this object's memory area.
        
        Parameters:
        - mem_source: ReservedMemory source object (mandatory)
        - count: How many bytes or positions to copy.
                 Optional. Default: Source size - source_index
                 If not provided, copy from the beginning or source_index
                 until the end of source.
        - source_index: Source's start index or from where to copy the
                        content.
                        Optional. Default: 0
        - destination_index: Destination's start index or where to copy
                             the content.
                             Optional. Default: 0

        Usage example:
        # Copy source to the start of destination
        destination.copy(source)

        # Copy only 5 memory positions of source
        destination.copy(source, count=5)
        # or
        destination.copy(source, 5)
        
        # Copy source to destination starting at index 10
        destination.copy(source, destination_index=10)

        # Copy the first 5 memory positions of source to destination's index 10
        destination.copy(source, count=5, destination_index=10)

        # Copy 5 memory positions from source index 7 to destination's
        # index 10
        destination.copy(source, count=5, source_index=7, destination_index=10)
        # or
        destination.copy(source, 5, 7, 10)

        Copy area can't fall outside the bounds of the destination's
        memory area.
        """
        
        if not isinstance(mem_source, ReservedMemory):
            return TypeError('Source object must be a ReservedMemory object')
        
        if count is None:
            count = len(mem_source._reserved_memory) - source_index
        elif not isinstance(count, int):
            return TypeError('Count must be a positive integer > 0')
        elif count <= 0:
            return ValueError('Count must be a positive integer > 0')
        
        if not isinstance(source_index, int):
            return TypeError('Source index must be a positive integer >= 0')
        elif 0 > source_index >= len(mem_source._reserved_memory):
            return IndexError('Source index out of bounds!')

        if not isinstance(destination_index, int):
            return TypeError('Destination index must be a positive integer >= 0')
        elif 0 > destination_index >= len(self._reserved_memory):
            return IndexError('Destination index out of bounds!')

        if count > len(self._reserved_memory):
            return IndexError('Source is bigger than destination!')
        elif source_index + count > len(mem_source._reserved_memory):
            return IndexError('Source copy area out of bounds!')
        elif destination_index + count > len(self._reserved_memory):
            return IndexError('Destination copy area out of bounds!')

        self._reserved_memory[destination_index:destination_index+count] = mem_source._reserved_memory[source_index:source_index+count]

    def __getitem__(self, k:int) -> int:
        """
        Return value at index k
        """
        if not isinstance(k, int):
            raise TypeError('Index must be a positive integer >= 0')
        elif not 0 <= k < len(self._reserved_memory):
            raise IndexError('Index is out of bounds!')
        
        return ord(self._reserved_memory[k])

    def __setitem__(self, k:int, val:int) -> None:
        """
        set value at index k with val
        """
        if not isinstance(k, int):
            raise TypeError('Index must be a positive integer >= 0')
        elif not (0 <= k < len(self._reserved_memory)):
            raise IndexError('Index is out of bounds!')
        
        self._reserved_memory[k] = val

class IntArray():
    """
    A class to implement an Array Data Structure that accepts integer values
    between -(2**(n-1)) and (2**(n-1))-1 (being n the number of bits per element).
    By default, element size is 2 bytes (16 bits), so accepted values go
    from -(2**15) to (2**15)-1, that is from -32768 to 32767. 
    Python does not have a internal type with these characteristics, so values
    are accepted as normal Python int type and then converted to be stored.

    IntArray uses static arrays to hold the values, but allows to expand or
    shrunk the array internally copying the values to a new static array.

    Parameters (IntArray creation):
    - bytes_per_element: How many bytes per element should be reserved. 

    Supported methods:
    - Array creation
    - Append: Insert at the end
    - Pop: Delete from the end
    """

    def __init__(self, bytes_per_element:int = 2) -> None:
        self._resmem = None
        self._size = 0  # Logical size
        self._bytes_per_element = bytes_per_element
        self._shift_val = 2**((self._bytes_per_element * 8)-1)
        self._min_val = -self._shift_val
        self._max_val = self._shift_val - 1

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self) -> int:
        if self._iter_index < self._size:
            self._iter_index += 1
            return self.__getitem__(self._iter_index-1)
        else:
            raise StopIteration

    def __repr__(self) -> str:
        """
        Custom representation of the IntArray
        """
        if not self._resmem:
            return "Empty IntArray"
        l = self._size
        plural = 's' if l>1 else ''
        str_repr = f"[{', '.join(str(v) for v in self)}]"
        return f"IntArray ({l} element{plural}): {str_repr}"

    def __setitem__(self, k:int, val:int) -> None:
        """
        Set value at index k with val.
        """
        if not isinstance(val, int) or not self._min_val <= val <= self._max_val:
            raise TypeError(f'Value must be an integer between {self._min_val} and {self._max_val}')

        # Convert or shift the value to be suitable to be stored.
        # Value to be stored must be in the positive range from 0 to (2**bits_per_element)-1
        # For 2 bytes that is from 0 to 65535
        val_to_store = val + self._shift_val
        # Store the bytes of the value in Little-endian (https://en.wikipedia.org/wiki/Endianness)    
        for byte_index in range(self._bytes_per_element):
            self._resmem[k*self._bytes_per_element+byte_index] = (val_to_store >> (8*byte_index)) & 255

    def __getitem__(self, k:int) -> int:
        """
        Return value at index k
        """

        # Read stored bytes in Little-endian and restore original value
        stored_val = 0
        for byte_index in range(self._bytes_per_element):
            stored_val |= self._resmem[k*self._bytes_per_element+byte_index] << (8*byte_index)
        return (stored_val - self._shift_val)

    def append(self, val: int) -> None:
        """
        Append an element to the end of the array
        """
        if not isinstance(val, int) or not self._min_val <= val <= self._max_val:
            raise TypeError('Value must be an integer between {self._min_val} and {self._max_val}')
        
        # Update array's size
        self._size += 1

        # Reserve a new memory area with the new size.
        # It is _bytes_per_element bigger than the current one
        new_resmem = ReservedMemory(self._size*self._bytes_per_element)

        # Copy the old reserved memory area (if there was one)
        if self._resmem:
            new_resmem.copy(self._resmem)

        # The new created reserved memory area will be the one to be used
        # from now on
        self._resmem = new_resmem

        # Store the new value at the end of the array
        self.__setitem__(self._size-1, val)

    def pop(self) -> int:
        """
        Remove an element from the end of the array and return its value
        """
        # Elements can not be removed from empty arrays
        if self._size == 0:
            return None

        # Get the last element's value
        val = self.__getitem__(self._size-1)
        
        # Decrease the size of the array
        self._size -= 1

        # Find out the need for reserved memory
        if self._size > 0:
            # if new size is still bigger than 0
            # reserve a new memory area with the new size.
            # It is _bytes_per_element smaller than the current one
            new_resmem = ReservedMemory(self._size*self._bytes_per_element)
            # And copy the old memory area (except last element)
            new_resmem.copy(self._resmem, count=self._size*self._bytes_per_element)
        else:
            # If new size is 0, there is no need to reserve memory for it
            new_resmem = None

        # Make the new memory area value the current one
        self._resmem = new_resmem

        # Return the last element's value that was stored at the beginning
        return val
    
    #exercise 1
    def insert(self, index:int, val:int) -> None:
        ### Remove this comment and the `return` line and write your code here!
        # Validate the index to be within bounds for insertion
        if not 0 <= index <= self._size:
            raise IndexError("Insertion index is out of bounds")

        # prepara new memory space
        new_resmem = ReservedMemory((self._size + 1) * self._bytes_per_element)

        # Copy elements before the insertion index
        if index > 0:
            new_resmem.copy(self._resmem, count=index * self._bytes_per_element)

        # set the new value
        temp_resmem = self._resmem
        self._resmem = new_resmem
        self.__setitem__(index,val)
        self._resmem = temp_resmem

        # Copy elements after the insertion index
        if index < self._size:
            new_resmem.copy(self._resmem, source_index=index * self._bytes_per_element, destination_index=(index + 1) * self._bytes_per_element, count=(self._size - index) * self._bytes_per_element)

        # Update to use the new memory
        self._resmem = new_resmem
        self._size += 1

    # exercise 2
    def remove(self, index:int) -> int:
        ### Remove this comment and the `pass` line and write your code here!
        if self._size == 0:
            return None
        #Validate the index
        if not 0 <= index < self._size:
            raise IndexError('Index is out of bounds!')

        # retrieve the values at the given index
        val = self. __getitem__(index)

        # decrease the size of the array
        self._size -= 1

        #If the array is now empty, clear the reserved memory
        if self._size == 0:
            self._resmem = None
            return val

        # otherwise prepare a new memory area with the reduced size
        new_resmem = ReservedMemory(self._size * self._bytes_per_element)
        
        # copy elements before the removal index
        if index> 0:
            new_resmem.copy(self._resmem, count= index * self._bytes_per_element)
            
        # copy elements after the removal index to the new position
        if index <= self._size:
            new_resmem.copy(self._resmem, source_index=(index+1) * self._bytes_per_element, destination_index=index * self._bytes_per_element, count=(self._size - index) * self._bytes_per_element)
            
        # update to use the new memory area
        self._resmem = new_resmem
        
        return val
    # exercise 3
    def search(self, value: int) -> int:
        """
        Search method for the array

        Parameters:
        - 'value': value to search

        Returns:
          First index position where the value is found or -1 if not found
        """
        for index in range(self._size):
            if self.__getitem__(index) == value:
                return index
        return -1



# TESTING THE EXERCISES

# Test Script for IntArray class
def test_int_array():
    # Testing append method and length
    array = IntArray()
    for i in range(6):
        array.append(i)
    print("After append operations:", array)
    print("Length should be 6:", len(array))

    # Testing insert at middle
    array.insert(3, 999)
    print("After insert at middle:", array)

    # Testing insert at end
    array.insert(7, 888)
    print("After insert at end:", array)

    # Testing insert at beginning
    array.insert(0, 777)
    print("After insert at beginning:", array)

    # Testing index out of bounds
    try:
        array.insert(100, 555)
    except IndexError as e:
        print("IndexError as expected:", e)

    # Test inserting into an empty array
    empty_array = IntArray()
    empty_array.insert(0, 444)
    print("Insert into empty array:", empty_array)

    # Testing with larger numbers and different byte sizes
    large_array = IntArray(bytes_per_element=4)
    for i in range(6):
        large_array.append(i*10000)
    large_array.insert(2, 12345678)
    print("Large array with insert:", large_array)

def test_remove():
    print("Test 1: Remove from middle")
    array = IntArray()
    for i in range(6):  # Create an array [0, 1, 2, 3, 4, 5]
        array.append(i)
    val = array.remove(3)  # Remove element at index 3 (value 3)
    print(f"Removed Value: {val}, Array after removal: {array}")  # Expected: [0, 1, 2, 4, 5]

    print("\nTest 2: Remove from start")
    array = IntArray()
    for i in range(6):
        array.append(i)
    val = array.remove(0)  # Remove first element
    print(f"Removed Value: {val}, Array after removal: {array}")  # Expected: [1, 2, 3, 4, 5]

    print("\nTest 3: Remove from end")
    array = IntArray()
    for i in range(6):
        array.append(i)
    val = array.remove(5)  # Remove last element
    print(f"Removed Value: {val}, Array after removal: {array}")  # Expected: [0, 1, 2, 3, 4]

    print("\nTest 4: Remove with index out of bounds")
    array = IntArray()
    for i in range(6):
        array.append(i)
    try:
        array.remove(6)  # Attempt to remove non-existent element
    except IndexError as e:
        print(f"Caught an exception as expected: {e}")

    print("\nTest 5: Remove from empty array")
    array = IntArray()
    val = array.remove(0)  # Attempt to remove from an empty array
    print(f"Expected None, got: {val}")

    print("\nTest 6: Comprehensive removal")
    array = IntArray(bytes_per_element=3)
    for i in range(6):
        array.append(i)
    while len(array) > 0:
        print(f"Removing {array.remove(0)}, New array: {array}")  # Sequentially remove all elements

def test_search():
    print("Test 1: Search for existing value")
    array = IntArray()
    for i in range(6):  # Create an array [0, 2, 4, 6, 8, 10]
        array.append(i * 2)
    print("Index of 8:", array.search(8))  # Should return 4

    print("\nTest 2: Search for a value at the beginning")
    array = IntArray()
    for i in range(6):  # Create an array [1000, 999, 998, 997, 996, 995]
        array.append(1000 - i)
    print("Index of 1000:", array.search(1000))  # Should return 0

    print("\nTest 3: Search for a value at the end")
    array = IntArray()
    for i in range(6):
        array.append(1000 - i)
    print("Index of 995:", array.search(995))  # Should return 5

    print("\nTest 4: Search after modifications")
    array = IntArray()
    for i in range(6):
        array.append(1000 - i)
    array.pop()  # Removes last item (995)
    array.append(500)  # Append 500 at the end
    print("Index of 500:", array.search(500))  # Should return 5

    print("\nTest 5: Search for non-existing value")
    array = IntArray()
    for i in range(6):
        array.append(1000 - i)
    print("Index of 1001:", array.search(1001))  # Should return -1

    print("\nTest 6: Search for repeated values")
    array = IntArray()
    for i in range(3):
        array.append(2)  # Create an array [2, 2, 2]
    array.append(3)  # Now array is [2, 2, 2, 3]
    print("First index of 2:", array.search(2))  # Should return 0
    print("Index of 3:", array.search(3))  # Should return 3




test_int_array()
test_remove()
test_search()

