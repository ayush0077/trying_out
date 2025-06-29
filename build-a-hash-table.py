** start of main.py **

class HashTable:
    def __init__(self):
        # collection maps: hash_value -> {original_key: value, ...}
        self.collection = {}

    def hash(self, key: str) -> int:
        """Return sum of Unicode values of characters in key."""
        return sum(ord(char) for char in key)

    def add(self, key, value):
        """Add a key-value pair to the hash table."""
        hashed = self.hash(key)

        # Create bucket if it doesn't exist
        if hashed not in self.collection:
            self.collection[hashed] = {}

        # Store key-value inside bucket
        self.collection[hashed][key] = value

    def remove(self, key):
        """Remove a key-value pair if it exists."""
        hashed = self.hash(key)

        if hashed in self.collection and key in self.collection[hashed]:
            del self.collection[hashed][key]

            # Optional cleanup: remove empty bucket
            if not self.collection[hashed]:
                del self.collection[hashed]

    def lookup(self, key):
        """Return value associated with key or None."""
        hashed = self.hash(key)

        if hashed in self.collection and key in self.collection[hashed]:
            return self.collection[hashed][key]

        return None


** end of main.py **

