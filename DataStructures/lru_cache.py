# ----------------------------------------------------------------------------------------------------
# IBM Confidential
# OCO Source Materials
# 5900-A3Q, 5737-H76
# Copyright IBM Corp. 2024
# The source code for this program is not published or other-wise divested of its trade
# secrets, irrespective of what has been deposited with the U.S. Copyright Office.
# ----------------------------------------------------------------------------------------------------

import threading
import time


class Node:
    """
    Node of the doubly linked list.
    """
    
    def __init__(self, key=None, value=None, expiry_time: int=1800):
        """
        The constructor for the node that would be used for cache.
        :key: The key for the value to be stored in cache.
        :value: The value to be stored in the cache.
        :expiry_time: The expiry time (in seconds) for the key-value pair in cache.
        """
        self.key = key
        self.value = value
        self.expiry_time = expiry_time
        self.insert_time = round(time.time())
        self.prev = None
        self.next = None

        return

class LRUCache:
    """
    Implementation of the LRU cache.
    """

    def __init__(self, capacity: int=128):
        """
        The constructor for initializing the cache variables.
        :capacity: The size of the cache.
        """
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lock = threading.RLock()

        return
  
    def _add_node(self, node: Node) -> None:
        """
        Adds a node to the doubly linked list used for cache.
        :node: The node to be added.

        :returns: None.
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

        return
  
    def _remove_node(self, node: Node) -> None:
        """
        Removes the given node from the doubly linked list for cache.
        :node: The node to be removed.

        :returns: None.
        """
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

        return
  
    def _move_to_head(self, node: Node) -> None:
        """
        Moves the given node to the head of the double linked list for cache.
        :node: The node to be moved to head.

        :returns: None.
        """
        self._remove_node(node)
        self._add_node(node)

        return
  
    def get(self, key: str):
        """
        Retrieves the value for the given key from the cache.
        :key: The key for which the value is to be retrieved.

        :returns: The value for the given key in cache, None otherwise.
        """
        value = None
        
        # Acquiring the lock in order to make the cache thread-safe
        with self.lock:
            if key in self.cache:
                node = self.cache[key]
                # Checking if the item has expired
                if round(time.time()) - node.insert_time > node.expiry_time:
                    # The key-value pair is expired, removing from cache
                    self._remove_node(node)
                else:
                    # Moving the used node to head
                    self._move_to_head(node)
                    value = node.value
        
        return value
  
    def put(self, key: str, value, expiry_time: int) -> None:
        """
        Puts the given key-value pair in the cache.
        :key: The key to be inserted in the cache.
        :value: The value to be inserted in the cache.
        :expiry_time: The expiry time (in seconds) for the key-value pair in cache.

        :returns: None.
        """
        
        # Acquiring the lock in order to make the cache thread-safe
        with self.lock:
            if key in self.cache:
                node = self.cache[key]
                node.value = value
                # Resetting the insert time
                node.insert_time = round(time.time())
                self._move_to_head(node)
            else:
                new_node = Node(key, value, expiry_time)
                self.cache[key] = new_node
                self._add_node(new_node)
                if len(self.cache) > self.capacity:
                    tail = self.tail.prev
                    self._remove_node(tail)
                    del self.cache[tail.key]
        
        return
