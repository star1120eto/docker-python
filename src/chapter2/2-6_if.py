print("◆どれがTrueか")
if 2 * 2 * 2 + 2 == 10:
    print("2*2*2+2は10")
if 2 + 2 * 2 + 2 == 10:
    print("2+2*2+2は10")  # これは8だからfalse
if (2 + 2) * 2 + 2 == 10:
    print("(2+2)*2+2は10")

print("◆数値の比較")
if 1 == 1:
    print("1番目はTrue")

if 5 ^ (4 - 4) + 9 == 10:
    print("2番目はTrue")

if 2 < len([0, 1, 2]):
    print("3番目はTrue")

if sum([1, 2, 3, 4]) < 10:
    print("4番目はTrue")

print("◆文字列の比較")
if "AUG" == "AUG":
    print("1番目はTrue")

if "AUG" == "aug":
    print("2番目はTrue")

if "あいう" == "あいう":
    print("3番目はTrue")

print("◆in演算子")
if "GAG" in "AUGACGGAGGCUU":
    print("1番目はTrue")

if "みんなのpython の学習履歴" in "学習":
    print("2番目はTrue")

if "Debian Python Mamba" in "Debian Python Mamba Debian Python Mamba":
    print("3番目はTrue")

print("◆リストの比較")
if [1, 2, 3, 4] == [1, 2, 3, 4]:
    print("1番目はTrue")

if [1, 2, 3] == [2, 3]:
    print("2番目はTrue")

if [1, 2, 3] == ["1", "2", "3"]:
    print("3番目はTrue")

print("◆リストの検索")
if 2 in [3, 4, 6, 8, 45]:
    print("1番目はTrue")

if 24 in [13, 24, 35, 46, 57, 58]:
    print("2番目はTrue")

if "フォーマット" in ["Ruff", "フォーマット", "Format", "リント", "Lint"]:
    print("3番目はTrue")
    
# 以降のif-else文、if-elifはスキップ