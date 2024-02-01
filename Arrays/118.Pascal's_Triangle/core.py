def wynik(numsRows):
    if numsRows == 0:
        return []
    if numsRows == 1:
        return [[1]]

    triangle = [[1]]
    for i in range(1, numsRows):
        prev_row = triangle[i - 1]
        new_row = [1]

        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
  
print(wynik(15))
