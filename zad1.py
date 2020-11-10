
class Planety():
   def newWiek(self, wiek, planeta):
      """

      >>> page = Planety()
      >>> page.newWiek(2134835688,"Merkury")
      280.88
      >>> page.newWiek(2134835688,"Wenus")
      109.96
      >>> page.newWiek(2134835688,"Mars")
      35.97
      >>> page.newWiek(2134835688,"Jowisz")
      5.7
      >>> page.newWiek(2134835688,"Saturn")
      2.3
      >>> page.newWiek(2134835688,"Uran")
      0.81
      >>> page.newWiek(2134835688,"Neptun")
      0.41
      >>> page.newWiek("123213", "Uran")
      Traceback (most recent call last):
        ...
      Exception: Error in program
      >>> page.newWiek(None,None)
      Traceback (most recent call last):
        ...
      Exception: Error in program
      """
      earth = 31557600
      dict = {
          "Ziemia": 1,
          "Merkury": 0.2408467,
          "Wenus": 0.61519726,
          "Mars": 1.8808158,
          "Jowisz": 11.862615,
          "Saturn": 29.447498,
          "Uran": 84.016846,
          "Neptun": 164.79132
      }

      if type(wiek) == int and type(planeta) == str:
         if wiek > 0 and (planeta in dict):
            x = wiek / (dict[planeta] * earth)
            return (round(x, 2))
         else:
            raise Exception("Error in program")
      else:
         raise Exception("Error in program")

if __name__ == "__main__":
    import doctest
    doctest.testmod()