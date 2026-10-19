import xlrd
from pprint import pprint

SHEET_NAME = "MS.xls"

# list of 3-tuples
data1024: list[tuple[str, str, str]] = []

# read 1024 data into list
book = xlrd.open_workbook(SHEET_NAME)
sheet = book.sheet_by_index(0)
for row in range(0, sheet.nrows):
    rowTuple = tuple(
        sheet.cell_value(rowx=row, colx=i) for i in range(0, 3)
    )
    assert len(rowTuple) == 3
    data1024.append(rowTuple)

# get total unique pieces in stage
uniquePieces: set[str] = set()
for set1024 in data1024:
    for piece in set1024:
        uniquePieces.add(piece)

# get covered pieces from each set in file
piecesCovered: set[str] = set()
with open("setlist.txt", "r") as f:
    for line in f.readlines():
        curSetID = int(line)
        curSet1024 = data1024[curSetID]
        for piece in curSet1024:
            piecesCovered.add(piece)

# display results

pprint(uniquePieces - piecesCovered)

print(f"{len(uniquePieces)=}")
print(f"{len(piecesCovered)=}")
