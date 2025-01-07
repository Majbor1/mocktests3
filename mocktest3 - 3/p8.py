class Matrix:
    def __init__(self, data):
        self.data = data
    
    def rows(self):
        return len(self.data)
    
    def cols(self):
        return len(self.data[0])

    def transpose(self):
        """Zwraca nową macierz będącą transpozycją bieżącej macierzy."""
        transposed_data = []  # Tworzymy pustą listę na macierz transponowaną
    
        # Iterujemy po indeksach kolumn w oryginalnej macierzy
        for i in range(self.cols()):
            new_row = []  # Tworzymy nowy wiersz dla macierzy transponowanej
        
            # Iterujemy po indeksach wierszy w oryginalnej macierzy
            for j in range(self.rows()):
                # Dodajemy element z (j, i) oryginalnej macierzy do nowego wiersza
                new_row.append(self.data[j][i])
        
            # Dodajemy nowy wiersz do transponowanej macierzy
            transposed_data.append(new_row)

        return transposed_data
def main():
    m = Matrix([[1, 2, 3], [4, 5, 6]]) 
    print(m.rows())
    print(m.cols())
    print(m.transpose())

if __name__ == "__main__":
    main()