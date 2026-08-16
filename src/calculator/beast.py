class Beast():
    """A wild beast doing lots of stuff."""
    
    def __init__(self, name, size):
        self.name = name
        self.size = size
        
    def roar(self, volume):
        """Make some noise.
        
        Args:
            volume (int): Volume of the sound.
            
        Returns:
            (str): A load roar.
        """
        return "Roar-"*volume
    
    @property
    def name(self):
        """Get the beast name."""
        return self.name
    
    